# Word-frequency counter and file search


'''

1. Be able to read the file (done)
2. Count word frequencies (done)
3. Let users search for specific words (done)

'''

from collections import Counter



try:
    def word_counter():
        with open("let_down.txt", "r")as file:
            chop= Counter(file.read().lower().split()).most_common(5)
            print(dict(chop))


    def search_engine():
        with open("let_down.txt", "r")as file:
            word=input("What would you like to search: ").lower()
            for index, line in enumerate(file.read().lower().split()):
                if word in line:
                    answer= f"line number {index+1} contains this word : {word}"
                    print(answer)

    def read():
        with open("let_down.txt", "r") as file:
            content=file.read()
            print(content)
            

    while True: 
        print("---------------------------------------------------------")
        start=input("What you want to do? (search/count/read/ (q) quit):")
        print('----------------------------------------------------------')
        if start == "search":
            search_engine()
        elif start =="count":
            word_counter()
        elif start == "read":
            read()
        elif start =="q":
            break
        else:
            print("Invalid input")

except FileNotFoundError:
    print("File not found")
except KeyboardInterrupt:
    print("You pressed Ctrl+C, Exiting...")
    



        



