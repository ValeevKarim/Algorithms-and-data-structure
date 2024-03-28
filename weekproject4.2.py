class Myset:  # я его давно сделал, просто забыл отправить
    def __init__(self):
        self.set = []

    def add(self, x):
        self.new_set = []
        if len(self.set) == 0:
            self.set.append(x)
            return
        self.i = 0
        while self.i < len(self.set) and self.set[self.i] <= x:
            self.new_set.append(self.set[self.i])
            self.i += 1
            print(self.i)
        self.new_set.append(x)
        while self.i < len(self.set):
            self.new_set.append(self.set[self.i])
            self.i += 1
        self.set = self.new_set

    def remove(self, x):
        new_set = []
        for i in range(len(self.set)):
            if self.set[i] == x:
                x = '#'
                continue
            new_set.append(self.set[i])
        self.set = new_set

    def contains(self, x):
        for i in range(len(self.set)):
            if self.set[i] == x:
                return True
        return False


a = Myset()
a.add(1)
a.add(0)
a.add(3)
a.add(0)
a.add(-1)
a.remove(0)
print(a.set)
print(a.contains(4))
print((a.contains(3)))