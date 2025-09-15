import json
# import tiktoken

with open("longbench.json", "r", encoding="utf-8") as f:
    longbench = json.load(f)

for i, data in enumerate(longbench):
    print(f"({i}) {data["question"]} ({data["difficulty"]} {data["length"]})")

