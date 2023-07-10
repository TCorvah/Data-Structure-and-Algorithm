def isPalindrome(str):
    empty_str = ""
    assert len(str) != empty_str
    if len(str) == 1:
        print('A one letter word is a palindrome\n')

    elif str == str[::-1]:
        print(str, "is a palindrome\n")
        
    else:
        print(str, "is not a palindrome\n")
            
   
     
# main

s = input('Enter string to check: ')
ans = isPalindrome(s)



