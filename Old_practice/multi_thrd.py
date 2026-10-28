import threading
import time

def count_up(name, count):
    for i in range(1, count+1):
        print(f"{name} working.....{i}")
        time.sleep(0.5)

def count_down(name, count):
    for i in range(count, 0, -1):
        print(f"{name} working.....{i}")
        time.sleep(0.5)

t1=threading.Thread(target=count_up, args=("uploader", 3))
t2=threading.Thread(target=count_down, args=("downloader", 3))

t1.start()
t2.start()

t1.join()
t2.join()

print("All work finished")