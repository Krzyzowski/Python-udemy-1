
def add_numbers(num1, num2):

    result = num1 + num2
    return result

sum_result = add_numbers(num1= 5, num2= 3)
print("the sum is:", sum_result)

def concat_uppercase(str1, str2):

    result = str1 + str2
    return result.upper()

concatenated_str = concat_uppercase("hello ", "world")
print(concatenated_str)