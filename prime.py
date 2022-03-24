def prime(s):
    number = 0
    for i in range(1, s+1):
        if s%i== 0:
            number = number + 1   
    if number == 2:
        print(f"prime Number{i}")
    else:
        print(f"Not prime Number{i}")
        
if __name__=="__main__":
    s = int(input("Number:"))
    prime(s)

num = int(input("Num:"))
arr = []
sum = 0
count = 0
if num > 1:
    for i in range(2, num+2):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                arr.append(i)
                
def is_prime(sum):
    for i in range(2, (sum // 2) +2):
        if sum % i == 0:
            return False
        else:
            return True
for i in range(0, len(arr)):
    sum = sum + arr[i]
    if sum <= num:
        if is_prime(sum):
            count = count + 1
print(count)
    


