import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.tools.json_tools import get_json_data_with_path, write_json_in_copy, \
		put_key_at_position, get_reordered_keys
from core.settings import CUSTOM_DATA_PATH


zoneNames_file = CUSTOM_DATA_PATH / "zoneNames.json"
zoneNames_data = get_json_data_with_path(zoneNames_file)
# edit data here
i = 0
while i < len(zoneNames_data):
	y = 0
	while y < len(zoneNames_data):
		if y == i:
			y += 1
			continue
		if zoneNames_data[i]["title"]["fr"] == zoneNames_data[y]["title"]["fr"]:
			print(f'{zoneNames_data[i]["title"]["fr"]} en double')
		y += 1
	i += 1
# edit data here
# write_json_in_copy(zones_file, zones_data)
