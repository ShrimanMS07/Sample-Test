def calculate_sum(integers):
    total = 0
    for num in integers:
        if num % 2 == 0:  
            total += int(str(abs(num))[0]) * num  
        else:  
            if abs(num) < 10:  
                total += num * num
            else:
                total += (abs(num) % 10) * num  
    return total

numbers = list(map(int, input("Enter integers separated by commas: ").split(',')))
print("Result:", calculate_sum(numbers))