# 

# def display_breakfast(breakfast_fruit):
#     print(f"My breakfast today is {breakfast_fruit}")

# display_breakfast("an apple")
# print("Let's try to access the value of breakfast_fruit outside of the display_breakfast function:")
# print(f"The value of breakfast message is {breakfast_fruit}")

# def display_breakfast():
#     breakfast_message = "My breakfast today is an apple"
#     print(breakfast_message)
#     return breakfast_message

# resulting_message = display_breakfast()
# print("Instead of trying to access breakfast_message, let's return breakfast_message, store it in resulting_message, and access resulting_message instead:")
# print(f"The value of resulting_message is {resulting_message}")


# def display_breakfast():
#     print("Let's try to access the value of breakfast_message INSIDE of the display_breakfast function:")
#     print(breakfast_message)


# breakfast_message = "My breakfast today is an apple"
# print("Let's try to access the value of breakfast_message OUTSIDE of the display_breakfast function:")
# print(f"The value of breakfast message is {breakfast_message}")

# display_breakfast()

# def display_breakfast(breakfast_of_champions):
#     # The parameter breakfast_of_champions exists in this function!
#     print(f"This function call has the parameter breakfast_of_champions with the value {breakfast_of_champions}")

#     # The local variable breakfast_message exists in this function!
#     breakfast_message = f"My breakfast today is {breakfast_of_champions}"
#     print(breakfast_message)

#     # After the return statement, the function will end, and breakfast_of_champions AND breakfast_message will no longer exist...
#     return breakfast_message

# # display_breakfast("waffles and syrup")
# value_1=display_breakfast("waffles and syrup")
# print(f"Uncommenting this line and trying to access breakfast_of_champions will create a NameError: {value_1}")
# print(f"Uncommenting this line and trying to access breakfast_message will create a NameError: {value_1}")

# apples = 1000
# oranges = apples

# print("id of apples:", id(apples))
# print("id of oranges:", id(oranges))

# my_list=[[1,2,3],[4,5,6]]
# print(my_list)
# print("my_list id is :",id(my_list))
# my_list[0].append(9)
# print(my_list)
# print("my_list id is:",id(my_list))

# my_list_second=[{"name":"halise","ID":115},{"name":"hedi","ID":223}]
# print(my_list_second)
# print("my_list_second id is:",id(my_list_second))
# my_list_second[1]["pro"]="she/her"
# print(my_list_second)
# print("my_list_second id is:",id(my_list_second))

# def add_clovers(charms):
#     print("==== Appending 'clovers' to charms ====")
#     print("id of charms:", id(charms))
#     charms.append("clovers")

# berries = ["hearts", "stars", "horseshoes"]
# print("==== Before calling add_clovers ====")
# print("id of berries:", id(berries))
# print("value of berries:", berries)

# add_clovers(berries)

# print("==== After calling add_clovers ====")
# print("id of berries:", id(berries))
# print("value of berries:", berries)



# import string
# letters =list(string.ascii_lowercase)
# print(letters)

# def get_last_letter(letters):
#       letter =letters.pop()
#       return letter
# letter =get_last_letter(letters)
# print(letter)
# print(letters)

value_1=None
print("id of value_1:", id(value_1))
value_1=None
print("id of value_1:", id(value_1))