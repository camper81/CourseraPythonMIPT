#  from abc import ABC, abstractmethod
#
# class Engine():
#     def __init__(self):
#         pass


class ObservableEngine(Engine):
    def __init__(self):
        self.listners = set()

    def subscribe(self,subscriber):
        self.listners.add(subscriber)

    def unsubscribe(self,subscriber):
        self.listners.remove(subscriber)

    def notify(self, message):
        for listner in self.listners:
            listner.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass

class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()


    def update(self, message):
        self.achievements.add(message['title'])

class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)

