def shift_op(chv, sv, limit):

    if (ord(chv) + sv) > ord(limit):

        return chr(ord(chv) + sv - 26)
    else:
        return chr(ord(chv) + sv)


word = input("Enter the string to encrypt:")
enc = ''
while True:
    try:
        shift_value = int(input("Enter shift value:"))
        if 0 < shift_value < 26:
            break
        else:
            print("Enter an integer from 1 - 25")
    except:
        print("Enter an integer from 1 - 25")

for ch in word:
    if ch.isalpha() and ch.isupper():
        enc += shift_op(ch, shift_value, 'Z')

    elif ch.isalpha() and ch.islower():
        enc += shift_op(ch, shift_value, 'z')
    else:
        enc += ch

print(enc)