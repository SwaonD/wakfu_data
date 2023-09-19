from settings import *
import requests
import json


def wakfu_version():
	response_version = requests.get(VERSION_URL)
	if response_version.status_code == 200:
		config_json = json.loads(response_version.content)
		version = config_json["version"]
		return version
	else:
		print("Error config JSON")
		return None

def main():
	version = wakfu_version()
	url = DATA_URL.replace("<version>", version).replace("<type>", type["name"])

if __name__ == "__main__":
	main()
