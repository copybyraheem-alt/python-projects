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


query = input("Search for a word: ").lower()
matching_chunks = inverted_index.get(query, {})


for chunk_id in matching_chunks:
    total_words= len(chunks[chunk_id].split())
    tf= freq / total_words

    idf= math.log(len(chunks)/ len(matching_chunks))
    score=tf*idf
    print(chunks[chunk_id], score)


