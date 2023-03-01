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
property_list = []
file = open("property-listing.txt", "r")
for each in file:
    property_list.append(each.strip())
file.close()
listing_points= []
i = 0
for i in range(11):
   for j in range(7):
       listing_points.append(property_list[i])
       i += 12
listing_dict = {}
listing_value = [listing_points[7:14],listing_points[14:21],listing_points[21:28],listing_points[28:35],listing_points[35:42],listing_points[42:49],listing_points[49:56],listing_points[56:63],listing_points[63:70],listing_points[70:77]]
listing_key = []
attributes_complete_list = []
file = open("property-attributes.txt", "r")
for each in file:
    attributes_complete_list.append(each.strip())
file.close()
for each in attributes_complete_list:
    listing_key.append(each)
for i in range(len(listing_key)):
    listing_key[i] = listing_key[i][listing_key[i].find('.')+1:].lstrip()
for each in listing_value:
    for i in range(7):
        each[i] = each[i][each[i].find(':')+1:].lstrip()
for i in range(len(listing_key)):
    listing_dict[listing_key[i]] = listing_value[i]

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
        
        
    if "B" in chosen_criteria:
        headers = ['Property', 'Town']
        print('''Here is a list of Town's available for your property: ''')
        print('{:<15}{}'.format(*headers))
        print('-' * 25)
        towns = listing_dict['town']
        index = []
        for i in range(1,len(towns)+1):
            index.append(i)
        for i in range(0,7):
            print(f"{index[i]:<15}{listing_dict['town'][i]}") 
            
        town_choices = input("Please input one or more property numbers separated by commas: ").split(",")
        town_choices = [int(choice.strip()) for choice in town_choices]  # Convert each choice to int and strip any whitespace
        #criteria values are in town_choices
        print("You selected the following towns:")
        for choice in town_choices:
            print(f" - {listing_dict['town'][choice-1]}")
    else:
        pass

    if "C" in chosen_criteria:
        headers = ['Property', 'Property_type']
        print('''Here is a list of Property_type's available for your property: ''')
        print('{:<15}{}'.format(*headers))
        print('-' * 25)
        property_type = listing_dict['property_type']
        index = []
        for i in range(1,len(property_type)+1):
            index.append(i)
        for i in range(0,7):
            print(f"{index[i]:<15}{listing_dict['property_type'][i]}") 
            
        property_type_choices = input("Please input one or more property_type numbers separated by commas: ").split(",")
        property_type_choices = [int(choice.strip()) for choice in property_type_choices]  # Convert each choice to int and strip any whitespace
        #criteria values are in town_choices
        print("You selected the following property_type:")
        for choice in property_type_choices:
            print(f" - {listing_dict['property_type'][choice-1]}")
    else:
        pass
    
    if "D" in chosen_criteria:
        headers = ['Property', 'Floor_size']
        print('''Here is a list of Floor_size's available for your property: ''')
        print('{:<15}{}'.format(*headers))
        print('-' * 25)
        floor_size = listing_dict['floor_size']
        index = []
        for i in range(1,len(floor_size)+1):
            index.append(i)
        for i in range(0,7):
            print(f"{index[i]:<15}{listing_dict['floor_size'][i]}") 
            
        floor_size_choices = input("Please input one or more floor_size numbers separated by commas: ").split(",")
        floor_size_choices = [int(choice.strip()) for choice in floor_size_choices]  # Convert each choice to int and strip any whitespace
        #criteria values are in town_choices
        print("You selected the following floor_size:")
        for choice in floor_size_choices:
            print(f" - {listing_dict['floor_size'][choice-1]}")
    else:
        pass

    if "E" in chosen_criteria:
        headers = ['Property', 'TOP']
        print('''Here is a list of TOP's available for your property: ''')
        print('{:<15}{}'.format(*headers))
        print('-' * 25)
        TOP = listing_dict['TOP']
        index = []
        for i in range(1,len(TOP)+1):
            index.append(i)
        for i in range(0,7):
            print(f"{index[i]:<15}{listing_dict['TOP'][i]}") 
            
        TOP_choices = input("Please input one or more TOP numbers separated by commas: ").split(",")
        TOP_choices = [int(choice.strip()) for choice in TOP_choices]  # Convert each choice to int and strip any whitespace
        #criteria values are in town_choices
        print("You selected the following TOP:")
        for choice in TOP_choices:
            print(f" - {listing_dict['TOP'][choice-1]}")
    else:
        pass
    
    if "F" in chosen_criteria:
        headers = ['Property', 'Bedrooms']
        print('''Here is a list of Bedrooms's available for your property: ''')
        print('{:<15}{}'.format(*headers))
        print('-' * 25)
        bedrooms = listing_dict['bedrooms']
        index = []
        for i in range(1,len(bedrooms)+1):
            index.append(i)
        for i in range(0,7):
            print(f"{index[i]:<15}{listing_dict['bedrooms'][i]}") 
            
        bedrooms_choices = input("Please input one or more bedrooms numbers separated by commas: ").split(",")
        bedrooms_choices = [int(choice.strip()) for choice in bedrooms_choices]  # Convert each choice to int and strip any whitespace
        #criteria values are in town_choices
        print("You selected the following bedrooms:")
        for choice in bedrooms_choices:
            print(f" - {listing_dict['bedrooms'][choice-1]}")
    else:
        pass

#%%
if "G" in chosen_criteria:
    headers = ['Property', 'Bathroom']
    print('''Here is a list of Bathroom's available for your property: ''')
    print('{:<15}{}'.format(*headers))
    print('-' * 25)
    bathroom = listing_dict['bathroom']
    index = []
    for i in range(1,len(bathroom)+1):
        index.append(i)
    for i in range(0,1):
        print(f"{index[i]:<15}{listing_dict['bathroom'][i]}") 
        
    bathroom_choices = input("Please input one or more bathroom numbers separated by commas: ").split(",")
    bathroom_choices = [int(choice.strip()) for choice in bathroom_choices]  # Convert each choice to int and strip any whitespace
    #criteria values are in town_choices
    print("You selected the following bathroom:")
    for choice in bathroom_choices:
        print(f" - {listing_dict['bathroom'][choice-1]}")
else:
    pass
#%%  
if "H" in chosen_criteria:
    headers = ['Property', 'Asking_price']
    print('''Here is a list of Asking_price's available for your property: ''')
    print('{:<15}{}'.format(*headers))
    print('-' * 25)
    asking_price = listing_dict['asking_price']
    index = []
    for i in range(1,len(asking_price)+1):
        index.append(i)
    for i in range(0,7):
        print(f"{index[i]:<15}{listing_dict['asking_price'][i]}") 
        
    asking_price_choices = input("Please input one or more asking_price numbers separated by commas: ").split(",")
    asking_price_choices = [int(choice.strip()) for choice in asking_price_choices]  # Convert each choice to int and strip any whitespace
    #criteria values are in town_choices
    print("You selected the following asking_price:")
    for choice in asking_price_choices:
        print(f" - {listing_dict['asking_price'][choice-1]}")
else:
    pass 
#%% Running the function
option_selectionABC()
#%% creating function to store criteria parameters into a list variable for comparison
