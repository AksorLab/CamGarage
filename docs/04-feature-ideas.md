# 04. Feature ideas (draft)

Built from the base idea (map plus listing details: hours, services, categories, pricing) and the research. Priorities are my proposal, **not validated**.

## MVP: directory

1. **Map with lot pins**, filter by vehicle (motorcycle / car / truck), open now, price, covered, 24h.
2. **Listing detail**: hours (including holidays and night rates), price tiers (per hour, daily cap, monthly, overnight, flat motorcycle rate), currency (**KHR and USD**), vehicle types, height limit, capacity, photos, entrance location.
3. **Categories**: mall, hotel, condo/monthly, street (marked), market, hospital, airport, event venue, open lot, garage.
4. **Services**: EV charging, car wash, valet, security/CCTV, covered, lift, women-friendly lighting, disabled bays, toilet.
5. **Khmer and English**, Khmer first. Khmer plate and address search. **[assumption]** Many users will not type in English.
6. **Navigate** (hand-off to Google Maps or Apple Maps) and **share listing** by Telegram link. **[assumption]** Telegram is a main channel in Cambodia, and we already run Telegram bots.
7. **Report a correction**, "price is wrong" or "closed" buttons. We cannot afford wrong data, since OSM has none to fall back on.

## Phase 2: trust and data freshness

8. **Last verified date** and a verified badge on every listing.
9. **Owner claim and edit** flow for lots and garages, plus a simple dashboard.
10. **Community contributions** with photos of price boards. Points or badges for contributors.
11. **Crowdsourced "is it full?"**, a busy/free report with a timestamp, rather than hardware sensors.

## Phase 3: money

12. **KHQR payment** for pre-paid hours and monthly passes, via a bank (ABA PayWay documents KHQR). Needs a bank merchant account.
13. **Reservations** for operators with a booking-friendly lot.
14. **Monthly parking marketplace** for condos and offices, where owners rent unused spaces. **[assumption]** Possibly the best business model, since monthly slots are hard to find.
15. **Promotions** such as mall validation and coupons (SuperPark has e-coupons, so a partnership may be possible).
16. **Advertising or featured listing** for lots.

## Later

- Operator integration (SuperPark/Keytop APIs) for live availability.
- Fine/tow warnings: mapped no-parking zones and common crackdown areas (news says enforcement is active). Needs data and has legal risk.
- "Where did I park?" pin and timer.
- Event mode (concerts, Water Festival, Khmer New Year) with overflow parking.
- Other cities: Siem Reap, Sihanoukville.

## Business model thoughts

- Free for drivers. Revenue from featured listings, monthly-parking commission, and later payment fees. **[assumption]**
- Operators' biggest benefit is more customers. Pitch with data on search volume once we have users.
