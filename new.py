import time
import datetime

def set_alaram(alaram_time):
	print(f"okayy? {alaram_time}")
	is_running=True

	while is_running:
		current_time=datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time)
		
		if current_time==alaram_time:
			print("Wake up!!")
			is_running=False
		time.sleep(1)

if __name__=='__main__':
	user_alaram= input("Enter alarm time (HH:MM:SS): ")
	set_alaram(user_alaram)

