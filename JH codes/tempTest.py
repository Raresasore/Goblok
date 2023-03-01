# -*- coding: utf-8 -*-
#%%  turning attributes into criteria
attributes_list = []
file = open("property-attributes.txt", "r")
for each in file:
    attributes_list.append(each.strip())
attributes_list = attributes_list[1:3] + attributes_list[4:]
file.close()
attributes = []
for each in attributes_list:
    attributes.append(each[2:])
str= attributes[-1][1:]
attributes.pop(-1)
attributes.append(str)
attributes_key = ["A","B","C","D","E","F","G","H"]
attributes_value = attributes
my_dict = {}
for i in range(len(attributes_key)):
    my_dict[attributes_key[i]] = attributes_value[i]

#%% dictionaries

#%%  getting user input of what criteria they want
while True:
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    
    user_choices = input('Please select one or more property criteria of your choice (type "all" for all options):').split(",")
    user_choices = [choice.upper().strip() for choice in user_choices]  # Convert each choice to upper case and strip any whitespace
    
    valid_choices = []
    chosen_criteria = []
    
    for choice in user_choices:
        if choice == "ALL":
            valid_choices = list(my_dict.keys())
            break
        elif choice in my_dict.keys() and choice not in valid_choices:
            valid_choices.append(choice)
        else:  # If the user entered an invalid input
            print(f"Invalid input: {choice}. Please enter a valid property criteria.")
            valid_choices = []  # Reset valid_choices to force the user to input again
            break  # Exit the loop if any invalid input is detected    
    if valid_choices:
        print("You chose the following property criteria:")
        for choice in valid_choices:
            print(f" - {choice}: {my_dict[choice]}")
        
        chosen_criteria += valid_choices
        
        confirm = input("Are these all the property criteria you want? If not you can renter your selection again or quit the program (y/n/q):  ")
        if confirm.lower() == "y":
            print("Thank you for confirming your choices.")
            break
        elif confirm.lower() == "n":
            print("Please try again and select the criteria again.")
            continue
        elif confirm.lower() == "q":  # Check if the user wants to quit
            print("Thank you for using this program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter y, n or q")
            
print("You chose the following property criteria:")
for choice in chosen_criteria:
    print(f" - {choice}: {my_dict[choice]}")
    
#%% DISPLAY CHOSEN CRITERIA OPTIONS
ind = 0
def criteria_options(ind):
    headers = ['Option']
    headers.append(attributes_value[ind].title())
    print(f'''Here is a list of {headers[ind+1]}'s available for your property: ''')
    print('{:<15}{}'.format(*headers))
    print('-' * 25)
    unique_set = set(listing_dict[headers[ind+1].lower()])
    unique_list = list(unique_set)
    index = []
    for i in range(1,len(unique_list)+1):
        index.append(i)
    for j in range(len(unique_list)):
        print(f"{index[j]:<15} {unique_list[j]}") 
        
    option = input("Please input one or more property numbers separated by commas: ").split(",")
    option = [int(choice.strip()) for choice in option]  # Convert each choice to int and strip any whitespace
    #criteria values are in area_choices
    print("You selected the following areas:")
    for choice in option:
        print(f" - {listing_dict[headers[ind+1].lower()][choice-1]}")

    else:
        pass


def option_selectionABC():
    if "A" in chosen_criteria:
      criteria_options(0)
    elif ["A","B"] in chosen_criteria:
      criteria_options(0)
      criteria_options(1)
    elif ["A","B","C"] in chosen_criteria:
      criteria_options(0)
      criteria_options(1)
      criteria_options(2)
        
      
    else:
        pass

option_selectionABC()