# Praktika — marketing & distribution teardown

Compiled 2026-10-10. Purpose: understand how Praktika gets its downloads and revenue, and decide what (if anything) transfers to the Polish B1 certification-prep project ([`context/project-context.md`](context/project-context.md)).

**How this was sourced, read first.** All research came from web-search results and snippets. The research environment's proxy blocked direct page loads (TikTok, praktika.ai, TechCrunch, Social Blade, Meta Ad Library all returned 403). Follower counts are cached snapshots of unknown date. Every number is tagged:
- **[co]** — the company's own claim, via press or vendor case studies
- **[est]** — third-party estimate (Sensor Tower, GetLatka, Dealroom, etc.)
- **[1-src]** — a single secondary source, unverified
- **[inf]** — my inference

**Name check.** The app is **praktika.ai** (App Store id 1624701477, Android `ai.praktika.android`). **praktika.app is a different, unrelated company** — "Practico", a meditation app from PRAKTIKA, INC. (Charlotte, NC). The confusion is understandable: Praktika's TikTok handle is **@praktika.app**.

---

## 1. The company in one screen

| | |
|---|---|
| **What it is** | 1-on-1 spoken practice with photorealistic AI-avatar tutors: role-plays, pronunciation and grammar feedback. Started as English for non-native speakers. Now 9–12 study languages, depth varies. |
| **Founders** | Adam Turaev (CEO, HSE Moscow), Anton Marin (CTO, ex-relayr/Rakuten), Ilya Chernyakov (CPO/COO, ex-Sanofi/Bosch). All three previously co-founded **Cleverbots**, a Dubai B2B conversational-AI company (clients: Coca-Cola, AstraZeneca). All three grew up in immigrant families. A Russian-speaking team. |
| **Base** | Delaware entity. Press calls it "London-based". Team in 19 countries: UK, UAE, Armenia lead. About 50 people **[est]**. |
| **Launched** | June 2022. Early on: ~30k active users, **half of them in Brazil** **[co]**. |
| **Funding** | $2.5M seed (Creator Ventures, Blue Wire). **$35.5M Series A, May 2024, led by Blossom Capital**; angels include ElevenLabs' Carles Reina and Patrice Evra **[co]**. No round found in 2025–26. |
| **Revenue** | ~**$20M over the trailing 12 months as of May 2024**, 1.2M MAU, 100+ countries **[co]**. Revenue up >20× from 2023 to 2024 **[co, Amplitude]**. In January 2026, OpenAI's case study claims a "2× revenue" lift from the multi-agent tutor **[co]**. Sensor Tower: ~$1–2M/month on iOS **[est]**. My read: probably **$30–50M+ annualised in 2026** **[inf]**, but no hard number since 2024. |
| **Scale** | 15M downloads, 2M+ MAU (2025, **[co]**). Google Play 10M+ installs, 4.6★ from 1.2M reviews. iOS 4.8★ **[est]**. |
| **Tech** | OpenAI GPT-4.1 / GPT-5.2, multi-agent: Lesson, Student-Progress and Planning agents. ElevenLabs TTS (+15% session length). Amplitude for experiments. Adjust for attribution **[co, vendor case studies]**. |
| **Trust** | Trustpilot 3.6/5. Recurring complaints: charged before the trial ended, refunds refused, ads showing avatars that aren't in the app **[est]**. |

---

## 2. How they actually got the downloads — the engine

### 2.1 Entry market: Brazil, not home turf
- **Brazil was chosen because only ~5% of Brazilians speak English** **[1-src]**.
- It is a huge, mobile-first, English-poor market with cheap creator rates and a big English-teacher creator scene.
- They skipped CIS and their own network entirely.
- Telegram and WhatsApp campaigns were tried and **failed** **[1-src]**.

