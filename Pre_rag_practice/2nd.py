from langchain_text_splitters import RecursiveCharacterTextSplitter

text = open("let_down.txt", "r").read()
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=25, separators=[" ", ""])
chunks = splitter.split_text(text)
all_chunks=[]


for i, chunk in enumerate(chunks):
        chunk_data= {
                
                "chunk_id": i,
                 "text": chunk,
                 "sourse": "let_down.txt",
                 "chunk_index": 1
        }

        all_chunks.append(chunk_data)

print(all_chunks)



