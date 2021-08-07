# write a program to remove the duplicates in a list

numbers = [5, 2, 1, 7, 4, 5, 3, 3, 7, 0, 4]
uniques = []

for number in numbers:
    if number is not in uniques:
        uniques.append(number)
print(uniques)
