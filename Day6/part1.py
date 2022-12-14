file = open('input.txt', 'r')

msg = file.read()
# print(msg)
for i in range(len(msg)-4):
    first = msg[i]
    second = msg[i+1]
    third = msg[i+2]
    fourth = msg[i+3]

    print(first, second, third, fourth)
    values = []

    # Checks if characters do not match
    if first not in values:
        values.append(first)
    if second not in values:
        values.append(second)
    if third not in values:
        values.append(third)
    if fourth not in values:
        values.append(fourth)
    
    if len(values) == 4:
        print(i+4)
        break
    


