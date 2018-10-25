import time

print("Fibonacci Sequence using pop to 25:")
startTime = time.time()
fibonacci = [0,1]
for i in range(2,26): 
    fibonacci.append(fibonacci[0]+fibonacci[1])
    fibonacci.pop(0)
print(fibonacci[1])
print(float(time.time() - startTime), "seconds")

print("Fibonacci Sequence growing to 25:")
startTime = time.time()
growFibon = [0,1]
for i in range(2,26):
    growFibon.append(growFibon[i-1] + growFibon[i-2])
print(growFibon[25])
print(float(time.time() - startTime), "seconds")


print("Fibonacci Sequence Recursive Function to 25:")
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

startTime = time.time()
print(recursive_fibonacci(25))
print(float(time.time() - startTime), "seconds")


