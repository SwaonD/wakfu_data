import json
from pathlib import Path

from settings import DATA_URL, CATEGORYS, VERSION_URL, DATA_PATH
import json_tools
import tools

def wakfu_version():
	data = json_tools.get_json_data_with_url(VERSION_URL)
	if data:
		return data["version"]
	else:
		return None

def	import_online_data():
	version = wakfu_version()
	path = f"{DATA_PATH}/imported/{version}"
	tools.mkdir(path)
	i = 0
	while i < len(CATEGORYS):
		if Path(f"{path}/{CATEGORYS[i]}.json").exists():
			i += 1
			continue
		url = DATA_URL.replace("<version>", version) \
				.replace("<category>", CATEGORYS[i])
		data = json_tools.get_json_data_with_url(url)
		if data:
			with open(f"{path}/{CATEGORYS[i]}.json", "w", encoding="utf-8") \
					as imported_json:
				json.dump(data, imported_json, ensure_ascii = False, indent = 4)
			print(f"{path}/{CATEGORYS[i]}.json written")
		i += 1

