# Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/6wjscp/2017828_challenge_329_easy_nearest_lucky_numbers/

# User Input: Positive Integer (e.g. 2)
    # Allow user to input a number
    # Validate that number is Positive

def numberCheck(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
                print("Please enter a positive number.")
                continue
        else:
            break
    return value

luckyNumber = numberCheck("Please enter a number to check.")

# Lucky number:
    # Step 1 - Begin with list of numbers (e.g. 1, 2, 3, 4, 5, ...)
    # Iteration 1 - 1 is a lucky number, remove every n+2 (every second) number from the 1st set
    # Iteration 2 - 3 is a lucky number, remove every n+3 number from second list
    # Iteration 3+ - n+4 is a lucky number, remove every n+4 number from third list
# Create list with consecutive numbers at least through chosen number.
# Based on the index value, identify lucky numbers and compute further lucky numbers.
# Loop through all numbers at least through luckyNumber value.

# While i < luckyNumber, if i >= LuckyNumber, iterate one more time and then pass top 3 variables to another list.
def lucky2(n):
    result = (list(range(10000000)))
    i = 1
    while result[(i)] <= luckyNumber:
        a = result[(i)]
        if i == 1:
            del result[a+1::a+1]
            i+=1
        elif a >= luckyNumber:
            del result[a::a]
            del result[a+1::a+1]
            i+=1
        else:
            del result[a::a]
            i+=1
    result = [result[i-2], result[i-1], result[i]]
    return result
luckyRange2 = lucky2(luckyNumber)

# Desired Output: Closest lucky number in syntax luckyNumberBelow < N < luckyNumberAbove
    # Run luckyNumber until N+1 is reached
    # Output 1 of 2 status':
        # Status 1: Input is not a lucky number, output both luckyNumberBelow < N < luckyNumberAbove
        # Status 2: Input is a lucky number, output "Number 'n' is a Lucky Number"

def luckyOutput2():
    if luckyRange2[1] == luckyNumber:
        print("Your number " + str(luckyNumber) + " is lucky!")
    else:
        print("Your number, " + str(luckyNumber) + ", is not lucky. The closest lucky numbers are " + str(luckyRange2[1]) + " and " + str(luckyRange2[2]) + ".")
luckyOutput2()
