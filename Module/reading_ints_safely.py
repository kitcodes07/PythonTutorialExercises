def read_int(prompt, min, max):
    while True:
        try:
           num = int(input(prompt))
           assert min <= num <= max
           return num

        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range ({0}..{1})".format(min, max))



v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)