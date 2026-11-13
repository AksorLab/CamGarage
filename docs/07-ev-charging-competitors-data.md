# 07 - EV charging: competitors and data sources (round 3b)

Tags: [verified] / [source-claim] / [assumption] as before.

## Key finding: the charger map already exists
1. **UnifyCharge** - national app built by MME + EDC + EAC (operator: OneGo, Play id `asia.onego.ev`). Shows stations, real-time availability, tariffs, starts/monitors charging, pays in Riel. Counted 460 charging machines on 15 Sep 2026 (each station has at least 2). [verified] (Cambodianess, Play Store, App Store, unifycharge.com.kh)
   - It is government-backed and consolidates the public chargers. Competing head-on on a charger map plus payment is a bad bet. [assumption]
2. **Fresh AI "EV Zone"** (Feb 2026): maps 200+ stations nationwide with power, connector (CCS2/GBT), payment app, hours; links to Google Maps. Free. [source-claim] (Cambodge Mag)
3. Kiripost map of 104 stations (84 open 24h), older. [source-claim] (page content did not load)
4. Operators seen: EDC, CHARGE+ (target 4,000 points by 2030), BYD (18 flash-charging stations by end 2026 in Phnom Penh, Siem Reap, Sihanoukville; Cambodia first outside China), VinFast (appears in OSM). [source-claim]

## Open data
- OSM `amenity=charging_station`, bbox of Cambodia (rough box, includes parts of Thailand/Vietnam): 53 elements. Operator or brand on about 35, opening_hours on 3, fee on 6, no socket tags at all. Mostly VinFast (a Vietnam-side result). [verified] (`data/osm_cambodia_charging.json`, `fetch_osm_charging.py`, `sum_chg.py`)
- So OSM is useless for Cambodian chargers. Data must come from operators, UnifyCharge or our own survey. Whether UnifyCharge has an API or partner access: unknown.

## What this means for strategy
- Chargers are being mapped by the state. Charging data is not our differentiator.
- What nobody seems to cover: **parking at/near the charger** (does the charger sit in a mall lot, hours, fee, whether a non-charging car blocks the bay, can I reserve), and trip planning that combines both. [assumption: not verified in apps]
- Best fit is a partner or integration rather than competitor: ask UnifyCharge/OneGo for data access, and let CamGarage own parking data, with chargers as a layer on top.
- Revenue idea stays: mall and parking-lot owners pay for traffic or reservations; chargers are the draw.

## Next steps
- Install and inspect UnifyCharge (I can't run an Android app here; someone on the team should screenshot stations, filter options and whether parking info exists).
- Contact OneGo / MME about a data API or partnership.
- Check EVCambodia and CHARGE+ locations and whether they are listed in UnifyCharge.
- Survey 10-20 chargers in Phnom Penh for parking conditions (fee, hours, blocked bays).
