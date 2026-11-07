from collections import Counter
import math

chunks=[
    "python is useful",
    "python has great name in market",
    "Machine learning uses very much of python"
]


inverted_index={}
for chunk_id, chunk in enumerate(chunks):
    words=chunk.lower().split()
    word_counts= Counter(words)
    for word, freq in word_counts.items():
        if word not in inverted_index:
            inverted_index[word]={}

        inverted_index[word][chunk_id]=freq

word=input("Search: ").lower()
total_chunks=len(chunks)
doc_freq=len(inverted_index[word])

idf= math.log(total_chunks / doc_freq)
print(idf)