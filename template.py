import json
import os
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template")
cache = {}

def FORMAT_JSON(func):
    """
    JSON 파일을 로드하여 반환하는 함수의 데코레이터
    """
    def wrapper(file_name, *args, **kwargs):
        file_name = file_name if file_name.endswith(".json") else file_name + ".json"
        return func(file_name, *args, **kwargs)
    return wrapper

def get_all_source():
    """
    템플릿 디렉토리에 있는 모든 JSON 파일 이름을 반환
    """
    return [os.path.splitext(f)[0] for f in os.listdir(base_dir) if f.endswith(".json")]

@FORMAT_JSON
def load_file(file_name):
    """
    JSON 파일을 로드하여 반환
    """

    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

@FORMAT_JSON
def getKeys(file_name):
    """
    파일이름 file_name에 해당하는 JSON 파일의 모든 키를 반환
    파일이 캐시되어 있지 않으면 로드하고 캐시함
    """
    if file_name not in cache:
        try:
            cache[file_name] = load_file(file_name)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_name}' not found in directory '{base_dir}'.")
        except json.JSONDecodeError:
            raise ValueError(f"File '{file_name}' is not a valid JSON file.")
    return list(cache[file_name].keys())

@FORMAT_JSON
def getData(file_name, key):
    """
    파일이름과 키를 받아서 해당 키의 값을 반환
    파일이 캐시되어 있지 않으면 로드하고 캐시함
    """
    if file_name not in cache:
        try:
            cache[file_name] = load_file(file_name)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_name}' not found in directory '{base_dir}'.")
        except json.JSONDecodeError:
            raise ValueError(f"File '{file_name}' is not a valid JSON file.")

    if key in cache[file_name]:
        return cache[file_name][key]
    else:
        raise KeyError(f"Key '{key}' not found in file '{file_name}'.")