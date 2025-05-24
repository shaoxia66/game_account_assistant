import json

raw_json='[{"name": "deal_record", "arguments": {"p": {"keywords": ["段位】铂金"]}}]'
print(raw_json[:-1]+"}]")
json_obj = json.loads(raw_json[:-1]+"}]")
print(json_obj)
# tool_call = json.loads(json_obj)