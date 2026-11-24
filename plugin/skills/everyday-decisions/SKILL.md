---
name: everyday-decisions
description: Makes one firm, defensible decision for everyday choices (purchases, home, travel, food, habits, how to spend time or money) when there are several options and the user wants a verdict, not a pros-and-cons list. Use when the user says "help me choose", "which should I get", "X or Y?", "I can't decide", "just tell me what to buy", compares products, plans or places, or keeps going back and forth, even if they never say "decide". Classifies the question and how reversible it is, checks fresh facts and prices, and returns one recommendation with its trade-off and a condition for revisiting. Not for stress-testing a choice the user has already made, business or software-architecture decisions, emergencies, medical or legal crises, or relationship conflicts.
license: MIT
metadata:
  author: Stanislav Fedyna
  version: "1.0.0"
---

# Everyday Decisions: decide, don't dither

## Why this exists

Most everyday choices don't stall for lack of information. They stall for lack of method. People hunt for "the best in the world" when the answer depends on them. They go with gut feel when there is an objective answer. They compare vacuum cleaners for a week when a wrong pick can be returned within 14 days.

This skill produces **one decision you can defend**. It accounts for the user's constraints (budget, home, schedule, tastes), what is already known about this kind of choice, and how costly a mistake would be. Next to it sit a named trade-off and a condition, written down in advance, under which the decision gets revisited. The choice is closed, and nobody has to keep chewing on it.

**Neighbouring skills:** this skill decides **from scratch**, when there is no front-runner yet or too many options. If the user has already settled on an option and wants it attacked, a stress-test or red-team skill fits better. If one is available, hand a high-stakes (Type 1) decision to it after this skill is done.

## Core idea: classify the question first, then answer it

The method depends on the **nature** of the question, not its topic (car, tattoo, dinner):

| Type | What it is | Where the answer comes from |
|---|---|---|
| **A. Has an objective answer** | safety, law, technical compatibility, facts; doesn't depend on the user | primary source, current version: manufacturer, official rules, law, spec sheet |
| **B. Trade-off between parameters** | several decent options differing in specs (price / weight / durability / time) | must-haves → weighted criteria → scoring → check the riskiest assumption |
| **C. "How will I feel", already studied** | habits, purchase satisfaction, commute, sleep, experiences vs things | research (with year and sample, not as law) + the user's own track record |
| **D. Only knowable by trying** | taste, fit, whether a hobby will stick | best guess + the **most reversible** way in (return policy, rental, trial month, second-hand) + a test criterion |
| **E. Values and taste** | two reasonable people with the same data would choose differently | the user's stated priorities and goals as a proxy; regret test; 10/10/10 |
| **F. Urgent / crisis** | health, safety, legal threat right now | **not this skill**: refer to a professional or emergency services |

The second axis is **reversibility**:
- **Type 2**: a two-way door. Can be returned, resold without big losses, cancelled, retried (restaurant, sneakers with free returns, subscription, weekend route).
- **Type 1**: a one-way door, or an expensive rollback. Tattoo, a one-year lease, a car, a move, a non-refundable prepayment, a loan.

"Technically resellable" is not "cheap to undo". If resale loses 20–30%, plus stress and weeks of time, treat it as Type 1.

## On being "100% right"

No judgment comes with a guarantee, and this skill doesn't pretend otherwise. Instead:

1. **One answer.** No "on the one hand… on the other".
2. **Every supporting point carries an evidence level:** `strong` (official spec, law, meta-analysis) · `moderate` (a single study, independent test, large volume of owner reviews) · `consensus` (common advice nobody has checked) · `weak` (one review, an influencer, "everyone buys it").
3. **A revisit condition written before the choice.** The decision is then judged by its process, not by luck, and there is no need to beat yourself up if things turned out worse than they could have.

## Limits of autonomy

The skill **always** decides. In three zones, though, a mistake is costly and invisible until late, so the decision gets the status **"decided — check before <step>"**:

- **Health and medicine** (medication, symptoms, procedures, diets with numbers) → see a doctor before the step.
- **Legal and contractual** (lease, car purchase, self-employment, taxes) → read the contract or get advice before signing.
- **Big money and expensive Type 1** → before paying, get one independent check (e.g. a pre-purchase mechanic inspection) or run a stress-test.

In these zones the skill does not say "consult a professional" *instead of* answering. It makes the decision and holds back only **one named irreversible step** until it is checked. Financial choices are information for the user's own decision, not advice from a licensed financial adviser; label them that way.

## Modes

- **Single question**: the default. "X or Y?", "which power station should I buy".
- **Several questions at once** (planning a trip, fitting out a kitchen): `--one` goes one at a time and stops after each; `--all` runs them in sequence and ends with a summary table. With no flag: `--all` if every question is low-cost Type 2, otherwise `--one`.
- **Quick**: "just tell me what to get". Use the compact block (Step 7), but still run Steps 1–2 and the disconfirming search silently.

