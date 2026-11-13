# 01. Cambodia market research

## Vehicle growth

- **[verified]** Cambodia registered **413,067 vehicles in 2024**: 353,603 motorcycles, 54,692 family and tourist vehicles, 5,841 heavy vehicles. Source: MPWT spokesperson via Cambodia's Ministry of Information (AKP), 15 Jan 2025. https://www.information.gov.kh/articles/149337 (the search snippet showed these numbers; the page body did not load for me).
- So cars are about **13%** of new registrations and motorcycles about **86%**. **[derived]**
- **[assumption]** Most of the parking pain is motorcycle and car parking in central Phnom Penh. Motorcycles are the bulk of vehicles, but cars take the most space per vehicle and are likelier to need paid parking. The app should support both types, with car first for garages. This needs validating.
- More data: Cambodia Automotive Association registration page, https://cambodia-automotive.org/industry/vehicles-registration-statistic/ (not yet read).

## Pain points

- **[verified, headline only]** Illegal parking on roads, sidewalks and at markets is a known problem. Police crackdowns are reported (Khmer Times). Kiripost reports the city proposing fines for sidewalk obstruction. A June 2025 opinion piece calls for towing and fines, on the view that drivers use sidewalks for parking. Search snippets only. Full articles blocked or empty for me.
- **[verified, headline only]** A student mini-research paper says illegal roadside parking comes from **a lack of parking facilities and weak enforcement** (Scribd, "Illegal Parking Issues in Phnom Penh").
- **[verified, secondary source]** A travel-guide site says paid on-street areas are marked with blue lines or signs, at roughly **1,000 to 5,000 KHR/hour (about $0.25 to $1.25)**, and that malls, hotels and restaurants run private parking. This is a low-quality source. Treat the figures as a rough range only.
- **[assumption]** Drivers' real problems are: not knowing whether a lot has space, not knowing the price before arriving, fear of fines or towing, and fear of theft or damage. Interview 10 to 20 drivers to confirm.

## Smart parking market

- **[source-claim]** 6Wresearch projects the Cambodian smart parking market to grow at **17.8% CAGR 2025 to 2031**, with ultrasonic sensors, guided parking and security/surveillance as the dominant segments. It also names weak awareness, high upfront cost for small operators and patchy digital infrastructure as barriers. Market-research vendor, no methodology visible. Do not quote the figure as fact.
- 6Wresearch names Parkopedia and EasyPark as active, and Paragon Parking, Mekong Smart Tech and Smart City Solutions Asia as players. **[source-claim, unchecked]**. I found no evidence of Parkopedia or EasyPark operating a real Cambodian service.

## Payments

- **[verified]** **KHQR** is the national QR payment standard of the National Bank of Cambodia. It works across banks and wallets in KHR and USD. ABA publishes a KHQR developer guideline (https://developer.payway.com.kh/khqr-guideline-3192101f0). Cambodia has cross-border QR links, for example Singapore (Mar 2026 article).
- **[assumption]** Any online payment feature should use KHQR first, since every user's bank app can scan it. Card payments are less important here.

## Other cities

- Siem Reap (tourists, hotels, Angkor) and Sihanoukville: **no research done**, search failed. See open questions.

## Round 2 additions

### Phnom Penh parking supply and demand (JICA, Data Collection Survey on Urban Transport in Phnom Penh, Final Report)
Source: https://openjicareport.jica.go.jp/pdf/12371746_01.pdf. Extracted parking pages are in `data/jica_parking_pages.txt`.

- **[source-claim]** In the CBD, parking **demand exceeds capacity** (off-street plus on-street). Survey covered 17 parking facilities and 38 on-street sections. Legal parking capacity in Blocks A to E is 5,705 PCU (read from chart label).
- **[source-claim]** Demand is high in daytime and drops at night.
- **[source-claim]** Why drivers park illegally on the street: 36% say it is hard to find a free space, 19% parking fees, 17% assume no crackdown risk, 12% no lot near the destination. The report concludes parking information is also needed. This supports a directory with availability.
- **[source-claim]** 71% disagree that the current illegal parking situation is acceptable, and 90% agree illegal parking should be strictly controlled.
- **[source-claim]** If a 25,000 KHR fine were enforced, 66% would still drive to the CBD; of those, 98% would use the closest paid facility. Over half of those who would stop driving cite high fees and lack of lots.
- **[source-claim]** Share of parked users walking under 50 m to the destination: 61% (2012), 45% (2022). People walk further now, so "near the destination" is getting harder.
- **[source-claim]** Car mode share rose from 9.9% (2012) to 14.9% (2022), projected 20-22% by 2035.
- **[source-claim]** The inventory survey records name, floor area, hours, capacity and fee per facility. The exact tables are in figures I could not extract; read the PDF pages 5-35 to 5-38 by hand.

### Regulation
- **[source-claim]** The JICA report says on-street parking has no clear legal definition of legal/illegal; the survey had to invent one. MPWT, with JICA support, was drafting a **parking law** (bill planned by June 2023) covering parking management areas, on-street and setback parking, off-street parking, mandatory building parking, fees and penalties. **Status unknown**; check whether it passed.
- **[source-claim]** History: Phnom Penh Post 2009 quotes a deputy governor saying there were no rules on on-street parking. In 2010 a one-week pilot on Charles de Gaulle Blvd (120 m, Streets 107-109) gave 1 hour free, then 500 to 20,000 riel; shop owners complained. https://www.phnompenhpost.com/national/parking-fees-spark-complaints/ Old and may be outdated.
- **[assumption]** Informal street and sidewalk parking is still common and fees are set by whoever runs the spot.
