string1 = input("Enter 1st string for anagram verification:").replace(" ","").lower()
string2 = input("Enter 2nd string for anagram verification:").replace(" ","").lower()

if sorted(string1) == sorted(string2):
    print("Anagrams")
else:
    print("Not anagrams")