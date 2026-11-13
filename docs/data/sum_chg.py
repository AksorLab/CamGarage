import json,collections
d=json.load(open("osm_cambodia_charging.json"))["elements"]
print(len(d))
for k in ["operator","brand","socket:type2","socket:ccs","socket:gb_dc","opening_hours","fee","capacity"]:
    print(k,sum(1 for e in d if k in e.get("tags",{})))
print(collections.Counter(e["tags"].get("operator") or e["tags"].get("brand") or e["tags"].get("name") for e in d).most_common(12))