### 2.2 The lever: creator videos where the product *is* the content
The single best-documented growth event **[1-src, Consumer Startups]**:
- **The creator.** Praktika signed a Brazilian English-teacher creator, "Gustavo". He had only ~10k followers but 2–3M views per video.
- **The format.** He talks to the AI avatar while **deliberately making ridiculous English mistakes**. The avatar reacts and corrects him.
- **The reach.** One video reportedly hit ~12M views on Instagram and ~10M each on TikTok and YouTube. The likely match is TikTok @gustavosilvaingles, Jan 2024, ~635k likes **[inf]**.
- **The amplification.** Praktika then put **paid spend behind the winning creator video** (Spark/whitelisted-style ads **[inf]**).
- **The lock-in.** Gustavo was signed to an exclusive content deal, described as "acquihire-like".
- **The result.** MRR went from ~$1K after the first influencer to ~$100K within three months **[1-src]**. The source attributes ~$1M → $12M ARR to this format.

**The pattern repeated across markets [snippet-verified posts]:**
- **@nesly.english (Turkey).** "I am Türkiye ❌ I am from Türkiye ✅ Download Praktika… #ad". It carries a per-creator **Adjust tracking link**.
- **Elsewhere.** Spanish, Japanese, Korean, Thai and Russian teacher-creators, each labelled "Paid partnership".
- **The common shape.** The same hook every time: *the typical mistake of this nationality → fixed by talking to the avatar*.

**Why it works [inf, AJTBD lens]:** the video loads every Consideration Activator at once.
1. **New way to do the Job.** "Practise speaking with an AI, not a human tutor."
2. **Value delta.** Instant, free to start, available at 2am.
3. **Named product + entry path.** "Download Praktika, link in bio."
4. **Fear removed: embarrassment.** The creator is *laughing at his own mistakes*. The core fear of the segment, being judged while speaking, is shown as irrelevant here.
5. **Old way fired.** It is implicit: a human tutor is expensive and judging you.

The value proposition is demonstrated, not claimed. That's the whole trick.

### 2.3 Owned channels — a support act, not the engine
- **TikTok @praktika.app.** ~540k followers, ~3M likes **[cached]**. Content:
  - avatar product demos ("Next Gen Avatars")
  - recurring avatar characters ("Speak English with Dwayne")
  - promo posts ("50% off after the placement test")
  - multilingual hashtags: Spanish, Portuguese, Arabic
- **Instagram @praktika.ai.** ~1M followers. Bio: "10,000,000+ students".
- **No regional brand accounts.** Regional reach comes via creators.
- **UGC challenge.** #PraktikaChallenge2025, Jan 2025: users post a screen-recording of themselves talking to their tutor. Ranked by in-app "friendship points", top prize a London trip. **This turns users into creators of the exact winning format.**

### 2.4 Scaling the creator lever into a system
- **Affiliate programme** (praktika.ai/affiliate). Open to creators, teachers and communities. **30% commission**; one creator claims 50%.
- **Hiring.** "Influencer Coach" contract role. A Brand Director role covering an *AI-influencer strategy*, a *micro-influencer programme* and Meta Ads.
- **Paid UA.** Meta + Google, measured on **trials and subscriptions per creative**, not installs (Adjust case study).
- **Word of mouth.** Claimed at ~60% of new users later on **[1-src]**.

### 2.5 Funnel and monetisation
- **Onboarding.** Long and personalised: **~30 screens**. It asks about level, motivation, **speaking fears**, past methods, interests and practice time. Then a vocabulary check, then a generated study plan, **then** the paywall.
- **Web funnel.** A vocabulary test whose *result is shown before the paywall*.
- **Soft paywall.** The free tier gets 3 avatars. The paywall screen is closable.
- **Plans.** Weekly, monthly, quarterly and annual, plus a $99.99 lifetime plan seen in the US store.

| Channel | Price |
|---|---|
| US iOS | ~$9.99/mo, $49.99 for 3 months, $119.99/yr |
| Web | €11.99/mo, €59.99/yr — **cheaper than in-app**, avoiding the store cut |
| Brazil | R$199–399/yr tiers, likely A/B tests |

- **The trial is where trust breaks.** "7-day free trial" auto-converts to a quarterly or annual plan. This is the source of most Trustpilot anger.

### 2.6 PR and other channels
- **One coordinated press burst** at the Series A. The traction numbers (1.2M MAU, $20M) were the hook.
- **Free global PR from AI vendors' case studies** (OpenAI, ElevenLabs, Amplitude, Adjust), translated into many languages.
- **B2B page and scholarship programme** exist, but are minor.
- **Not found:** telco, OEM or government deals, and Apple/Google editorial features.

