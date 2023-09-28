import json
from pathlib import Path

from core.settings import DATA_URL, CATEGORYS, DATA_PATH, JSON_SUFFIX
from core.tools.json_tools import get_json_data_with_url
from core.data_version import get_version

def	generate_online_json():
	version = get_version()
	path: Path = DATA_PATH / "imported" / version
	if not path.exists():
		path.mkdir(parents = True)
	i = 0
	while i < len(CATEGORYS):
		file = path / (CATEGORYS[i] + JSON_SUFFIX)
		if file.exists():
			i += 1
			continue
		url = DATA_URL.replace("<version>", version) \
				.replace("<category>", CATEGORYS[i])
		data = get_json_data_with_url(url)
		if data:
			with open(file, "w", encoding="utf-8") as imported_json:
				json.dump(data, imported_json, ensure_ascii = False, indent = 4)
			print(f"{file.name} written in {path.parents[1].name}/" \
					f"{path.parents[0].name}/{path.name}")
		i += 1

if __name__ == "__main__":
	generate_online_json()
