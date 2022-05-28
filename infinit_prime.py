class Prime:
    def __init__(self, start=1):
        print("Prime.__init__")
        self.current = start
    
    def __iter__(self):
        print("Prime.__iter__")
        return self
    
    def is_prime(self, n):
        print("Prime.is_prime")
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def __next__(self):
        print("Prime.__next__")
        next_prime = self.current + 1
        while not self.is_prime(next_prime):
            next_prime += 1
        self.current = next_prime
        return self.current
        
        

a = Prime()
print(a.current)
# next(a)
for i in a:
    print(i)
    if i > 2:
        break
    
def mimic_for():
    pass
    
while(a.current < 3):
    print(next(a))
while(a.__iter__()):
    s = a.__iter__()
    print(next(a))
    if s.current > 2:
        break
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


        
        
        
        