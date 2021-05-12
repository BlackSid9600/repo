input = input('Введитет значения:')
list = []
list.extend(input)
# print(list)

num = len(input)

if num % 2 == 0:
    x = 0
    while x < num:
        r = list[x]
        list[x] = list[x + 1]
        list[x + 1] = r
        x += 2

else:
    x = 0
    while x < num - 1:
        r = list[x]
        list[x] = list[x + 1]
        list[x + 1] = r
        x += 2
print(list)




# print(num)
# while num > 0:
#     step = input[x]
#     n = []
#     x += 1
#     n.insert(x, step)
# print(n)