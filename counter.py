#countdown timer
import time
n=int(input("Enter countdown number:"))
print("\n countdown start:")
for i in range(n,0,-1):
    print(i)
    time.sleep(1)
print("Happy new year🥳 ")