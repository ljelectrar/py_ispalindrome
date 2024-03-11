
user_in = input("Enter a word: ")

# test a palindrome
def is_palindrome(str):
    list(str)
    if str == str[::-1]:
        print("Is a palindrome")
    else:
        print("It is not a palindrome")

is_palindrome(user_in)