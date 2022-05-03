class DemoIterator():

    def __init__(self, number):
        self.value = number
        self.index = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 2:
            self.index += 1
            return (self.index - 1)
        if self.index < self.value:
            notprime = True
            while notprime:
                flag = True
                for j in range(2, self.index):
                    if self.index % j == 0:
                        flag = False
                        notprime = True
                        self.index += 1
                        break
                if flag:
                    self.index += 1
                    return (self.index - 1)
        else:
            raise StopIteration

                # print("Iterations are over")


d = DemoIterator(100)
for i in d:
    print(i)