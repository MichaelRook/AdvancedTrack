class SMS_store:

    def __init__(self):
        self.store = []
        self.count = 0

    def add_new_arrival(self, number, time, text, viewed=False):
        self.store.append([number, time, text, viewed])
        self.count += 1

    def message_count(self):
        return self.count

    def get_unread_indexes(self):
        counter = 0
        for i in self.store:
            if not i(3):
                counter += 1
        return counter

    def get_message(self, i):
        a = self.store[i][:3]
        self.store[i][3] = True
        return a

    def delete(self, i):
        if i >= len(self.store):
            raise IndexError
        else:
            del self.store[i]
            self.count -= 1

    def clear(self):
        self.count = 0
        self.store.clear()


""" EXAMPLE """

# create inbox
my_inbox = SMS_store()

# add messages
my_inbox.add_new_arrival("06123", "12:30", "hi")
my_inbox.add_new_arrival("061234", "15:00", "bye")

print(my_inbox.store)

# get first message and change it into viewed
print(my_inbox.get_message(0))

# get all messages
print(my_inbox.store)

# clear inbox
my_inbox.clear()
print(my_inbox.store)