## Workflow

### Step 0: Question and context

1. Keep the question verbatim.
2. **Gather context you already have**: anything known about the user (memory, earlier messages, their notes or files if connected): budget, home, city and country, sizes, preferences, past decisions on the same topic. Don't re-ask what is known.
3. If the decision is impossible without a fact (budget, deadline, a hard constraint), ask **1–3 questions in one block**, using a structured question tool if the environment has one. For everything else, make the most reasonable assumption and state it in the decision.
4. If there are several questions, **order them by dependency** (trip city before lodging; car budget before model).

### Step 1: Reframe into something answerable

"Which car is better?" has no answer. This one does: "Pick a first car for city driving and mountain weekends, under budget N, with maintenance under M a year." The shape is **"choose X for Y, given Z"**, where Z is what the decision can later be checked against.

If the type is unclear, the question is probably **compound**. Split it: "which tattoo and where" = taste (E) + pain and healing at that spot (C) + irreversibility (Type 1). Each part gets its own method.

If the question is **factual** ("will this power station run my fridge?"), it isn't decided, it's looked up: specs, a calculation, a source.

### Step 2: Classify and choose the depth

One-minute triage:
1. Is there someone who answers this authoritatively (manufacturer, law, carrier rules, spec)? → **A**.
2. Would the answer change if the person changed? Yes → **C/D** (C if research exists, D if it has to be tried). No, but it depends on priorities → **B**.
3. Could two reasonable people choose differently because of different values? → **E**.

Then reversibility and cost of error:

| | Type 2, low cost | Type 2, noticeable cost | Type 1 |
|---|---|---|---|
| Options | 2–3 (incl. "change nothing / don't buy") | 3–4 | 3–5, at least one unconventional |
| Evidence | ~70% of the information is enough | main sources for the type | full route, primary sources, current prices |
| Debiasing | one disconfirming search | + premortem | + outside view + regret test |
| Answer | compact block | full write-up | full write-up + "check before <step>" in the zones above |

**The 70% rule:** for a reversible choice, waiting for 90% of the information is just slow, because a mistake is cheap to fix anyway. For Type 1 it's the opposite: research until the decision stops moving. **Timebox** low-cost Type 2: if the analysis takes longer than the choice deserves, use the tie-break and close it.

### Step 3: Frame and evidence by type

Write down:
- **Hard constraints**: budget, dimensions, dates, must-haves, decisions the user has already made. An option that breaks one is dropped immediately, with a one-line reason.
- **Facts**, with sources. If a fact is missing, **go and get it**: web search, the manufacturer's site, spec sheets.
- **Evidence route by type:**
  - **A** → primary source and **currency**: this year's carrier rules, the law as currently in force, the spec of the exact model revision. Reviews and forums are for navigation only.
  - **B** → separate must-haves from nice-to-haves. 3–5 criteria that actually separate the options. Find the **trade-off points** (lighter = less capacity) and the **sensitive parameter** (what everything hinges on: real consumption, boot size, distance). Check the riskiest assumption now (calculation, spec, owner reviews on durability).
  - **Prices and availability**: always fresh, from a search, **in the user's market** (major local retailers, price-comparison sites, second-hand marketplaces in their country, in their currency). Never estimate prices from memory; give the date checked.
  - **C** → what research says (year, sample, context), and what has or hasn't worked **for this particular person**. Their own track record weighs as much as the research.
  - **D** → best guess from C + the **most reversible** way in: buy with free returns, rent, buy second-hand and resell, a trial class, a smaller size. Write down how to test it ("two weeks of use: do I reach for it daily?").
  - **E** → the person's stated goals and priorities (from memory or earlier conversation). Tools: **regret test** (what will I regret at 80 if I don't?), **10/10/10** (how will I feel in 10 minutes / months / years?), **coin test** (flip one mentally: which side were you hoping for?). These give structure, not a verdict.

### Step 4: Generate options separately from scoring

List them all first, then score. Otherwise the first attractive option swallows the rest.
- **Status quo / don't buy / postpone**: always. It often wins, and without it you can't see whether a change is worth the money.
- **The options from the question.**
- **An unconventional one**: rent instead of buy, used instead of new, borrow from a friend, combine two cheaper things, reframe ("do you need the thing, or can the problem be solved differently?").

Present each option in its strongest form. No straw men.

### Step 5: Criteria, scoring, robustness

