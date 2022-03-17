import json


def create_json_file(payload):
    with open("token.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=4)