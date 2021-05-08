input_str = input()
row = int(input_str[1])
col = ord(input_str[0]) - ord('a') + 1

steps = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1)]

result = 0
for step in steps:
    if row + step[0] < 1 or row + step[0] > 8 or col + step[1] < 1 or col + step[1] > 8:
        continue
    else:
        result += 1
        
print(result)