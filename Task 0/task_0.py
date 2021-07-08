# Варіант 1
import random
arr = [random.randint(-100,100) for i in range(30)]
MaxNumb=max(arr)
arr.index(MaxNumb)
print(arr)
print("Max number is " + str(MaxNumb))
print("This number is in " + str(arr.index(MaxNumb)+1)+"th place")
for i in range(29):
    if i%2 ==0:
        odds =[ n for n in arr if n%2]
odds.sort(reverse = True)
print(odds)