### 2.7 How competitors entered, for contrast
| | Entry route |
|---|---|
| **Praktika** | Brazil via creators → paid amplification |
| **Speak** | Korea via App Store top charts + big rounds |
| **ELSA** | Vietnam via schools / B2B |
| **Langua** | Clones partnered YouTubers' voices, so creator distribution is built into the product |
| **Talkpal** | SEO comparison pages |

---

## 3. Diagnosis — why Praktika works (and where it's fragile)

**Segment and Job [inf].**
- **Who.** Adults in English-poor emerging markets: Brazil, Turkey, Vietnam, Iran.
- **Core Job.** *I want to practise speaking English out loud* in order to *stop freezing when I have to speak* (job, travel, status).
- **Priority order of success criteria:** no embarrassment > price > availability > accuracy.
  - The tutor is the incumbent Solution. It fails on criterion #1 (a human is judging me) and #2 (cost; they claim "50× cheaper").

**Value mechanics.**
- **Eliminate a negative emotion:** the shame of speaking. That is the main one.
- **Lower cost:** money and scheduling.

**Fragility.**
- **Promise ≠ delivery.** Ads show avatars and live correction the app doesn't have, which manufactures Problems. The 3.6 Trustpilot score and refund fights are the bill for that.
- **Billing tricks** convert well short-term and poison word of mouth.
- **Commoditised category.** Speak is at a $1B valuation, Duolingo Video Call exists, and dozens of clones. Their moat is the creator machine plus brand, not the tech.

---

## 4. What to take for the Polish B1 project — and what not to

Context: solo founder, no ad budget, ~8k buyers/yr, a **one-off Job with a deadline** ("pass B1 to keep legal status / get citizenship"), a Russian-speaking diaspora where *everyone talks*.

### Take these

1. **The ad is a recording of the product doing the Job.**
   - Praktika's Gustavo video, transposed: *a person sits a mock B1 oral with the AI examiner, in Polish, and gets a per-module score and a Russian-language explanation of what would have failed.*
   - Best variant: show the three real failure modes examiners name — off-instruction writing, unfinished text, missed oral task elements — being caught.
   - This loads all five Consideration Activators in 60 seconds:
     - **Job Graph:** practise with an AI examiner.
     - **Value delta:** a score tonight instead of a 730 PLN surprise.
     - **Product + link.**
     - **Fear removed:** "will I fail?" becomes a number.
     - **Competitor fired:** a 3-month Białystok course on fixed evenings.

2. **Micro-creators chosen by views, not followers, paid per tracked link.**
   - **Who:** Russian- and Ukrainian-language "польский язык" / "Karta Polaka" / "переезд в Польшу" creators on TikTok, Reels, YouTube Shorts and Telegram.
   - **How:** each gets their own tracking link (UTM or promo code) plus a **30% affiliate cut**.
   - **Then:** amplify the one format that wins. Praktika's whole curve came from *one* creator and *one* format; you need to find yours, not run 50.

3. **Nationality-specific mistake hooks.**
   - The "I am Türkiye ❌" pattern maps directly onto "ошибки русскоязычных на экзамене B1".
   - Examples: false friends (*zapominać*, *uroda*), aspect, cases after numerals.
   - This is native, shareable content that *only someone teaching from Russian can make*. That is your differentiation, made visible.

4. **A diagnostic quiz whose result comes before the paywall.**
   - Praktika's vocab test → results → plan → paywall becomes **"Проверка готовности к B1 за 10 минут"**.
   - It scores each module against the real pass rule (≥50% in *every* module) and shows *which module you'd fail today*.
   - It is lead magnet, demo and Aha Moment in one. It is also the cheapest thing to build first.

5. **Web checkout, no app store.**
   - Praktika routes users to cheaper web pricing. You can skip the stores entirely: web or Telegram bot plus bePaid/Stripe.
   - That keeps 15–30% margin that Praktika gives Apple.

