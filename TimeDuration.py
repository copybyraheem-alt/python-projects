class TimeDuration:

    def __init__(self, hours=0, minutes=0, seconds=0):
        
        if hours<0:
            raise ValueError("Time cannot be negative")

        if minutes<0:
            raise ValueError ("Time cannot be negative")

        if seconds<0:
            raise ValueError ("Time cannot be negative")
        
        self.total_seconds= hours* 3600 + minutes * 60 + seconds

        
    def __str__(self):
        return f"{self.total_seconds//3600:02d}:{(self.total_seconds%3600)//60:02d}:{self.total_seconds%60:02d}"


    def __add__(self, other):
        return TimeDuration(seconds=self.total_seconds + other.total_seconds)

    def __sub__(self, other):
        calc= self.total_seconds - other.total_seconds
        if calc <0:
            raise ValueError ("Time cannot be negative")
        return TimeDuration(seconds=calc)

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        return self.total_seconds<other.total_seconds

    def __mul__(self, multiplier):
           if type(multiplier) != int:
               raise TypeError ("Multiplier must be an integer")
           else:
            calc= self.total_seconds * multiplier

           return TimeDuration(seconds=calc)


t1=TimeDuration(1, 61, 65)
t2=TimeDuration(0,30,0)



print(t1)
print(t2)
print(t1+t2)
print(t1 - t2)
print (t1 == t2)
print (t2 < t1)
print (t2 * 3)