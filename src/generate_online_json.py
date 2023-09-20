import json
from pathlib import Path

from core.settings import DATA_URL, CATEGORYS, DATA_PATH
from core.tools.json_tools import get_json_data_with_url
from core.tools.tools import mkdir
from core.data_version import get_version

def	generate_online_json():
	version = get_version()
	path = f"{DATA_PATH}/imported/{version}"
	mkdir(path)
	i = 0
	while i < len(CATEGORYS):
		if Path(f"{path}/{CATEGORYS[i]}.json").exists():
			i += 1
			continue
		url = DATA_URL.replace("<version>", version) \
				.replace("<category>", CATEGORYS[i])
		data = get_json_data_with_url(url)
		if data:
			with open(f"{path}/{CATEGORYS[i]}.json", "w", encoding="utf-8") \
					as imported_json:
				json.dump(data, imported_json, ensure_ascii = False, indent = 4)
			print(f"{path}/{CATEGORYS[i]}.json written")
		i += 1

if __name__ == "__main__":
	generate_online_json()
