# Project Context — Polish Language Certification Prep (working name: TBD)

Context handoff document. Paste into Claude Code at the start of a session.
Compiled September 2026. All figures are as researched on that date — re-verify anything time-sensitive.

---

## 0. How to use this file

This is a context dump from a long strategy conversation, written so you don't have to re-derive any of it.

**Section 8 lists ideas already evaluated and killed, with reasons.** Read it before proposing anything. Re-suggesting a killed idea wastes the session.

**Section 9 is the live open question.** That's what needs work.

---

## 1. Founder context

- Belarusian, grew up in Minsk, currently in the United States
- Combined BS/MS at Johns Hopkins — Applied Math & Statistics, Master's in data science
- Background across AI, data science, embedded systems; internship on IoT sensor data
- Writing a technical book, *AI Agent Engineering* — 20 chapters, 6 parts, building agents from scratch in Python
- Has a paid invitation from O'Reilly for a live workshop series, "Zero to Agent in 30 Minutes"
- Core technical strength: **agent engineering**. LLM orchestration, tool loops, evaluation
- Has shipped: Telegram bot on Google Cloud Run, Vue.js frontend work, Python throughout

**Relevant constraints:**
- Physically in the US → US tax reporting obligations attach to any foreign company (Form 5471, FBAR, possibly GILTI). Needs a real tax advisor before registering anything anywhere.
- Student, so time-constrained, but a multi-year horizon is acceptable
- Has **no proven distribution yet** — a book in progress and workshop invitations are a channel, not an audience. Nobody has paid her for anything she has made. This is the single most important open fact.

---

## 2. The product

**AI-powered preparation for Polish language certification, taught from Russian / Belarusian / Ukrainian rather than English.**

The core product is **not lessons**. It is a **grader**:
- Full-length timed mock exams
- Written tasks marked against the real rubric
- Scored mock orals with a transcript

**The strategic thesis, which surfaced independently three times in research:** build for people the English-first world skips. Every incumbent teaches from English. The people who actually need these certificates are East Slavic speakers studying through an English-language app in a language they also don't command.

---

## 3. Why the demand is structural (Poland)

- **B1 certificate is legally required** for Polish citizenship (uznanie za obywatela) and for permanent residence / EU long-term resident status. B1 is by far the most-taken level for exactly this reason.
- Since **1 July 2025** the certificate is also a required document for university admission in Poland.
- Nursing boards expect B1 for foreigners in Polish hospitals; civil service B2.
- **From 9 June 2026** the threshold for obtaining a certificate *without* sitting the exam rose from B1 to B2 — pushing more people into the actual test.
- There is exactly **one official exam**, run by the state commission (Państwowa Komisja) and administered through NAWA at authorized centers.

**Population:**
- Poland crossed **2.0 million foreigners** with valid residence permits (April 2026), just over 5% of the population
- 1.55M Ukrainians, 139,300 Belarusians, then Indians (26,100), Georgians (22,200), Russians (19,500)
- Only **191,000** hold permanent or EU long-term status; **758,000** on temporary permits
- ~**960,000 Ukrainians** on temporary protection now being phased out → must convert to a status requiring B1
- Jan–May 2026: **23,280 Belarusians** applied for Polish residence permits
- Foreign workers: 1.14M, up 7.2%. Citizenship grants hit a record in 2025.
- **~1.71M of the 2M are East Slavic speakers** — the addressable base language group

---

## 4. Market sizing (hard numbers separated from assumptions)

**Hard data:**
- **27,518 people sat the state certificate exam in 2025**, up from ~1,000 in 2016 (~45% CAGR)
- First 2026 session alone: 68 locations, ~9,000 candidates
- Exam fee: ~**730 PLN / €170** (€150 exam + €20 certificate)
- Existing prep courses price at **800–1400 PLN** (€190–330)

**Modeled (assumptions, not data):**
- **TAM** ≈ €10–12M/yr — all Polish certification prep spend including language schools
- **SAM** ≈ 8,000 buyers/yr × €60–120 = **€0.5–1.0M/yr**
  - derivation: 27.5k takers → ~70% adult B1 → ~85% East Slavic → ~50% would buy self-study software
- **SOM** — solo founder, no ad budget, Telegram-community distribution:
  - Year 1: 3–5% of SAM → 250–400 customers → **€20–35k**
  - Year 3: 10–15% → ~1,000 customers → **€80–100k**

