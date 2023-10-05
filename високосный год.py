a = int(input())
z = a % 4
b = a % 100
c = a % 400
if z == 0 and b != 0 or c == 0:
    print('YES')
else:
    print('NO')