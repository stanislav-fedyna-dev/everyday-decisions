# Worked examples

These show the expected **shape and depth** of an answer. Products, prices and sources are illustrative placeholders. In a real answer, every price and spec comes from a fresh search in the user's market, with the date checked.

---

## 1. Compact block: low-cost Type 2

**User:** "Running shoes: brand A's daily trainer or brand B's? I run 3× a week, ~25 km total, mostly asphalt. Just tell me."

Silent work: reframed as "pick a daily trainer for ~25 km/week on asphalt, within ~<budget>". Type B, Type 2 (both stores offer 30-day returns on unworn or lightly worn pairs). Disconfirming search: "<model B> durability problems" turned up repeated reports of outsole wear around 300 km.

> **Go with:** Brand A daily trainer · B (trade-off) · Type 2
> **Why:** Same cushioning class; A's outsole lasts noticeably longer in owner reports (`moderate`: large volume of reviews), and you run on asphalt, where wear is what you'll notice. A is also <X> cheaper today at <store>.
> **Trade-off:** A is ~20 g heavier per shoe. · **Revisit if:** heel or arch discomfort after the first 3 runs → return within the 30-day window. · **Next step:** <store link>, <price>, checked <date>.

---

## 2. Full write-up: Type 1 with a "check before"

**User:** "Should I buy a used car or keep using public transport + taxis? I live in the city, drive to the mountains about once a month."

Context gathered: budget ceiling mentioned earlier in the chat; no parking at home (assumption, flagged).

**Decision:** Don't buy a car now. Use public transport for the city and rent a car for the monthly mountain trips.

**Y-statement:** In the context of city living with one mountain trip a month, to get flexible weekends without a fixed monthly cost, I choose transit + monthly rental over buying a used car, accepting the hassle of booking a rental and occasionally paying peak-weekend rates.

**Classification:** B with an E component (how much independence is worth) · buying is Type 1 (resale loss + time) · cost of error: high.

**Why:**
- Total cost of ownership for a used car in budget (insurance + maintenance + parking + depreciation) is about <N>/month at today's local rates; 12 weekend rentals + taxis come to about <M>/month (`moderate`: computed from current listings, checked <date>).
- Usage is the sensitive parameter: the car would sit idle ~25 days a month.
- Outside view: first-car owners routinely underestimate maintenance and parking (`consensus`).

**Rejected:**
- Used car: highest monthly cost at this usage, and an expensive rollback.
- Car-sharing only: not available for multi-day mountain trips in your city.
- Status quo (transit + taxis only): mountain trips become impractical, which is the actual problem.

**Confidence:** medium. Weak spot: if mountain trips become weekly, or you start commuting outside the city, buying wins.

**Next step:** Book next month's trip with <rental company>, <price> for a weekend, checked <date>.

**Revisit condition:** Right if you take ≥10 mountain trips over the next year without rental friction stopping you. Revisit if trips go above 3 a month or you move somewhere without good transit.

**Status:** decided. (If you later decide to buy, the status becomes "decided — check before paying": independent pre-purchase inspection first.)

---

## 3. Type A: looked up, not decided

**User:** "Can I take my power bank on the plane? It's 26,800 mAh."

Not a judgment call: the carrier's and aviation authority's current rules answer it.

> **Answer:** Convert to Wh (26.8 Ah × 3.7 V ≈ 99 Wh). It falls under the threshold most carriers allow in **carry-on only**, never checked luggage. Confirm on <airline>'s current dangerous-goods page (`strong`: primary source, checked <date>), since some carriers set their own lower limits.

---

## 4. `--all` summary table

**User:** "Fitting out the new kitchen: kettle, toaster, and do I need a microwave? `--all`"

| Question | Decision | Type | Confidence | Next step |
|---|---|---|---|---|
| Kettle | <model>, 1.7 L, auto-off | B · Type 2 | high | <store>, <price> |
| Toaster | Don't buy; use the oven's grill for now | B/D · Type 2 | medium | revisit after 1 month |
| Microwave | Yes, basic solo model | C · Type 2 | high | <store>, <price> |

**Needs attention:** Toaster (medium): depends on how often you actually make toast. Revisit if you use the grill for toast more than twice a week.
