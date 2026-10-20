# Brama mascot — brief and prompt pack

Status: **concept stage, nothing rendered yet.** The prompts below are ready to run with
`generate.py` as soon as a `GEMINI_API_KEY` is available in the environment.

Reference point the founder raised: OpenAI's **dots** (DevDay, 29 Sep 2026). They're plush,
blobby characters (a green bean, a cloud in a beret, a bunny with headphones) that you can
customise. Meta's equivalent is Jolly, a fuzzy egg.

---

## 1. Should a reliable, results-first brand have a fluffy mascot?

**Short answer: yes, but the mascot should not be the one doing the grading.**

Who we're designing for (see `research/context/project-context.md`): adults whose residence
permit, citizenship, university place or nursing licence depends on a single 730 PLN exam. Many
of them are studying in a language that isn't their first. The Job is
`I want to pass B1 on the first attempt`, and the strongest negative emotion around it is fear.
They're afraid of failing, of wasting the fee, and of a reputation hit in a diaspora where
everyone talks.

So two things have to be true, and they pull in opposite directions:

| What the brand must do | What a fluffy mascot does |
|---|---|
| **Be believed when it says "you're ready."** The grader is the product. If its score feels like a game, nobody trusts it with a 730 PLN decision. | Toy-like cuteness signals "game" and "Duolingo." It also prompts the Clippy and Fairplay criticism that dots is already getting: *cute face, serious stakes.* |
| **Lower anxiety.** Removing a negative emotion is one of the strongest value mechanics. | A soft, calm creature is very good at this. It works at 2am, before a mock oral, or after a failed module. |

**The resolution is a division of labour:**

- **The score speaks in the brand's own voice:** clean type, numbers, per-module pass/fail, no
  mascot in the room. This is the "reliable" part.
- **The mascot is a companion, not an examiner.** It shows up at the edges: onboarding, streaks,
  "you finished a full mock," failure recovery, Telegram stickers. This is the "less scary" part.
- **Fluffy, but heavy.** Choose a dense, grounded, low-centre-of-gravity character over a
  floaty, fragile one. It should read as *steady and on your side*, not *silly*.

**On the butterfly:** it's a poor fit for this brand. It reads as fragile and flighty, and its
symbolism is about transformation. The user wants to stay themselves and get a stamp.
"Reliable" and "result-oriented" point to something sturdy that walks *through* a gate rather than
fluttering over it.

**On a non-identifiable blob:** this is a safe fallback, and it's the dots approach. It's cheap
to produce and easy to make into stickers. Its weakness is that it means nothing on its own, so
all of its meaning has to come from colour and context.

## 2. Concepts to prototype

*Brama* means **gate** in Polish. Each concept tries to carry that meaning.

1. **Żubr calf (lead concept).** A plush baby European bison. The żubr lives in the Białowieża
   forest, right on the Belarus–Poland border, and it's a national symbol on *both* sides. That
   fits the Job B audience (Belarus → Karta Polaka) and Job A (already in Poland). A bison is the
   most "solid and reliable" animal you could pick, and a calf softens it.
   Risk: Żubrówka and Żubr beer own the adult bison image in Poland. Keep it a round, young calf
   with no horns.
2. **Gate-blob.** A non-identifiable plush creature whose body is an arch or doorway shape. It's
   the dots style with meaning built in. You walk *through* it.
3. **Stork (bocian).** A soft, round stork chick. Poland hosts about a quarter of the world's white
   storks, and the stork is a migration symbol (it comes back every year). Risk: babies/delivery
   connotations.
4. **Butterfly (control).** Rendered so the founder's original idea can be judged side by side,
   not dismissed on paper.

Shared style for all four: soft felt/plush 3D, studio lighting, a warm neutral background, a
restrained palette (one brand accent, not rainbow), and calm eyes rather than manic ones.

## 3. How to validate (don't decide this on taste)

The mascot is **not** the riskiest assumption. That's still *will anyone pay for AI-scored
prep* (project context §9/§11). Spend at most a few hours here.

The cheapest useful test is to pin 3–4 renders in the Telegram/Viber groups you're already
recruiting from, or show them at the end of the customer interviews, and ask *one* question:

> "Если бы этот персонаж сказал вам «вы готовы к экзамену» — вы бы поверили?"
> *(If this character told you "you're ready for the exam", would you believe it?)*

If people laugh, the mascot stays on stickers and onboarding and never goes near a score. If
they say "yes, it's calming," you can give it a bigger role.

## 4. Generate

```bash
export GEMINI_API_KEY=...            # set as an environment secret, never commit it
python3 brand/mascot/generate.py     # → brand/mascot/out/<concept>-<n>.png
python3 brand/mascot/generate.py zubr gate --n 4
```

Override the model with `GEMINI_IMAGE_MODEL` if a newer image model is available.
Prompts live in `generate.py` (`CONCEPTS`), so you can edit them there.
