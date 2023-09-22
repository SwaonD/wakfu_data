import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.settings import CUSTOM_DATA_PATH
from core.tools.json_tools import get_json_data_with_path, write_json_in_copy, \
		put_key_at_position

ID_PATH = "current_id.json"
FIRST_ID = 10000000

def generate_ids(file_name: str):
	"""
	Generate ids in a new wakfu custom json file
	"""
	file_path = CUSTOM_DATA_PATH / file_name
	data = get_json_data_with_path(file_path)
	json_id_data = get_json_data_with_path(ID_PATH)
	id = json_id_data["id"]
	unused_ids = check_for_unused_id(FIRST_ID, id)
	i = 0
	while i < len(data):
		if i < len(unused_ids):
			new_id =  unused_ids[i]
		else:
			new_id = id
		if "definition" in data[i]:
			if "id" in data[i]["definition"]:
				i += 1
				continue
			else:
				data[i]["definition"] = put_key_at_position( \
						data[i]["definition"], "id", new_id, 0)
		else:
			data[i] = put_key_at_position( \
					data[i], "definition", {"id": new_id}, 0)
		if i >= len(unused_ids):
			id += 1
		i += 1
	json_id_data["id"] = id
	write_json_in_copy(file_path, data)
	write_json_in_copy(ID_PATH, json_id_data)

def check_for_unused_id(first_id: int, current_id: int) -> list:
	all_ids = []
	for file in CUSTOM_DATA_PATH.iterdir():
		file = Path(CUSTOM_DATA_PATH / file)
		if file.is_file() and file.suffix == ".json":
			data = get_json_data_with_path(file)
			for item in data:
				if "definition" in item and "id" in item["definition"]:
					all_ids.append(item["definition"]["id"])
		print(file)
	unused_ids = []
	for i in range(first_id, current_id):
		if i not in all_ids:
			unused_ids.append(i)
	return unused_ids

if __name__ == "__main__":
	argv = sys.argv
	if len(argv) >= 2:
		generate_ids(sys.argv[1])
