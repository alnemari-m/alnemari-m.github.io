"""
Fetch arXiv papers authored by Mohammed Alnemari.
Runs monthly via GitHub Actions, writes to _data/arxiv_papers.yml
"""

import requests
import xml.etree.ElementTree as ET
import yaml
import os
import time
from datetime import datetime

# Author search queries — covers name variations
AUTHOR_QUERIES = [
    'au:"Mohammed Alnemari"',
    'au:"M Alnemari"',
    'au:"M. Alnemari"',
    'au:"Mohammed H Alnemari"',
    'au:"M. H. Alnemari"',
]

ARXIV_API = "http://export.arxiv.org/api/query"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "_data", "arxiv_papers.yml")

NAMESPACE = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


def fetch_arxiv_papers():
    """Query arXiv API for all name variations and deduplicate."""
    all_papers = {}

    for query in AUTHOR_QUERIES:
        params = {
            "search_query": query,
            "start": 0,
            "max_results": 50,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }

        try:
            resp = requests.get(ARXIV_API, params=params, timeout=30)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"Warning: Failed to fetch for query '{query}': {e}")
            continue

        root = ET.fromstring(resp.text)

        for entry in root.findall("atom:entry", NAMESPACE):
            arxiv_id = entry.find("atom:id", NAMESPACE).text.strip()
            # Normalize ID: extract just the ID part
            arxiv_id = arxiv_id.split("/abs/")[-1]

            if arxiv_id in all_papers:
                continue

            title = entry.find("atom:title", NAMESPACE).text.strip().replace("\n", " ")
            # Collapse multiple spaces
            title = " ".join(title.split())

            summary = entry.find("atom:summary", NAMESPACE).text.strip().replace("\n", " ")
            summary = " ".join(summary.split())
            # Truncate long abstracts
            if len(summary) > 300:
                summary = summary[:297] + "..."

            published = entry.find("atom:published", NAMESPACE).text.strip()
            year = published[:4]
            date = published[:10]

            authors = []
            for author in entry.findall("atom:author", NAMESPACE):
                name = author.find("atom:name", NAMESPACE).text.strip()
                authors.append(name)

            # Get categories
            categories = []
            for cat in entry.findall("atom:category", NAMESPACE):
                categories.append(cat.get("term", ""))
            primary_category_el = entry.find("arxiv:primary_category", NAMESPACE)
            primary_category = primary_category_el.get("term", "") if primary_category_el is not None else ""

            # Get PDF link
            pdf_link = ""
            for link in entry.findall("atom:link", NAMESPACE):
                if link.get("title") == "pdf":
                    pdf_link = link.get("href", "")
                    break

            all_papers[arxiv_id] = {
                "arxiv_id": arxiv_id,
                "title": title,
                "authors": authors,
                "abstract": summary,
                "year": int(year),
                "date": date,
                "primary_category": primary_category,
                "categories": categories[:5],
                "pdf_url": pdf_link,
                "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
            }

        # Be polite to arXiv API
        time.sleep(3)

    return all_papers


def is_alnemari_paper(paper):
    """Verify the paper actually has Alnemari as an author (not just a citation match)."""
    name_variants = ["alnemari", "al-nemari", "al nemari"]
    for author in paper["authors"]:
        if any(v in author.lower() for v in name_variants):
            return True
    return False


def main():
    print(f"Fetching arXiv papers... ({datetime.now().isoformat()})")

    all_papers = fetch_arxiv_papers()
    print(f"Found {len(all_papers)} total results")

    # Filter to confirmed Alnemari papers
    confirmed = {k: v for k, v in all_papers.items() if is_alnemari_paper(v)}
    print(f"Confirmed {len(confirmed)} papers with Alnemari as author")

    # Sort by date (newest first)
    sorted_papers = sorted(confirmed.values(), key=lambda p: p["date"], reverse=True)

    # Load existing papers to preserve any manual additions
    existing = []
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            existing = yaml.safe_load(f) or []

    existing_ids = {p.get("arxiv_id") for p in existing}

    # Merge: keep existing entries, add new ones
    new_count = 0
    for paper in sorted_papers:
        if paper["arxiv_id"] not in existing_ids:
            existing.append(paper)
            existing_ids.add(paper["arxiv_id"])
            new_count += 1
            print(f"  NEW: {paper['title'][:80]}... ({paper['arxiv_id']})")

    # Re-sort by date
    existing.sort(key=lambda p: p.get("date", ""), reverse=True)

    # Write output
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(existing, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nDone. {new_count} new papers added. Total: {len(existing)} papers.")
    print(f"Written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
