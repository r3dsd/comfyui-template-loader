import glob
import json
import os
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template")
cache = {}

def FORMAT_JSON(func):
    """
    A decorator that ensures the file_name argument is always a JSON file
    """
    def wrapper(file_name, *args, **kwargs):
        file_name = file_name if file_name.endswith(".json") else file_name + ".json"
        return func(file_name, *args, **kwargs)
    return wrapper

def get_all_source():
    """
    return all JSON file paths in the template directory
    """
    absolute_paths = glob.glob(f"{base_dir}/**/*.json", recursive=True)
    result = [os.path.splitext(os.path.relpath(path, base_dir))[0] for path in absolute_paths]
    return result

@FORMAT_JSON
def load_file(file_name):
    """
    return the JSON file as a dictionary
    """

    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

@FORMAT_JSON
def getKeys(file_name):
    """
    return the keys of the file_name JSON file
    if the file is not cached, load and cache it
    """
    if file_name not in cache:
        try:
            cache[file_name] = load_file(file_name)
        except FileNotFoundError:
            return ['Load failed [not found]']
        except json.JSONDecodeError:
            return ['Load failed [invalid JSON]']
    return list(cache[file_name].keys())

@FORMAT_JSON
def getData(file_name, key):
    """
    return the value of the key in the file_name JSON file
    if the file is not cached, load and cache it
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