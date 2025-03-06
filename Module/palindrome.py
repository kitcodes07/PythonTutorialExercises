strings = input("Enter string for palindrome verification:").replace(" ","").lower()

if len(strings) == 0:
    print("It's not a palindrome.")
else:
    if strings == strings[::-1]:
        print("It's a palindrome.")
    else:
       print("It's not a palindrome.")
 #
 # mid = len(strings) // 2
 #   end = len(strings)-1
 #   count=0
 #   for i in range(mid):
 #       if strings[i] != strings[end - i]:
 #           count += 1
 #           break
 #   if count == 0:
 #       print("It's a palindrome.")
 #   else:
 #       print("It's not a palindrome.")



