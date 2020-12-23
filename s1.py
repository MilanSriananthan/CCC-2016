start = input()
end = input()
start = list(start)
end = list(end)
leftover = []
for i in start:
    if i in end:
        end.remove(i)
    else:
        leftover.append(i)

if len(leftover) == end.count("*"):
    print('A')
else:
    print('N')


