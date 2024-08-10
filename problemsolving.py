
enternum = input("Enter a list of integers separated by spaces: ")

num_list = list(map(int, enternum.split()))

uniquenums = list(set(num_list))


uniquenums.sort(reverse=True)


print("nums with no duplicates:", uniquenums)
