import json
import requests
from pathlib import Path

def	get_json_data_with_url(url: str) -> dict:
	content = None
	response = requests.get(url)
	if response.status_code == 200:
		content = response.content
	if content:
		data = json.loads(content)
		return data
	else:
		print(f"get_json_data_with_url failed with url={url}")
		return None

def	get_json_data_with_path(path: str) -> dict:
	with open(path, 'r', encoding="utf-8") as file:
		content = file.read()
	if content:
		data = json.loads(content)
		return data
	else:
		print(f"get_json_data_with_path failed with path={path}")
		return None

def	write_json_in_copy(json_path: str, data: dict):
	parent_dir = Path(json_path).parent
	copy_name = f"{Path(json_path).stem}_copy{Path(json_path).suffix}"
	copy_path = parent_dir.joinpath(copy_name)
	with open(copy_path, 'w', encoding = "utf-8") as f:
		json.dump(data, f, ensure_ascii = False, indent = 4)

def	get_reordered_keys(parent_key: dict, child_keys: list) -> dict:
	if not isinstance(parent_key, dict) or not isinstance(child_keys, list):
		raise TypeError()
	i = 0
	while i < len(child_keys):
		key_exist = False
		for key in parent_key.keys():
			if child_keys[i] == key:
				key_exist = True
		if not key_exist:
			del child_keys[i]
		else:
			i += 1
	# remove every junk keys (lol)
	new_parent_key = {}
	child_keys_incr = 0
	for key in parent_key.keys():
		keymatch = False
		for child_key in child_keys:
			if key == child_key:
				new_key = child_keys[child_keys_incr]
				new_parent_key[new_key] = parent_key[new_key]
				child_keys_incr += 1
				keymatch = True
				# if any key match with a child, take a child and increment
		if not keymatch:
			new_parent_key[key] = parent_key[key]
	return new_parent_key

def put_key_at_position(parent_key: dict, new_key: str, value, pos: int) \
		-> dict:
	new_parent_key = {}
	key_added = False
	for i, key in enumerate(parent_key.keys()):
		if i == pos:
			new_parent_key[new_key] = value
			key_added = True
		new_parent_key[key] = parent_key[key]
	if not key_added and len(parent_key.keys()) > 0:
		new_parent_key[new_key] = value
	return new_parent_key