6. **Turn customers into the creators.**
   - Praktika's challenge had users post screen-recordings. Yours: "share your mock-exam score" or "сдала B1 — вот мой путь" stories.
   - In a diaspora, a pass story with a named product is the strongest Consideration Activator there is.

7. **Use vendor and community PR.** You are an agent engineer with an O'Reilly workshop. "How I built an AI examiner for the Polish state exam" is content the AI-builder audience shares. It won't sell to learners, but it builds credibility and opens partner doors with schools.

### Do NOT take these

- **Annual or auto-renewing subscriptions and trial-to-annual tricks.**
  - Your Job is one-off with an exam date. Price it as a **pack until the exam** (e.g. "до экзамена", N mock exams) or a fixed-term pass.
  - In a community where everyone talks, one "списали деньги" thread kills you. Praktika's 3.6★ is the warning.
- **Ads that overpromise.** Never imply NAWA/commission endorsement and never promise a pass. Calibrate the score against real outcomes. Promise must match delivery, or you manufacture the Problem yourself.
- **Paid-UA-first growth.** Praktika could buy amplification with $35M. You can't, and general language learning is already a killed idea (§8 of the context file). Only pay to boost a creator video *after* it has proven itself organically.
- **Expanding languages early.** Praktika's breadth came after the engine worked in one market with one language.

### One important difference: Telegram

Praktika found Telegram and WhatsApp *failed*. Don't over-read that.
- **Their use was mass broadcast** to a broad market.
- **Your segment *lives* in Telegram groups**: Belarusians in Poland, Karta Polaka chats.
- Those groups are where trust and referrals travel, so they're a channel to test, not one to drop.

---

## 5. Riskiest assumption and the cheapest test

**Order matters (canon: communication §1).** Don't scale communication before value is proven. The interviews in [`interview-script.md`](interview-script.md) come first: they answer "will anyone pay". The creator channel is the *next* assumption.

**Assumption, stated so it can be falsified:**
> Russian-language Polish-teacher micro-creators (TikTok/Reels, 5–50k followers), posting a 60-second "mock B1 oral with an AI examiner" video, drive ≥1% of viewers to the free readiness check. ≥5% of those pre-pay €X for exam prep. Audience: Belarusians in Poland, 2026 exam sessions.

**Cheapest test (~2 weeks, ~€300–500):**
1. Build only the readiness check plus a recorded mock oral. Wizard-of-Oz is fine: ChatGPT prompt + manual scoring.
2. Pay 3 creators €50–150 each, one video each, with separate links.
3. Measure views → check completions → pre-payments per creator.
4. **Kill/continue rule:** 0 pre-payments across 3 creators = the format or segment is wrong. Pre-payments from one creator = find out why that one and double down. That one is your Gustavo.

---

## 6. Gaps worth closing by hand (a few minutes in a normal browser)

- **Meta Ad Library**, search "Praktika": count live creatives and note the angles.
- **TikTok Creative Center → Top Ads**, search "Praktika".
- **@praktika.app on TikTok**: current followers, posting frequency, top 10 videos by views.
- **Russian-language Polish-teaching creators**: list 20 with average views per video — that's your creator shortlist.

## Sources (main)
TechCrunch 2024-05-22 (Series A); tech.eu; EU-Startups; openai.com/index/praktika (2026-01); amplitude.com/blog/praktika-experimentation-and-revenue-growth; elevenlabs.io/blog/praktika-scales-immersive-language-learning-with-elevenlabs-tts; adjust.com/resources/case-studies/praktika; consumerstartups.com/p/praktika-ai; startupi.com.br/?p=220633; growthgems.substack.com (GG #131); screensdesign.com/showcase/praktika-ai-language-tutor; praktika.ai/affiliate; praktika.ai/blog/praktika-challenge-2025; intercom.help/praktika-ai; trustpilot.com/review/praktika.ai; oh-yeah-sarah.medium.com (teacher review, 2026-03); tiktok.com/@praktika.app; tiktok.com/@nesly.english/video/7368875747450031365; tiktok.com/@teachergustavosilva/video/7324698950999526662; dealroom.co; getlatka.com; app.sensortower.com/overview/1624701477; appbrain.com.
