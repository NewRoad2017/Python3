class Book(object): # this a new class
    #private static field
    __author = "chenlu"
    # the first method:
    @property
    def author(self): # when refer,has not a brackets
        return "unKnown"
    @author.setter
    def author(self,value):
        self.__author = value
    @author.deleter
    def author(self):
        pass
    #ordinary method
    def __init__(self):
        #ordinary field
        self.publishTime = "2017-09-15 00:00:00"
    #ordinary method
    def Print(self):
        print (Book.author)
    @classmethod
    def PrintCountry(cls):#this is a default arg
        print (cls.author)
    @staticmethod
    def static_func():
        pass


if __name__ == '__main__':
    book = Book()
    # a = Book.author
    a = book.author
    book.Print()