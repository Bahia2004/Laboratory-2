numbers = (1, 3, 2, 4, 3, 1, 2, 5)

for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):  
        if numbers[i] == numbers[j]:
            count += 1

    if count > 1:
        already_printed = False
        for k in range(i):  
            if numbers[k] == numbers[i]:
                already_printed = True
                break
        if not already_printed:
            print(numbers[i], "appears more than once")
