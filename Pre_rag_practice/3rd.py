from collections import Counter


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



print(inverted_index)