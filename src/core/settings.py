from pathlib import Path

FOLDER_ABS_PATH = Path(__file__).resolve().parents[2]
DATA_PATH = FOLDER_ABS_PATH / "data"
CUSTOM_DATA_PATH = DATA_PATH / "custom"
DATA_URL = "https://wakfu.cdn.ankama.com/gamedata/<version>/<category>.json"
VERSION_URL = "https://wakfu.cdn.ankama.com/gamedata/config.json"
CATEGORYS = [
	"actions", "blueprints", "collectibleResources", "equipmentItemTypes",
	"harvestLoots", "itemTypes", "itemProperties", "items", "jobsItems",
	"recipeCategories", "recipeIngredients", "recipeResults", "recipes",
	"resourceTypes", "resources", "states"
]