**Conclusion: beachhead, not destination.** Big enough to win precisely because it's too small for a funded competitor to enter. Too small to be the end goal.

**The reusable asset** is the engine — *certification exam prep taught from a non-English base language*. Second market if Polish works: **German telc B2 Pflege from Russian/Ukrainian** (nursing shortfall ~100k now, projected 500k by 2035; German immigration law hard-codes language levels into visa outcomes — A1 for family reunification, B1 for permanent residence, B2 for nursing; Chancenkarte scores A2=1pt, B1=2pts, B2+=3pts). That market is 10–50x larger.

---

## 5. Competition (researched, not assumed)

**Layer 1 — Russian-language B1 prep schools. The real incumbents.**
This is the key correction to the original thesis: **"Polish taught from Russian" is NOT an empty niche.** It's occupied — just not by apps.

- **Zgoda-studio** — 3-month B1 course, groups of 8, taught by members of the exam commission, offices in Warsaw *and Białystok* (the Belarusian hub), also an exam registration site
- **Polski Instytut Językowy** — the most dangerous: an authorized state exam center for B1–C2 *and* a course seller, site localized into Belarusian/Russian/Ukrainian. Vertically integrated.
- **VARIA / kurspolskogo.com** — 1400 PLN with the exam fee bundled in
- **Chowaniak** — 16 lessons, 800 PLN
- **Pan Mickiewicz**, **Mova School** — Russian-language, advertise exam results

**Layer 2 — apps.** Duolingo, Babbel, Busuu, Mondly all have Polish; **none prepares for the state exam**. But **eTutor already shipped a Ukrainian-interface Polish app**, and Busuu gave Ukrainian refugees 90 days of premium free. Established Polish edtech is already in the base-language lane.

**Layer 3 — tutor marketplaces.** Preply (Ukrainian-founded) **owns the SEO** — they publish the "best apps to learn Polish, including for Ukrainians" article that ranks for the target keywords. Plus italki, Superprof, at €10–20/hr.

**Layer 4 — materials.** *Polski krok po kroku* is the pedagogical standard (e-polish.eu platform behind it). startpolish.pl and in-polish.pl run SEO content written by actual examiners. The commission publishes free sample exams.

**Layer 5 — ChatGPT.** Free, speaks Russian, will roleplay the oral exam. Does ~70% of this already.

**Therefore the remaining wedge is narrow and specific:**
1. **Format, not content** — incumbent courses are 3 fixed sessions/week in Warsaw or Białystok. Shift workers, people in other cities, and people still abroad can't attend. Self-paced at €60–120 undercuts by 3–5x.
2. **Scored practice, unbundled** — the schools' real edge is an examiner marking writing and running mock orals. That's now the cheapest thing an LLM does, in Russian, at 2am.
3. **Sell to the schools, not around them** — they have students, credibility and examiners; they have no software. (Currently ranked most promising.)

**What examiners say candidates actually fail on** — not hard grammar, but: writing that doesn't match the instruction, running out of time and submitting unfinished text, and not completing every element of the oral task. **Build the grader around those three.** They are exactly what an LLM catches and a textbook cannot.

**Pass rule:** B1 requires ≥50% in *every* written module plus the oral. Failure is per-module, so scoring must be per-module.

---

## 6. Why this survives where IELTS prep didn't

AI-scored IELTS prep has collapsed to **$1.49–9.99/month** — huge market, abundant free English content, dozens of near-identical clone apps (several built by solo devs with WordPress privacy policies). PREP's AI room grades all four skills against each criterion "like a real examiner."

Polish B1 has 27k annual takers and a rubric that isn't sitting in training data. **Too small for the clone farms to bother.** The commoditization that ruins IELTS economics is what protects this.

**Copy from IELTS apps:** timed full mocks, per-module scoring, task-fulfillment grading, mock orals.
**Copy their disclaimers too:** cannot imply endorsement by Państwowa Komisja / NAWA, cannot promise a score. Score calibration against real outcomes is mandatory from day one — telling someone they're ready and having them fail a 730 PLN exam ends your reputation in a diaspora where everyone talks.

---

## 7. Economic and legal context

