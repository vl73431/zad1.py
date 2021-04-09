# z = 0
# N = int(input("Enter the number:"))
# for i in range(1, N*10):
#     c = 0
#     for j in range(1, i+1):
#         a = i % j
#         if a == 0:
#             c = c + 1
#
#     if c == 2:
#         z = z+1
#         if z <= N:
#             print(i)
z=0
N = int(input("Enter the number:"))
k=1
while z<=N:
    c=0
    for i in range(1,k+1):
        remains=k%i
        if remains == 0:
            c=c+1
    if c==2:
        print(k)
        z=z+1
    k=k+1
