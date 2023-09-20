from settings import VERSION_URL
from tools.json_tools import get_json_data_with_url

def get_version():
	data = get_json_data_with_url(VERSION_URL)
	if data:
		return data["version"]
	else:
		return None
