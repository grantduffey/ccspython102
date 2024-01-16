condition = True

while condition:
    print("Please choose two numbers from 0-100")
    start = int(input("Starting number: "))
    if start < 0 or start > 100: continue
    end = int(input("Ending number: "))
    if end < 0 or end > 100: 
        continue
    if end < start: 
        print("Please make your ending number bigger than your starting number\n")
        continue
    condition = False

count = int(input("Count by: "))

while start <= end:
    print(start)
    start += count

