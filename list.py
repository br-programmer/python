
numbers = [3, 2, 1, 4, 5, 9, 7, 8, 6]
print('numbers:', numbers)
numbers.extend([10, 11, 12, 13, 14, 15, 16])
print('numbers extend:', numbers)
numbers.sort()
print('numbers sort:', numbers)
print('lenght numbers:', len(numbers))
numbers.insert(0, 20)
print('numbers insert 20 in position 0:', numbers)
numbers.remove(20)
print('numbers remove value 20:', numbers)
numbers.append(17)
print('numbers append 16:', numbers)
print('copy numbers:', numbers.copy())
print('repeat 16 in numbers:', numbers.count(16))
print('index value 1 in numbers:', numbers.index(1))
numbers.reverse()
print('numbers in reverse:', numbers)
numbers.reverse()
numbers.pop(2)
print('remove value in position 2:', numbers)

numbers.clear()
print('numbers clear:', numbers)