# import json
# # import tiktoken

# with open("longbench.json", "r", encoding="utf-8") as f:
#     longbench = json.load(f)

# for i, data in enumerate(longbench):
#     print(f"({i}) {data["question"]} ({data["difficulty"]} {data["length"]})")

import numpy as np
from sklearn.cluster import DBSCAN
from sentence_transformers import SentenceTransformer

# phrase_list = [ 'play an active role', 'participate actively', 'active lifestyle', "sleep in a bed"]

# model = SentenceTransformer('whaleloops/phrase-bert')
# phrase_embs = model.encode( phrase_list )
# [p1, p2, p3, p4] = phrase_embs

# for phrase, embedding in zip(phrase_list, phrase_embs):
#     print("Phrase:", phrase)
#     print("Embedding:", len(embedding))
#     print("")
