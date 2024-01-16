numbers = [1, 2, 3, 4, 5, 99, 2600, 300]
reversed_list = numbers[::-1]
print(reversed_list)

s = "abcdef"
l = []
for x in range(len(s)):
    l.append(s[x])
l.reverse()
s2 = ""
for x in l:
    s2 = s2 + x
print(s2)

gang = ["Charlie", "Mac", "Dennis", "Dee", "Frank"]
if "Dee" in gang:
    gang.remove("Dee")
else:
    gang.append("Dee")
print(gang)