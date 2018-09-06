# Taken from Reddit: https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/
#
# Create the "Alphabet Cipher" by creating a chart where each row
# of the alphabet is rotated by one as each letter goes down the
# chart.
#
# Create a validity check to ensure input is: single word, no numbers, no special characters.
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

# Input: Both people then agree on a secret keyword (such as "snitch")
# which is then used to encode the message.
secretKey = validityCheck("Please enter a secret keyword to encrypt your phrase with.")

# Input: A "secret" message is then added and encoded using the secret
# keyword.
unencryptedMessage = validityCheck("Please enter a phrase to encrypt.")

# Verify secretKey and unencryptedMessage variables are properly set.

# Create a mask for the secret key to allow proper encryption.
# For the example of below:
# Keyword = snitch, Message = thepackagehasbeendelivered:
# snitchsnitchsnitchsnitchsn
# thepackagehasbeendelivered
# While the variable "mask" is not as long as "unencryptedMessage"
# add the secretKey. If the "mask" variable is longer than unencryptedMessage
# remove the extra list items.

def masking(secret, message):
    i = 1; mask = ""
    while i <= len(message):
        mask += secret; i += 1
        if len(mask) > len(message):
            x = len(message); fullMask = mask[:x]
            break
    return fullMask

actualMask = masking(secretKey, unencryptedMessage)

# Create the cipher or masking algorithm according to
#   ABCDEFGHIJKLMNOPQRSTUVWXYZ
# A abcdefghijklmnopqrstuvwxyz
# B bcdefghijklmnopqrstuvwxyza
# C cdefghijklmnopqrstuvwxyzab
# D defghijklmnopqrstuvwxyzabc
# E efghijklmnopqrstuvwxyzabcd
# F fghijklmnopqrstuvwxyzabcde
# G ghijklmnopqrstuvwxyzabcdef
# H hijklmnopqrstuvwxyzabcdefg
# I ijklmnopqrstuvwxyzabcdefgh
# J jklmnopqrstuvwxyzabcdefghi
# K klmnopqrstuvwxyzabcdefghij
# L lmnopqrstuvwxyzabcdefghijk
# M mnopqrstuvwxyzabcdefghijkl
# N nopqrstuvwxyzabcdefghijklm
# O opqrstuvwxyzabcdefghijklmn
# P pqrstuvwxyzabcdefghijklmno
# Q qrstuvwxyzabcdefghijklmnop
# R rstuvwxyzabcdefghijklmnopq
# S stuvwxyzabcdefghijklmnopqr
# T tuvwxyzabcdefghijklmnopqrs
# U uvwxyzabcdefghijklmnopqrst
# V vwxyzabcdefghijklmnopqrstu
# W wxyzabcdefghijklmnopqrstuv
# X xyzabcdefghijklmnopqrstuvw
# Y yzabcdefghijklmnopqrstuvwx
# Z zabcdefghijklmnopqrstuvwxy
#
# An example of this would be:
# Keyword = snitch, Message = thepackagehasbeendelivered:
# snitchsnitchsnitchsnitchsn
# thepackagehasbeendelivered
# lumicjcnoxjhkomxpkwyqogywq
# locate cipherBase[18](s), locate cipherBase[19](t), restart cipherBase at
# cipherBase[19], count + 18 to locate encrypted value (l).

def encryptIt(mask, message):
    i = 0; encryptedMessage = ""
    while i < len(mask):
        cipherBase = list(string.ascii_lowercase); x = cipherBase.index(mask[i]); y = cipherBase.index(message[i])
        cipherBase.extend(list(string.ascii_lowercase))
        del cipherBase[:x:]
        u = cipherBase[y]; encryptedMessage += u; i+=1
        cipherBase = list(string.ascii_lowercase)
    return encryptedMessage

fullEncrypt = encryptIt(actualMask, unencryptedMessage)
print(fullEncrypt)


# Output: From the two above inputs, the user would then be provided
# the encrypted message, by masking the message with the looped
# keyword. The system would then encrypt the provided message by looking
# up the alphabet according to the looped letter and assigning the
# secret message the corresponding letter.
# An example of this would be:
# Keyword = snitch, Message = thepackagehasbeendelivered:
# snitchsnitchsnitchsnitchsn
# thepackagehasbeendelivered
# lumicjcnoxjhkomxpkwyqogywq
# The system would then output this encoded message (lumicjcnoxjhkomxpkwyqogywq)

# Bonus: Also implement a decryption portion, where the user inputs
# the keyword and encrypted message and is provided with the secret message.
