import json

from settings import DATA_URL, CATEGORYS, VERSION_URL
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
	path = f"./data/imported/{version}"
	tools.mkdir(path)
	i = 0
	while i < len(CATEGORYS):
		if tools.does_path_exist(f"{path}/{CATEGORYS[i]}.json"):
			continue
		url = DATA_URL.replace("<version>", version) \
				.replace("<category>", CATEGORYS[i])
		data = json_tools.get_json_data_with_url(url)
		if data:
			with open(f"{path}/{CATEGORYS[i]}.json", "w", encoding="utf-8") \
					as imported_json:
				json.dump(data, imported_json)
			print(f"{path}/{CATEGORYS[i]}.json written")
		i += 1

