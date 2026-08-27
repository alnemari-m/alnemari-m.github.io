---
title: "The Case for Small AI"
lang: en
date: 2026-08-27
description: "Everyone is watching the giant models in the cloud. The more interesting revolution is the one small enough to fit in your pocket."
translation: /articles/the-case-for-small-ai-ar/
---

When people talk about artificial intelligence today, they usually mean something enormous: models with hundreds of billions of parameters, running in data centers the size of football fields, consuming as much electricity as a small city. The story of AI, as it is usually told, is a story of *bigness*.

I want to tell you the opposite story.

## The AI you never notice

The most useful AI in your life is probably not the chatbot you talk to. It is the one you never notice.

It is the model in your smartwatch that watches your heartbeat all day and taps your wrist when something looks wrong. It is the chip in your hearing aid that separates your friend's voice from the noise of a crowded restaurant, in real time, on a battery smaller than a coin. It is the camera in your car that sees a child step off the curb a fraction of a second before you do.

None of these can afford to send your data to the cloud and wait for an answer. A car cannot ask a server in another country whether it should brake. Your medical data should not need to leave your wrist to be understood. These systems have to think *where they are* — on tiny chips, with tiny batteries, right now.

This is the field I work in, and it goes by many names: edge AI, TinyML, on-device intelligence. But the idea is simple: **make the intelligence small enough to live where the problem lives.**

## We have seen this movie before

In the 1960s, a computer was a mainframe: a machine that filled a room, owned by a corporation, shared by many people through terminals. Computing was something that happened *somewhere else*.

Then computers shrank. They landed on desks, then on laps, then in pockets. And here is the thing people forget: the personal computer was not just a smaller mainframe. It changed *who* could compute and *what* computing was for. Spreadsheets, video games, the web, the photo of your kids as your wallpaper — none of that came from the mainframe world. It came from smallness.

AI today is in its mainframe era. Intelligence lives somewhere else, in someone else's building, and we rent access to it. The shrinking has already begun — and if history is any guide, the most surprising applications of AI will not come from making the giant models bigger. They will come from making intelligence small enough to be *personal*.

## How do you shrink a brain?

You might think a smaller model is just a dumber model. Sometimes it is. But a large part of a big neural network is, frankly, redundant — and there is a whole toolbox for removing that redundancy without removing the intelligence. Three ideas do most of the work:

- **Pruning.** A trained network is like an overgrown garden: many connections contribute almost nothing. You can cut them — often the vast majority of them — and the network barely notices. Like a bonsai tree, what remains is smaller, but it is still a tree.
- **Quantization.** Networks are usually trained with very precise numbers, like measuring flour to six decimal places. For most recipes, "about two cups" works just as well. Storing numbers roughly instead of precisely can shrink a model by four times or more, with almost no loss.
- **Distillation.** Perhaps the most elegant idea of the three: let a large "teacher" model teach a small "student" model. The student does not memorize the textbook — it learns from how the teacher answers. Small models trained this way regularly punch far above their weight.

Combine these and models that once needed a server can run on a chip that costs a few dollars and sips power measured in milliwatts. That is not a rounding-error improvement. That is a different world.

## Why this matters beyond engineering

Small AI is not just an engineering convenience. It changes the answers to three questions that matter to everyone:

**Who sees your data?** If the model runs on your device, your voice, your heartbeat, and your photos can stay with you. Privacy stops being a promise written in a policy and becomes a property of the physics: the data simply never leaves.

**Who gets access?** A farmer with a $30 device and no reliable internet can still get a crop-disease detector. A rural clinic can run diagnostic tools without a data center subscription. Intelligence that requires constant connectivity is intelligence for the already-connected. Small AI travels further.

**What does it cost the planet?** A model that runs on milliwatts instead of megawatts is not just cheaper. Multiplied across billions of devices, efficiency stops being an optimization and becomes an environmental question.

## The best technology disappears

There is an old observation in computing, from the researcher Mark Weiser: *"The most profound technologies are those that disappear."* Electricity was once a spectacle — world's fairs, glowing towers, crowds. Now it is a socket in the wall, and we only think about it when it fails.

AI is still in its spectacle phase. We marvel at the demos, we argue about the giants. But the end state of a truly successful technology is invisibility — and for AI, invisibility means smallness: intelligence woven quietly into hearing aids and irrigation pumps and heart monitors, working for you, near you, without an audience.

The giants will keep their place; some problems genuinely need them. But the revolution worth watching is not on the stage. It is in your pocket, on your wrist, and in a thousand small places you will never think to look.

That is the case for small AI.
