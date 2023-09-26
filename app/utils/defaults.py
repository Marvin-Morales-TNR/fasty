import os, json, hashlib

root_route = os.path.dirname(os.path.abspath("main.py"))
config_file_route = os.path.join(root_route, "config", "config.json ")

def config_file_caller() -> dict:
   with open(config_file_route, "r") as config_file:
      config_data = json.load(config_file)
   return config_data

def create_sha256_hash(text: str) -> str:
   hash_obj = hashlib.sha256()
   hash_obj.update(text.encode('utf-8'))
   return hash_obj.hexdigest()