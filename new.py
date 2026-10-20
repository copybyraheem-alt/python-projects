import datetime
import time



class Alarm:

    def __init__(self,time_str, label):
        if not time_str== datetime.datetime.strptime(time_str, "%H:%M:%S"):
            raise ValueError ("Error")
        else:
            self.time_str = time_str

        clean_label=label.strip()

        if clean_label == "":
            self.label= "General alarm"
        else:
            self.label=clean_label





class AlarmClock:

    def __init__(self, log_file="alaram_log.txt"):
        self.alarm=[]
        self.log_file=log_file


    def add_alarm(self, time_str, label):
        try:
            my_alarm = Alarm(time_str, label)

            self.alarm.append(my_alarm)
            print("Alarm added successfully")
            return True

        except ValueError:
            print("invaild details, please fill correctly")
            return False


    def log_trigger(self, alarm):
         with open(self.log_file, "a") as f:
             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
             f.write(f"[{timestamp}] TRIGGERED: {alarm.label} set for {alarm.time_str}\n")

    def run(self):
        if not self.alarm:
            print("No Alarm to moniter")
            return
        while self.alarm:
            current_time = (datetime.datetime.now().strftime("%H:%M:%S"))
            print(current_time)

            for alarm in list(self.alarm):
                if alarm.time_str==current_time:
                    print(f" ALARM! {alarm.label} ")
                    self.log_trigger(alarm)
                    self.alarm.remove(alarm)
            time.sleep(1)



if __name__=='__main__':
    my_clock= AlarmClock()
    while True:
        choose=int(input("How many alarms do you want to set?"))

        if choose > 0:
            break
        else:
            print("please write a vaild count")

    for _ in range(choose):
        while True:
            time_str = input("Enter alarm time (HH:MM:SS): ")
            label = input("Enter alarm label: ")
            if my_clock.add_alarm(time_str, label):
                break

    my_clock.run()


    


