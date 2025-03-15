# WAP to print all numbers from 1 to 50 which is divisible by 3 and 7

start = 1
end = 50
for i in range (start, end+1):
    if i%3 == 0 & i%7 == 0:
        print(i)