class Iterables():
    
    def __init__(self):
        self.stor_book = {}  
        
    def st(self, student, namber):
        self.stor_book [student] = self.stor_book.get(student, namber)
            
    def __iter__(self):
        return iter(self.stor_book.items())
    
    
a = Iterables()
a.st("Ali", 430)
a.st("Ahmed", 340)       
a.st("Irfan", 500)       
a.st("Saad", 310)       
a.st("Irsalan", 290)     
for (student, namber) in a:
    print(student, namber)
    # print(type(student))
       