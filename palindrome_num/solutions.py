
def palindrome(x:int):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


print(palindrome(x=1440441))