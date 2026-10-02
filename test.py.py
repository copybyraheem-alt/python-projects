import os


def read_scores(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return {}

    scores = {}  # creating an empty dictionary
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) == 2:
                name, score = parts[0].strip(), parts[1].strip()
                try:
                    scores[name] = int(score)
                except ValueError:
                    continue
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