**Poland macro (supports the 10–30 year horizon):**
- GDP per capita PPP: 44% of EU average (1995) → 79% (2024) → 83.7% forecast (2027). Overtook Spain in 2025 (~€49,650 vs €49,465). ~87% of UK.
- Growth decelerating: 2021–26 averaged 3.1% (second-weakest 5-yr stretch on record); 2027–31 forecast 2.5% vs ~1% for Germany/France/Italy, 1.7% Spain
- Demographics reverse: fertility **1.068** in 2025 (among lowest globally); population 37.3M → 28.4–29.4M by 2060 (GUS); working-age share 58.1% → 47.6%, roughly **8M fewer working-age people**; total hours worked shrink ~1.2%/yr by 2045–50
- **Implication:** rising incomes → pricing power improves over the horizon. Labour shortfall makes sustained immigration an economic necessity for decades. The pipeline sits downstream of migration policy, not GDP.
- **Biggest single risk:** policy, not demography. Tusk government is tightening intake right now even as the labour math demands the opposite.

**Entity options researched:**

| Option | Online? | Cost | Verdict |
|---|---|---|---|
| Belarus ООО | Partially | 70–300 BYN DIY (~$25–95); registration 1–5 days; уставный фонд from 1 BYN | Cheap but money is trapped in Belarus |
| Poland sp. z o.o. via S24 | Yes, with a qualified e-signature (no PESEL needed — but sources conflict, verify with the signature provider) | ~280–300 PLN official + 300–600 PLN/yr signature + virtual office + ~280 PLN/mo accounting. Notary route = 1400–2000 PLN | **Correct long-term entity** — EUR, Stripe, VAT OSS, credibility with Polish schools. KSeF e-invoicing mandatory from 1 April 2026. |
| Kazakhstan ТОО | No — IIN and ЭЦП require in-person ЦОН visit; embassy issuance closed 31 Dec 2025 | ИИН 5,500 KZT | Irrelevant to this product |
| Kazakhstan AIFC + e-Residency | Yes, fully online (launched Jan 2026) | annual renewal required | e-IIN works **only inside the AIFC perimeter**; tax benefits target financial services. Wrong tool. |

**Belarus self-employment (самозанятость) + bePaid — the cheap starting rail:**
- Software development and tutoring both on the permitted list (Council of Ministers decree №851, 08.12.2022) — the product qualifies
- НПД rate 10% (20% above 60,000 BYN/yr from Belarusian orgs/ИП); no separate ФСЗН contributions
- **From 1 July 2026: minimum monthly tax of 45 BYN** (~$165/yr) regardless of revenue — so register *after* there's someone to charge
- Registration via the "Профдоход" app, ~10 minutes. Income must be recorded by the 7th of the following month.
- bePaid works with самозанятые. No business account needed — an ordinary personal current account works. Free to connect, no monthly fee, **commission 1.2–3%**. Accepts Visa, Mastercard, Maestro, Apple Pay, Google Pay from anywhere. Recurring payments supported. Ready modules for Tilda, GetCourse, WordPress, 90+ integrations. Activation 1–3 days.
- Two tiers for self-employed: E-POS (ЕРИП only, cheap) or full acquiring (cards + ЕРИП, needs a technical site)
- **Risks:** revenue settles in BYN inside Belarus; Ukrainian customers may refuse to pay a Belarusian merchant on principle; EU issuing banks may decline toward Belarusian acquiring (test with a real Polish card before committing)

---

## 8. Already evaluated and rejected — do not re-propose

| Idea | Why killed |
|---|---|
| Agent eval / prompt regression tool | Category closed. OpenAI acquired Promptfoo (Mar 2026, $86M); Braintrust raised $80M at $800M valuation; DeepEval/Ragas/Phoenix free forever |
| Infourok clone for Belarus | The business is the state-licensed certificate, which requires a Ministry of Education license in Belarus. Market ~1/10 of Russia's. |
| SimplePractice for Kazakhstan | Value concentrates in US insurance billing, which doesn't exist there. Where a payer layer does exist (ОСМС), it's a state МИС certification registry — a government-relations business |
| Gusto for Kazakhstan | Real regulatory moat (new Tax Code Jan 2026, VAT 12%→16%) but occupied by MyBuh.kz, Мойучет, 1C at ~$20/mo. No price umbrella, years of accountant-hours, real liability |
| AI clinical documentation, Kazakhstan | Viable but **Ascle** already has it — presented at a government cabinet session April 2026, 52 doctors, ~30 min/day saved |
| Same idea for Belarus | Worse: ЦИСЗ is a centralized state platform whose charter already includes clinical decision support; phase-2 technical order is ДСП (restricted); no language moat since it runs in Russian |
| General AI language learning (reels + AI conversation) | Speak raised $78M Series C at $1B, >$100M ARR; Duolingo at 56.5M DAU / 12.5M subscribers, commoditizing AI features. Acquisition is a paid-marketing war |
| ЦТ/ЦЭ prep for Belarus | ~70–80k school-leavers/yr, one-and-done; **Adukar gives the content away free** and monetizes via live tutoring and university lead-gen |
| Turkish language | Under-served but no deadline forcing anyone to pay |
| TOEFL prep | Same one-and-done churn problem, market 100x more competitive |
| Russia as a market | US persons prohibited from supplying IT consultancy/design and cloud services for enterprise management software to persons in Russia (OFAC, since Sept 2024). Routing via a Kazakh entity doesn't fix it |

