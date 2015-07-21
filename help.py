import sys
import json

with open("/tmp/pgdump", "r") as f:
    data = json.load(f)
osd_stats = data["osd_stats"]
key = sys.argv[1]
res = ""
if key != "kb_used":
    for item in osd_stats:
        res += ("osd{0}: {1} ".format(item["osd"], item["fs_perf_stat"][key]))
else:
    for item in osd_stats:
        res += ("osd{0}: {1} ".format(item["osd"], item[key]))
print res
