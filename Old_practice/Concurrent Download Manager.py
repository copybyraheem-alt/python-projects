import threading
import time



def download(file_name, duration):
    print(f"[START] {file_name} (needs {duration}s)")
    time.sleep(duration)
    print(f"[DONE] {file_name}")

def run_all(files):
    start= time.time()
    threads=[]
    for name,duration in files:
        t=threading.Thread(target=download, args=(name, duration))
        threads.append(t)

    for thread in threads:
        thread.start()

    for the in threads:
        the.join()
    end=time.time()

    print(f"Total wall-clock:{end-start:.2f}")


if __name__=="__main__":
    files = [
    ("video.mp4", 2),
    ("song.mp3", 1),
    ("notes.txt", 0),
    ("image.png", 1),
    ]

    run_all(files)
    print("All downloads complete.  ")

    



