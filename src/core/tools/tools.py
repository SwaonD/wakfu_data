from pathlib import Path

def mkdir(path: str):
	path_object = Path(path)
	if not path_object.exists():
		path_object.mkdir(parents=True, exist_ok=True)
		print(f"folder '{path}' created successfully")
	else:
		print(f"folder '{path}' already exist")
