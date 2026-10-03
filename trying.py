from datetime import datetime



m=datetime(2009, 7, 28)
r=datetime(2008, 7, 15)

print(f"born on a {m.strftime('%A')} in the year {m.strftime("%Y")}, in the month of {m.strftime("%B")}")
print(f"born on a {r.strftime('%A')} in the year {r.strftime("%Y")}, in the month of {r.strftime("%B")}")

print(f"The age gap is {(m-r).days} days")

