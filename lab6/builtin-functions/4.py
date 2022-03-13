import time, math

timed = int(input())
dec = int(input())
root = math.sqrt(dec)
time.sleep(timed / 1000)
print("Square root of " + str(dec) + " after " + str(timed) + " miliseconds is")
