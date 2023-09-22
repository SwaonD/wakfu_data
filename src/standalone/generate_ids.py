import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.settings import CUSTOM_DATA_PATH
from core.tools.json_tools import get_json_data_with_path, write_json_in_copy, \
		put_key_at_position

ID_PATH = "current_id.json"

def generate_ids(file_name):
	"""
	Generate ids in a new wakfu custom json file
	"""
	file_path = CUSTOM_DATA_PATH / file_name
	data = get_json_data_with_path(file_path)
	json_id_data = get_json_data_with_path(ID_PATH)
	id = json_id_data["id"]
	i = 0
	while i < len(data):
		if "definition" in data[i]:
			data[i]["definition"] = \
					put_key_at_position(data[i]["definition"], "id", id, 0)

		else:
			data[i] = put_key_at_position(data[i], "definition", {"id": id}, 0)
		i += 1
		id += 1
	json_id_data["id"] = id
	write_json_in_copy(file_path, data)
	write_json_in_copy(ID_PATH, json_id_data)
# add check if any objet is deleted, use the free id



if __name__ == "__main__":
	argv = sys.argv
	if len(argv) >= 2:
		generate_ids(sys.argv[1])
