import datetime



current_time=datetime.datetime.now()
future_date= datetime.datetime(2026, 12, 25, 0, 0, 0)
difference= future_date - current_time
print(difference)
print(f"There are {difference.days} days left until Christmas.")
print(type(difference.days))