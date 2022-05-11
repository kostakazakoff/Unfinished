targets = list(map(int, input().split()))
command = input()

while command != 'End':
    command = command.split()
    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if index < 0:
        index += len(targets)

    if action == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= value

    elif action == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')

    elif action == 'Strike':
        value = abs(value)
        if index - value >= 0 and len(targets) > index + value:
            for i in range(index - value, index + value + 1):
                targets[i] = 0
        else:
            print(f'Strike missed!')

    targets = list(filter(lambda x: x > 0, targets))
    command = input()

targets = list(map(str, targets))
print('|'.join(targets))
