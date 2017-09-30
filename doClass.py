class animal(object):
    def __init__(self,data):
        print (data)

    def eat(self):
        print (" %s eat" % (self.name))


class Cat(animal):
    # pass
    def __init__(self,data):
        self.name = "mimi"

if __name__ == '__main__':
    cat = Cat('dd')
    cat.eat()