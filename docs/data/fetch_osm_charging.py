"""Fetch OSM amenity=parking in a Phnom Penh bbox via Overpass; retries across mirrors."""
import json, sys, time, urllib.request, urllib.parse

MIRRORS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]
Q = '[out:json][timeout:90];nwr["amenity"="charging_station"](10.3,102.3,14.7,107.7);out tags center;'
UA = "CamGarage-research/0.1 (chanheng.sng3@gmail.com)"

for attempt in range(8):
    for m in MIRRORS:
        try:
            req = urllib.request.Request(
                m,
                data=urllib.parse.urlencode({"data": Q}).encode(),
                headers={"User-Agent": UA, "Accept": "application/json"},
            )
            d = json.loads(urllib.request.urlopen(req, timeout=120).read())
            json.dump(d, open("osm_cambodia_charging.json", "w"))
            print("ok", m, len(d["elements"]))
            sys.exit(0)
        except Exception as e:
            print("fail", m, str(e)[:80], flush=True)
    time.sleep(20 * (attempt + 1))
sys.exit(1)
