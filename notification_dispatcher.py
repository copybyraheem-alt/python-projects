class EmailNotifier:
    def send(self, message):
        return f"Email sent: {message}"

class SmsNotifier:
    def send(self, message):
        return f"SMS sent: {message}"

class DebugLogger:
    def send(self, message):
        return f"idk: {message}"

obj= [EmailNotifier(), SmsNotifier(), DebugLogger()]
    
def deliver_all(notifiers, message):
    for notifier in notifiers:
        print(notifier.send(message))

deliver_all(obj, "hi")
deliver_all(obj, "lol")