**Note on Belarus sanctions:** an earlier assumption that Belarus was covered by the Russia IT-services ban was **wrong**. That prohibition is under EO 14071 and scoped to persons in Russia. Belarus sanctions (EO 13405, EO 14038) are targeted at designated parties; transactions with non-designated Belarusian parties are generally permitted. BIS export controls are a separate regime that *does* reach Belarus. Needs a lawyer, not an assumption.

---

## 9. THE LIVE OPEN QUESTION

**Decision made:** start with Belarus / Belarusians.

**Not yet decided — and these are two different products:**

- **Job A — pass the state certificate exam at B1.** People already in Poland. Driver: residence, citizenship, university admission. Real rubric, 730 PLN fee, published sample exams, defined pass rule.
- **Job B — pass the consular language assessment for Karta Polaka.** People still in Belarus, pre-move. Different assessment, different format, different emotional stakes.

**Why it matters beyond curriculum:** it determines the payment rail. Belarusians still in Belarus → самозанятость + bePaid works cleanly, live in a week. Belarusians already in Poland → they hold Polish cards and think in złoty; skip the Belarusian setup entirely.

**Building for one and selling to the other is the most likely way this fails early.**

---

## 10. Method being used

**Next Move Theory / Advanced Jobs To Be Done** — Ivan Zamesin. Open canon, free.

- Canon: `nextmovetheory.com/library/canon`
- Repo with Claude Code skills: `github.com/zamesin/Next-Move-Theory-Canon-and-Skills`
- Install: the repo's installer drops canon and skills into `.claude/skills`. Invoke as `/nmt-market-research`, `/nmt-analyze-interviews`, `/nmt-craft-value-proposition`, `/ask-nmt`

**Principles that most govern this project:**
1. This is a **one-off Job**, not recurring — people sit the exam once. Interview in past tense, anchored to one concrete instance.
2. **Screen on past expenditure of money, time, or energy.** "I want to learn Polish" is a textbook Fake Job (same shape as an unused gym membership). No past payment → not a respondent.
3. **The competitive set sits at the Big Job, not the Core Job.** Climb with "зачем? чтобы что?" until you reach *перевезти семью* / *остаться легально*. At that level the alternatives are an immigration lawyer, a different visa route, another country, or giving up.
4. **Never accept an abstract answer.** "Быстро" is not data; "за четыре недели" is.
5. **Always sell on the call.** A price and a payment link. It tests at once whether the Job is real, whether money is there, whether the value lands, and what Barriers exist.
6. **Record their exact words.** Paraphrasing swaps their Job for your hypothesis.

---

## 11. What actually needs to happen next

Not more analysis. The one unanswered question in this entire project is **whether anyone will pay her anything**, and no amount of research answers it.

**Immediate:**
1. Recruit 12–15 respondents who have already spent money on Polish, split across Job A and Job B, plus 3–4 who started and quit (they hold the Barriers)
2. Run the interviews with a real offer and a real payment link at the end
3. Decide Job A vs Job B from the grid: importance score × money already spent × dissatisfaction with current solution × did they actually pay
4. Talk to Zgoda in Białystok — closest thing to both customer and competitor, and the most likely B2B partner

**Register nothing until someone has paid.** The 45 BYN/month minimum tax starts on registration.

**Success criterion:** 10 pre-sales means build it. 2 means something cheap and true was learned. 0 means the audience likes her free and won't pay — which is worth knowing before spending a semester on it.

---

## 12. What I want help with in this session

Brainstorming and refining the interview script. The current draft is structured as: emotional contact → qualifying → map the Job Graph → dig 2–3 Jobs in detail → sell → referral, with a post-interview capture table and a decision grid.
