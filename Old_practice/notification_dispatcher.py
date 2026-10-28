class EmailNotifier:
    def send(self, message):
        return f"Email sent: {message}"


class SmsNotifier:
    def send(self, message):
        return f"SMS sent: {message}"


class DebugLogger:
    def send(self, message):
        return f"idk: {message}"


def deliver_all(notifiers, message):
    for notifier in notifiers:
        print(notifier.send(message))


if __name__ == "__main__":
    notifiers = [EmailNotifier(), SmsNotifier(), DebugLogger()]
    deliver_all(notifiers, "hi")
    deliver_all(notifiers, "lol")
