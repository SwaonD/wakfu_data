import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.tools.json_tools import get_json_data_with_path, write_json_in_copy, \
		put_key_at_position, get_reordered_keys
from core.settings import CUSTOM_DATA_PATH


zones_file = CUSTOM_DATA_PATH / "zones.json"
zones_data = get_json_data_with_path(zones_file)
zoneNames_file = CUSTOM_DATA_PATH / "zoneNames.json"
zoneNames_data = get_json_data_with_path(zoneNames_file)
i = 0
while i < len(zones_data):
	for zoneName in zoneNames_data:
		if zones_data[i]["zoneName"] == zoneName["definition"]["id"]:
			zones_data[i]["zoneName"] = zoneName["title"]["fr"]
	i += 1
# edit data here
write_json_in_copy(zones_file, zones_data)
