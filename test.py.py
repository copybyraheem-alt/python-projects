from importlib import readers
import os


def read_scores(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return {}
    else:
        scores={} #creating an empty dictionary
        with open(path, "r") as file:
            for line in file:
                line=line.strip()
                name,score=line.split(",")
                score=int(score)
                scores[name]=score
            return scores

with open("scores.txt", "w") as file:
    file.write("Alice,90\n")
    file.write("Bob,75\n")
    file.write("cara,60\n")

with open("scores.txt", "r") as file:
    data=file.read()
    print(data)

data= read_scores("scores.txt")
print(data)
other=read_scores("missing.txt")
print(other)
