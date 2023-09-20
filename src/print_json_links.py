from core.settings import DATA_URL, CATEGORYS
from core.data_version import get_version

def print_json_links():
	version = get_version()
	i = 0
	while i < len(CATEGORYS):
		url = DATA_URL.replace("<version>", version) \
				.replace("<category>", CATEGORYS[i])
		print(url)
		i += 1

if __name__ == "__main__":
	print_json_links()
