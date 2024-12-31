#Check the number is Even or Odd
def check_Even_Odd(num):
    if num % 2 == 0:
        return f"The given {num} is Even"
    else:
        return f"The given {num} is Odd"


# result = check_Even_Odd(10.2)
# print(result)


# Multiplication table
def Multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
        

# value = Multiplication_table(5)

#Sum of natural numbers
def Sum_of_Natural_Numbers(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    return res
 
# print(Sum_of_Natural_Numbers(10))


#Fibanocci series
def Fibanocci_series(num):
    res = [0,1]
    for i in range(2,num):
        res.append(res[i-1] + res[i-2])
    return res
        
# print(Fibanocci_series(10))

#Swap two numbers:
def Swap_two_numbers(num1, num2):
    num1, num2 = num2, num1
    return num1, num2

# print(Swap_two_numbers(10, 20))

#Find the closet number to num1 and it should be divisible by num2
def Closet_Number(num1, num2):
    q = num1 % num2

    if (((abs(num1) + q) * -1) % num2) == 0:
        return f"{abs(num1) + q} is closet number to {num1} and divisible by {num2}"
    elif ((num1 - q) % num2) == 0:
        return f"{num1 - q} is closet number to {num1} and divisible by {num2}"
    
    
    
# print(Closet_Number(13, 4))
print(Closet_Number(-15, 6))


#find the other face of the dice
def Dice(num):
    if num < 1 or num > 6:
        return "Invalid"
    
    return f'The Opposite face of the number {num} in the Dice is {7 - num}'

# print(Dice(6))

#Arithmetic progression

def Arithmetic_progression(nums, n):
    sorted_nums = sorted(nums)
    
    diff = sorted_nums[1] - sorted_nums[0]
    
    for i in range(1, n):
        if sorted_nums[i] - sorted_nums[i-1] != diff:
            return "Not an Arithmetic progression"
        
    return "It's Arithmetic progression"

print(Arithmetic_progression([1,2,3,4,5], 5))

#geomentric series

def Geometric_progression(a,r,n):
    return a * ( 1 - r ** n) / (1 - r)

print(Geometric_progression(2, 2, 15))