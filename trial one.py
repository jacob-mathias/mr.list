def count_above_fifty(numbers):
    count = 0
    for num in numbers:
        if num > 50:
            count += 1
    return count

my_list = [17, 75, 48, 61, 50, 62, 59, 88, 44]
result = count_above_fifty(my_list)
print("Numbers above 50:", result)
