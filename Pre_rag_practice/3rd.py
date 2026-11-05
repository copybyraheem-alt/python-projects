chunks = [
    "I love learning Python",
    "Python is used for AI",
    "I enjoy documentaries"
]


inverted_index = {}

for chunk_id, chunk in enumerate(chunks):
    words= chunk.lower().split()
    for word in words:
        if word not in inverted_index:
            inverted_index[word]=[]

        if chunk_id not in inverted_index[word]:
            inverted_index[word].append(chunk_id)

print(inverted_index)
