import json
import requests

def get_json_data_with_url(url):
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

def	get_json_data_with_path(path, mode = "r"):
	with open(path, mode, encoding="utf-8") as file:
		content = file.read()
	if content:
		data = json.loads(content)
		return data
	else:
		print(f"get_json_data_with_path failed with path={path}")
		return None

# create function to place any key to any position in the object
