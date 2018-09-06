# Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/
#
# Given two strings of letters, determine whether the second can be made from the first by removing one letter.
# The remaining letters must stay in the same order.
# Examples
# funnel("leave", "eave") => true
# funnel("reset", "rest") => true
# funnel("dragoon", "dragon") => true
# funnel("eave", "leave") => false
# funnel("sleet", "lets") => false
# funnel("skiff", "ski") => false

import re
import string

def validityCheck(prompt):
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if len(value.split()) > 1:
                print("Input must be a single word.")
                continue
        if not re.match("^[a-z]*$", value):
            print("Please remove any special characters and numbers from your input.")
            continue
        else:
            break
    return value

rootWord = validityCheck("Please enter a root word to check against.")
checkWord = validityCheck("Please enter a word to check.")

def wordCheck(x, y):
    i = 0
    while i < len(x):
        checkAgainst = x[:i] + x[(i+1):]
        if len(x) < len(y):
            print("Please enter a word to check that is shorter than the root word.")
            return
        if checkAgainst == y:
            print(x + " does contain " + y + ".")
            return
        else:
            print("No match.")
            i+=1; checkAgainst = x
            if i >= len(x):
                print(x + " does not contain " + y + ".")

wordCheck(rootWord, checkWord)
  
