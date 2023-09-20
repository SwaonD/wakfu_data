import sys
from varname import nameof

from settings import *
from import_online_data import import_online_data, wakfu_version

def print_json_links():
	version = wakfu_version()
	i = 0
	while i < len(CATEGORYS):
		url = DATA_URL.replace("<version>", version) \
				.replace("<category>", CATEGORYS[i])
		print(url)
		i += 1

def main(argv):
	if (len(argv) >= 2) and argv[1] == nameof(print_json_links):
		print(f"{nameof(print_json_links)} …")
		print_json_links()
	else:
		print(f"{nameof(import_online_data)} …")
		import_online_data()

if __name__ == "__main__":
	main(sys.argv)
