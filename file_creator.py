import json
import csv


class RecordKeeper:
    def __init__(self):
        self.records=[]

    def add_record(self, name, score, passed):
        self.records.append({"name":name, "score":score, "passed":passed})
        return

    def export_txt(self, filename):
        with open(filename,"w") as f:
            for record in self.records:
                f.write(f"Name: {record['name']} | Score: {record['score']} | Passed: {record['passed']}\n")
        

    def export_json(self, filename):
        with open(filename, "w")as f:
            json.dump(self.records, f, indent=4)

    def export_csv(self, filename):
        with open(filename, "w", newline="")as f:
            writer=csv.writer(f)
            writer.writerow(["Name", "Score", "passed"])
            for record in self.records:
                writer.writerow([record["name"], record["score"], record["passed"]])



r=RecordKeeper()

r.add_record("Raheem", 90, "True")
r.add_record("Osama", 80, "True")
r.add_record("Osman", 70, "True")

r.export_txt("records.txt")
r.export_json("records.json")
r.export_csv("records.csv")