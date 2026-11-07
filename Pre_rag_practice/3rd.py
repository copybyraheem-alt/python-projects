from collections import Counter


chunks=[
    "Transport, motorways, and tramlines",
    "Starting and then stopping, taking off and landing",
    "The emptiest of feelings, disappointed people",
    "Clinging onto bottles, when it comes, it's so, so disappointing",
    "Let down and hanging around",
    "Crushed like a bug in the ground",
    "Let down and hanging around"
]


inverted_index={}

for chunk_id, chunk in enumerate(chunks):
    word_counter=Counter(chunk.lower().split())


    for word, freq in word_counter.items():
        if word not in inverted_index:
            inverted_index[word]={}

        inverted_index[word][chunk_id]=freq


chunk_id= 4
word="hanging"

frequency = inverted_index[word][chunk_id]
total_words = len(chunks[chunk_id].split())

tf = frequency / total_words

print(tf)









