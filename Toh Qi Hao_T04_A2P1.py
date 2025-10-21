# Full Name: Toh Qi Hao
# Tutorial Group: CSIT 110 T04
# Declaration: it is my own work and i have not
# passed my program to my friends


#title:
#define user input of credit card number
# A function to check if a credit card is valid

def user_input():
    while True:
        user_card_number = input("\nWelcome to ABC credit card company\n\nEnter a credit card: ")
        
        if validate_card(user_card_number):
            return user_card_number
        else:
            another_card = input("Another card (y/Y/n/N): ").strip().lower()
            print("-"*100)
            if another_card != 'y':
                input("Press enter to terminate")
                exit()

def validate_card(card_number):
    # Remove hyphens
    numbers = card_number.replace("-", " ")
    
    # Check for non-digit characters
    # Return false means return to def user_input(): else part
    if not all(char.isdigit() or char.isspace() for char in numbers):
        print("==> Non digits in card\n")
        return False
    
    # Split into tokens
    # Into 4 groups of number
    tokens = numbers.split()
    
    # Check the number of tokens
    # If length of tokens is not equal to 4 groups
    # If length of tokens have more than 4 groups: too many tokens 
    # Else, too few tokens 
    # Return false means return to def user_input(): else part
    
    if len(tokens) != 4:
        if len(tokens) > 4:
            print("==> Too many tokens\n")
        else:
            print("==> Too few tokens\n")
        return False
    
    # Check each token length
    # Specify the numbers in token 
    # If the length of tokens is not equal to 4
    # Return false means return to def user_input(): else part
    for token in tokens:
        if len(token) != 4:
            print("==> Invalid length\n")
            return False
    # Return to user_input()
    return True

# Remove the hyphen 
# Whenever you call the function def remove_hypen-card, it performs the work and the gives the result 
# Analoy: you give the worker some raw material (input)
        # The worker processes it (does some work)
        # The worker returns the finished product to you (output)
# reality: you give the function a card number with hyphens
        # The function removes the hypens and splits the numbers
        # the function returns the list of numbers to you

# 'returns' send the result of the function's work back to where the function was called

# parameters: if the user_card_number is 1234-1234-1234-1234
            # numbers = 1234-1234-1234-1234.replace - with ' ' 
            # meaning that 'user_card_number' is just a representative only
def remove_hyphen_card(user_card_number):
    numbers = user_card_number.replace("-", " ").split()
    return numbers

# A function to get the reverse of a positive integer. 
# 'number [::-1]' reverse the string 'number'
# 'for number in numbers' performs over each string in the 'numbers' list

def reverse_numbers(numbers):
    reversed_numbers = [number[::-1] for number in numbers]
    return reversed_numbers

#A function to form a new integer so that the 2nd the 4th digits are doubled

def multiply_even_positions(numbers):
    # initialise an empty space list to store the modified strings
    updated_numbers = []
    # go through each 4 digits string in the input list 
    for number in numbers:
        # Directly construct the modified number
        # number[0] means first digit, number [1] means second digit (like formatting)
        modified_number = (
            number[0] +
            str(int(number[1]) * 2) +
            number[2] +
            str(int(number[3]) * 2)
        )
        # add the modified number to the list
        updated_numbers.append(modified_number)
    return updated_numbers

# A function to find the sum of digits of a given positive integer.

def sum_of_digits_of_each_token(numbers):
    # initialise an empty space list to store the modified strongs
    sum_of_digits = []
    # goes through each 4 digits string in the input list
    for number in numbers:
        # add all 4 digits 
        # sum is a in-built function thats adds up 
        sum_digits = sum(int(digit) for digit in number)
        # add sum_digits into the list
        sum_of_digits.append(str(sum_digits))
    return sum_of_digits

# A function to find the sum of elements of a given positive integer.

def sum_of_all_elements(numbers):
    total_sum = sum(int(digit) for number in numbers for digit in number)
    return total_sum

# A function to divide the sum of elements by 10 to determine if the value is valid (=0)

def mod_sum_of_all_elements(total_sum):
    mod_all_elements = int(total_sum) % 10
    return mod_all_elements


def main():

    to_loop = True
    while to_loop:
        user_card_number = user_input()
    
        print("\nAnalysis:")
        print("\t(a) To get the reverse of each 4 digits")
        
        numbers = remove_hyphen_card(user_card_number)
        
        reversed_numbers = reverse_numbers(numbers)
        
        # Joining reversed numbers with adequate spacing
        formatted_reversed_output = "\t\t".join(reversed_numbers)
        print(f"\t\t{formatted_reversed_output}")
        
        print("\n\t(b) To multiply by 2 each even digit position")
        
        modified_numbers = multiply_even_positions(reversed_numbers)
        
        # Joining modified numbers with adequate spacing
        formatted_add2_even_output = "\t\t".join(modified_numbers)
        print(f"\t\t{formatted_add2_even_output}")

        print("\n\t(c) To get the sum of all digits in card elements")

        sum_digits = sum_of_digits_of_each_token(modified_numbers)
        
        # Joining sum of digits with adequate spacing
        formatted_sum_of_digits_output = "\t\t".join(sum_digits)
        print(f"\t\t{formatted_sum_of_digits_output}")

        print("\n\t(d) To find the sum of all elements in card")

        total_sum = sum_of_all_elements(modified_numbers)
        
        # Formatted sum of all elements similiar to display
        print(f"\t\tThe special sum is {total_sum}")

        mod_all_elements = mod_sum_of_all_elements(total_sum)

        #if mod all elements = 0, the card is valid

        if mod_all_elements == 0:
            print("\nConculsion:")
            print(f"\n\t{user_card_number} is a valid credit card number because {total_sum} % 10 = 0 ")

        #or else, the card is invalid

        else:
            print("\nConculsion:")
            print(f"\t{user_card_number} is a invalid credit card number because {total_sum} % 10 != 0 ")

        another_card = input("\nAnother card (y/Y/n/N): ").strip().lower()

        #if user did not say y or Y, the program will exit the loop 

        if another_card != "y":
            print("-"*100)
            input("Press enter to terminate")
            to_loop = False


if __name__ == "__main__":
        main()



    


