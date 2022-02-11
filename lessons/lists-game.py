"""Examples of using lists in a simple 'game'."""


from random import randint


rolls: list[int] = list()
rolls.append(randint(1, 6))
rolls.append(3)
print(rolls)

# Access an individual item
print(rolls[0])
print(rolls[1])

# Access the length of a list (number of items)
print(len(rolls))

# Access the last item of a list
print(rolls[len(rolls) - 1])
