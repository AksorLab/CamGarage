# 03. Data sources

## OpenStreetMap (checked, with a real pull)

I queried Overpass for `amenity=parking` in a Phnom Penh bounding box (lat 11.45 to 11.68, lon 104.80 to 105.00). Raw output: `data/osm_phnom_penh_parking.json`. Re-run with `python3 data/fetch_osm.py`.

**Result: 265 features, and the tagging is very thin.**

- 214 of 265 have no `parking=` type. Where set: 26 surface, 11 underground, 6 multi-storey, 3 street_side, 2 garage, 1 each of garage_boxes, rooftop, lane.
- `fee`: yes 16, no 7, **unset 242**.
- `access`: customers 12, private 11, yes 7, permit 1, unset 234.
- Only **10 have a name**, **4 a capacity**, **6 an operator**, **1 a website**.
- **0 have `opening_hours`**, **0 have a `charge`**, **0 have a phone number**.
- The bounding box is a rough rectangle, so it may include a few features outside the city. Not de-duplicated.

**Conclusion:** OSM gives us locations and a rough lot shape, but **hours, price, services and categories, which are the app's core content, are essentially absent**. We will have to collect that ourselves. OSM is still useful as a seed list of locations, and we can upload our data back to it.

## Other candidate sources (not yet checked)

- **Google Places API.** Good coverage of malls and hotels. Paid, with terms that restrict caching and storing the data. Check the terms before relying on it. **[assumption]**
- **Operator websites and pages**: mall fee tables (AEON etc.), hotels, condos, hospitals, airport (PNH). Manually collected, each needing a licence to reuse. **[assumption]**
- **Facebook pages and Telegram groups** of private garages and condo parking. **[assumption]** Probably where small operators advertise monthly rates. Not scraped, and scraping may breach terms.
- **Government**: MPWT and Phnom Penh Capital Administration for official on-street zones and rates. Nothing structured found. JICA's *Data Collection Survey on Urban Transport in Phnom Penh* (https://openjicareport.jica.go.jp/pdf/12371746_01.pdf) has a parking chapter. **Not yet read**; it could give surveyed supply and demand.
- **National Institute of Statistics** (https://nis.gov.kh/en/official-statistics-of-cambodia/): official statistics portal.
- **Crowdsourcing** by users and by the team walking the city. Likely the main source. **[assumption]**

## Takeaway

Plan on building the listing dataset ourselves, with owner self-service and community edits on top of an OSM seed.
