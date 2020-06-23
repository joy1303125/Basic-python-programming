for i in range(10,21):
    print(i)

digits=[10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20]
print(digits[8:0:-3])
print(digits[::-2])
window_size=-5
for i in range (len(digits)):
    print(i)
    print(digits[0:i])
    print(digits[0:i + 3])
    print(digits[0:i + window_size])
for i in range (len(digits)-2):
    print(i)
    print(digits[0:i])
    print(digits[0:i + 3])
    print(digits[0:i + window_size])
