file = open('input.txt', 'r')

msg = file.read()
# print(msg)
for i in range(len(msg)-4):
    fourteen_chars = []
    [fourteen_chars.append(msg[i+j]) for j in range(14)]


    unique_chars = []
    for char in fourteen_chars:
        if char not in unique_chars:
            unique_chars.append(char)
    
    print(unique_chars)
    if len(unique_chars) == 14:
        print(i+14)
        break