def is_even(num):
    if num % 2 == 0: return True
    return False

def is_odd(num):
    if is_even(num): return False
    return True

def only_evens(nums):
    l = []
    for i in nums:
        if is_even(i): l.append(i)
    return l

def only_odds(nums):
    l = []
    for i in nums:
        if is_odd(i): l.append(i)
    return l

def smallest(nums):
    nums.sort()
    return nums[0]

def largest(nums):
    nums.sort(reverse=True)
    return nums[0]

def shortest(strings):
    strings.sort(key=len)
    return strings[0]

def longest(strings):
    strings.sort(key=len, reverse=True)
    return strings[0]

print(only_evens([11, 20, 42, 97, 23, 10]))
print(only_odds([11, 20, 42, 97, 23, 10]))
print(smallest([11, 20, 42, 97, 23, 10]))
print(largest([11, 20, 42, 97, 23, 10]))
print(shortest(["this is sooooo long", "short", "medium", "long"]))
print(longest(["this is sooooo long", "short", "medium", "long"]))
