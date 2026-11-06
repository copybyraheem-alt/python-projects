chunks={
    "Transport, motorways, and tramlines",
    "Starting and then stopping, taking off and landing",
    "The emptiest of feelings, disappointed people",
    "Clinging onto bottles, when it comes, it's so, so disappointing",
    "Let down and hanging around",
    "Crushed like a bug in the ground",
    "Let down and hanging around"
}


inverted_index={}

for chunk_id, chunk in enumerate(chunks):
    words=chunk.lower().split()
    for word in words:
        if word not in inverted_index:
            inverted_index[word]=[]

        if chunk_id not in inverted_index[word]:
            inverted_index[word].append(chunk_id)





print(inverted_index)
 