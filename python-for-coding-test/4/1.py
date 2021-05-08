n = int(input())
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
x, y = 1, 1

for plan in plans:
    for j in range(len(move_types)):
        if plan == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
        else:
            continue
            
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
            
        x, y = nx, ny
        
print(x, y)