1. **Criteria before scoring.** Weight in words: `decisive` / `important` / `minor`. Default order when context doesn't say otherwise: **safety and health > must-haves > total cost of ownership (not just purchase price) > everyday convenience > looks and nice-to-have**.
2. **Score with support**, each point with its evidence level. "Everyone buys it" and "an influencer recommended it" are not support.
3. **Robustness check.** Does the winner change if one criterion's weight moves up or down a notch? If so, name that weight as the weak spot: "if weight matters more to you than capacity, take Y."

### Step 6: Debiasing: procedures, not a lecture

Knowing about biases doesn't help by itself; procedures do (depth per the Step 2 table):
- **Disconfirming search.** Before scoring, write down what would change your mind. Then search **against** the leader: "<model> problems", "<model> failure", "why I returned <model>".
- **Steelman the runner-up**: the strongest argument for the option that lost.
- **Premortem**: "Six months from now I regret this choice. Why?" 3–5 concrete reasons; for the realistic ones, a countermeasure or a changed decision.
- **Outside view** (Type 1): how choices like this usually end, for this person before and for people in general (a first car: maintenance underestimated; impulse buys "for a hobby": gathering dust).
- **Everyday traps to catch**: anchoring on the first price or a "-40%" discount; sunk cost ("I've already spent so much repairing the old one"); FOMO and the artificial deadline of a sale; social proof; the endowment effect (overvaluing your own item when reselling); the paradox of choice (past 4–5 options, more choice barely improves the pick and lowers satisfaction).

### Step 7: The decision

Full form:
- **Decision**: one sentence, no conditional branches.
- **Y-statement**: "In the context of <…>, to achieve <goal>, I choose <option> over <alternatives>, accepting <trade-off>." The named trade-off is mandatory: if you can't see one, you haven't seen the price yet.
- **Classification**: type · reversibility · cost of error.
- **Why**: 2–4 supporting points with evidence levels and sources.
- **Rejected**: one line per option.
- **Confidence**: `high`, or `medium` (options were close and a tie-break decided it; name which one) + the weak spot from the robustness check.
- **Next concrete step**: where to buy / what to book / whom to message, with a link and today's price.
- **Revisit condition**: "right if <observable> by <when>; revisit if <new fact>" (price drops below N, a new revision ships, unused for 2 weeks → return it).
- **Status**: `decided`, or `decided — check before <step>` (only for the zones in "Limits of autonomy").

Compact block for low-cost Type 2:

> **Go with:** <option> · <type> · Type 2
> **Why:** <1–2 sentences + support>
> **Trade-off:** <…> · **Revisit if:** <…> · **Next step:** <link / action>

**Tie-break**, in order, until one option wins: safer → more reversible (better return policy, more liquid on the second-hand market) → cheaper to own → simpler in daily use → closer to what the person has previously said they want.

For filled-in examples of both forms, read `references/worked-examples.md` the first time you use this skill in a conversation, or whenever unsure how detailed the answer should be.

### Step 8: Rhythm and corrections

`--one`: after each question, a compact block, then **stop**. A correction from the user ("no, weight doesn't matter to me") becomes a hard constraint for the following questions.
`--all`: all questions in sequence; in the chat, a summary table (question / decision / type / confidence / next step) plus a separate list of those with `medium` confidence or a "check before".

### Step 9: Save (if useful)

For Type 1, or a large set of decisions (fitting out a flat, planning a trip), offer in one line to save a decision log wherever the user keeps notes or tasks, with the next step and the revisit date. Create nothing without a yes. For small choices, the answer in the chat is the result.

### Step 10: Revisit

When a revisit condition fires or a new fact appears, **don't rewrite** the old decision after the fact. Make a new one that links to the previous one, with one line on "what changed". That shows the earlier decision was reasonable on the data it had, rather than "I was wrong".

## Never

- Build a decision on an unchecked fact when a search could check it.
- Quote prices, availability or rules from memory without a fresh check.
- Decide type A by taste, or treat type C/D research as law.
- Pick criteria after an attractive option is already visible.
- Present a matrix score as the verdict. The score is structure; the decision is an argument.
- Give a two-branch answer ("if you want X, then…") as final. Name the sensitive weight, but give one answer.
- Stretch a low-cost Type 2 into a long analysis. That is the same indecision, just with tables.
- Quietly swap the question for an easier one ("what's cheapest" instead of "what will suit me").

## When this skill doesn't fit

- **Type F**: a crisis now (health, safety, legal threat). Professional or emergency services first.
- **Emotional and relationship decisions** (a breakup, a conflict with someone close): this isn't choosing between options, it's a conversation. Help the person sort out their feelings, not build a matrix.
- **Options still equal after tie-break and debiasing**: say so ("both are good; the difference is smaller than the cost of thinking about it more"), pick by the last tie-break, and close the question.

## Language

Reply in the user's language. Keep prices in their currency and sources from their market.
