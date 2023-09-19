import json
import requests

def get_json_data_with_url(url):
	content = None
	response = requests.get(url)
	if response.status_code == 200:
		content = response.text # pb utf 8 ici
	if content:
		data = json.loads(content)
		return data
	else:
		print(f"get_json_data_with_url failed with url={url}")
		return None

def	get_json_data_with_path(path):
	with open(path, 'r', encoding="utf-8") as file:
		content = file.read()
	if content:
		data = json.loads(content)
		return data
	else:
		print(f"get_json_data_with_path failed with path={path}")
		return None
