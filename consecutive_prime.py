# def prime_number(n):
#         primes = [2]
#         for p in primes:
#             print(p) 
    
#         for num in range(3, n, 2):
#             for prime in primes:
#                 if num % prime == 0:
#                     break
#                     # isprime = False
#             else:
#                 primes.append(num)
#                 yield num
# l = prime_number(20)
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())



class PrimeList:
    def __init__(self, limit):
        self.limit = limit
        self.value = 2
        
    def __iter__(self):
        return self
    
    def is_prime(self, x):
        while True:
            try:
                y = next(self)
                if x % y == 0:
                    return False
            except StopIteration:
                return True

    def __next__(self):
        while self.value < self.limit:
            divisors = PrimeList(int(self.value ** 0.5) + 1)  # recursion
            found = divisors.is_prime(self.value)
            self.value += 1
            if found:
                return self.value - 1
        raise StopIteration()

test = PrimeList(100)
print(next(test))
print(next(test))
print(next(test))

# next(test)
        
        
                
                
        






















    
# class consecutive():
#     def prime_number(self, n):
#         primes = [2, 3]
#         for p in primes:
#             print(p) 
            
#         for num in range(5, n, 2):
#             isprime = True
#             for prime in primes:
#                 if num % prime == 0:
#                     isprime = False
#                     break
            
#             if isprime:
#                 primes.append(num)
#                 print(num)
                
    
# a = consecutive()
        
# a.prime_number(10)

    
# # print(a.__next__())




      
        
        
    