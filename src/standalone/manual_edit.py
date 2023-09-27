import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.tools.json_tools import get_json_data_with_path, write_json_in_copy, \
		put_key_at_position
from core.settings import CUSTOM_DATA_PATH


file = CUSTOM_DATA_PATH / ""
data = get_json_data_with_path(file)
# edit data here
write_json_in_copy(file, data)
