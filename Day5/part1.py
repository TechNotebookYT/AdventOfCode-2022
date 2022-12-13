file = open('input.txt', 'r')
lines = file.readlines()

stack1 = ['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T']
stack2 = ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V']
stack3 = ['B', 'J', 'F', 'H', 'D', 'R', 'P']
stack4 = ['F', 'R', 'P', 'B', 'M', 'N', 'D']
stack5 = ['H', 'V', 'R', 'P', 'T', 'B']
stack6 = ['C', 'B', 'P', 'T']
stack7 = ['B', 'J', 'R', 'P', 'L']
stack8 = ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W']
stack9 = ['L', 'S', 'G']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

lines = lines[10:]
# print(lines[0])

for line in lines:
    num_of_crates, places = line.split(" from ")
    num_of_crates = int(num_of_crates[5:])
    start, end = places.split(" to ")
    
    start = int(start)
    end = int(end)
    # print(num_of_crates, start, end)
    for i in range(num_of_crates):
        stacks[end-1].append(stacks[start-1].pop())

crates_at_top = ''

for stack in stacks:
    crates_at_top += stack.pop()

print(crates_at_top)