# replace id with name to make json readable
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.tools.json_tools import get_json_data_with_path, write_json_in_copy, \
		put_key_at_position
from core.settings import CUSTOM_DATA_PATH, JSON_SUFFIX

dir_name = "readable"

def	to_readable():
	dir = CUSTOM_DATA_PATH / dir_name
	dir.mkdir()
	for file in CUSTOM_DATA_PATH.iterdir():
		file = Path(CUSTOM_DATA_PATH / file)
		if file.is_file() and file.suffix == JSON_SUFFIX:
			data = get_json_data_with_path(file)
