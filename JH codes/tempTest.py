# -*- coding: utf-8 -*-
#%% importing CSV folder in a dictionary
import csv

CRITERIA_HIEARCHY = [3, 4, 2, 1, 5, 6, 7, 8] # Hierarchy when it comes to filtering

chosen_criteria = {}
for criteria_option in CRITERIA_HIEARCHY:
    chosen_criteria[criteria_option] = False

# Read CSV File
with open('./property-listing.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    list_of_rows = list(csv_reader)

    
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
attributes_key = [1,2,3,4,5,6,7,8]
attributes_value = attributes
my_dict = {}
for i in range(len(attributes_key)):
    my_dict[attributes_key[i]] = attributes_value[i]

#%%  getting user input of what criteria they want
while True:
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    
    user_choices = input('Please select one or more property criteria of your choice (type "all" for all options):').split(",")
    user_choices = [int(choice.upper().strip()) for choice in user_choices]  # Convert each choice to upper case and strip any whitespace
    
    valid_choices = []
    
    for choice in user_choices:
        if choice == "ALL":
            for key in chosen_criteria.keys():
                chosen_criteria[key] = True
            valid_choices += my_dict.keys()
            break
        elif choice in my_dict.keys() and choice not in valid_choices:
            valid_choices.append(int(choice))
        else:  # If the user entered an invalid input
            print(f"Invalid input: {choice}. Please enter a valid property criteria.")
            valid_choices = []  # Reset valid_choices to force the user to input again
            break  # Exit the loop if any invalid input is detected    
    if valid_choices:
        print("You chose the following property criteria:")
        for choice in valid_choices:
            print(f" - {choice}: {my_dict[choice]}")
            chosen_criteria[choice] = True

        
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
 
#%% DISPLAY CHOSEN CRITERIA OPTIONS
def criteria_options(ind, filters):
    ind_criteria = my_dict.get(ind)

    print(f'''Here is a list of {ind_criteria}'s available for your property: ''')
    print('{:<15}{}'.format(*["Option", ind_criteria]))
    print('-' * 25)

    counter = 0
    criteria_values = []
    for row in list_of_rows:
        # Ignore first 
        if (counter == 0):
            counter += 1
            continue

        def filtering():
            for filterCriteriaInd in filters.keys():
                comparedCriteriaValue = row[filterCriteriaInd]
                individualFound = False
                for filterValues in filters[filterCriteriaInd]:
                    if (filterValues == comparedCriteriaValue):
                        individualFound = True
                        break
                if (individualFound == False):
                    return False
            return True
        
        if(filtering() == False):
            continue
        
        criteria_value = row[ind]
        if (criteria_value in criteria_values):
            continue
        else:
            criteria_values.append(criteria_value)
        print(f"{counter:<15} {criteria_value}") 
        counter += 1

    user_input_options = input("Please input one or more property numbers separated by commas: ").split(",")
    # TODO Implement User Input Validation
    options = [int(choice.strip()) for choice in user_input_options]  # Convert each choice to int and strip any whitespace
    
    #criteria values are in area_choices
    print(f'''You selected the following {ind_criteria}:''')
    choice_values = []
    for choice in options:
        choice_value = criteria_values[choice - 1]
        print(f''' - {choice_value}''')
        choice_values.append(choice_value)
    filters[ind] = choice_values
    return filters


def option_selection():
    filters = {}
    for criteria_ind in CRITERIA_HIEARCHY:
        if (chosen_criteria[criteria_ind]):
            filters = criteria_options(criteria_ind, filters=filters)
            print(filters)

option_selection()
