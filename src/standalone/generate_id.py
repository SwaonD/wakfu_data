import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.settings import CUSTOM_DATA_PATH, COPY_ADD, JSON_SUFFIX
from core.tools.json_tools import get_json_data_with_path, write_json_in_copy, \
		put_key_at_position

ID_FILE_NAME = "current_id"
ID_FILE = Path(__file__).resolve().parent / f"{ID_FILE_NAME}.json"
FIRST_ID = 10000000

def generate_id(file: Path, is_overwrite: bool):
	"""
	Generate ids in a new wakfu custom json file
	"""
	data = get_json_data_with_path(file)
	json_id_data = get_json_data_with_path(ID_FILE)
	id = json_id_data["id"]
	unused_ids = check_for_unused_id(FIRST_ID, id)
	if is_overwrite:
		unused_ids.extend(get_id(data))
	nb_id_added = 0
	i = 0
	while i < len(data):
		if ("definition" in data[i] and "id" in data[i]["definition"] \
				or "id" in data[i]) and not is_overwrite:
			i += 1
			continue
		if len(unused_ids) > 0:
			new_id =  unused_ids.pop(0)
		else:
			new_id = id
		if "definition" in data[i]:
			data[i]["definition"] = put_key_at_position( \
					data[i]["definition"], "id", new_id, 0)
		elif "title" in data[i]:
			data[i] = put_key_at_position( \
					data[i], "definition", {"id": new_id}, 0)
		else:
			data[i] = put_key_at_position(data[i], "id", new_id, 0)
		if len(unused_ids) == 0:
			id += 1
			# increase id only if there is no more unuesed id
		nb_id_added += 1
		i += 1
	json_id_data["id"] = id
	write_json_in_copy(file, data)
	write_json_in_copy(ID_FILE, json_id_data)
	print(f"{nb_id_added} ids have been added to {file.name}")


def check_for_unused_id(first_id: int, current_id: int) -> list:
	all_ids = []
	for file in CUSTOM_DATA_PATH.iterdir():
		file = Path(CUSTOM_DATA_PATH / file)
		if file.is_file() and file.suffix == JSON_SUFFIX:
			data = get_json_data_with_path(file)
			if data:
				for item in data:
					if "definition" in item and "id" in item["definition"]:
						all_ids.append(item["definition"]["id"])
					elif "id" in item:
						all_ids.append(item["id"])
	unused_ids = []
	for i in range(first_id, current_id):
		if i not in all_ids:
			unused_ids.append(i)
	if len(unused_ids) > 0:
		print(f"unused ids found : {unused_ids}")
	return unused_ids

def	get_id(data: list) -> list:
	ids = []
	for item in data:
		if "definition" in item and "id" in item["definition"]:
			ids.append(item["definition"]["id"])
		elif "id" in item:
			ids.append(item["id"])
	return ids

def	overwrite(file: Path) -> bool:
	while True:
		user_input = input(f"Overwrite every id in {file.name} ? y/n ")
		if user_input.lower() == "y":
			return True
		elif user_input.lower() == "n":
			return False
		else:
			print("Please enter 'y' to say Yes or 'n' to say No")

def get_file():
	while True:
		print(f"Make sure that your file{JSON_SUFFIX} is in {CUSTOM_DATA_PATH}")
		user_input = input(f"Please give the file name : ")
		file = Path(CUSTOM_DATA_PATH / user_input)
		if file.is_file():
			return file
		else:
			file_json = file.with_name(file.stem + JSON_SUFFIX)
			if file_json.is_file():
				return file_json
			else:
				print(f"{file} not found\n")

def replace(file: Path):
	while True:
		user_input = input(f"Write changes ? y/n ")
		if user_input.lower() == "y":
			ID_FILE.unlink()
			ID_FILE.with_name(ID_FILE_NAME + COPY_ADD + JSON_SUFFIX) \
					.rename(ID_FILE)
			file.unlink()
			file.with_name(file.stem + COPY_ADD + JSON_SUFFIX).rename(file)
			return
		elif user_input.lower() == "n":
			ID_FILE.with_name(ID_FILE_NAME + COPY_ADD + JSON_SUFFIX).unlink()
			file.with_name(file.stem + COPY_ADD + JSON_SUFFIX).unlink()
			return
		else:
			print("Please enter 'y' to say Yes or 'n' to say No")

if __name__ == "__main__":
	file = get_file()
	generate_id(file, overwrite(file))
	replace(file)
