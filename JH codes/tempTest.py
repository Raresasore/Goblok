# -*- coding: utf-8 -*-
#%% Dictionary 

prop_list = []
file = open("property-listing.txt", "r")
for each in file:
    prop_list.append(each.strip())
file.close()

listing_points= []
i = 0
for i in range(11):
   for j in range(7):
       listing_points.append(prop_list[i])
       i += 12

listing_value = [listing_points[7:14],listing_points[14:21],listing_points[21:28],listing_points[28:35],listing_points[35:42],listing_points[42:49],listing_points[49:56],listing_points[56:63],listing_points[63:70],listing_points[70:77]]


for each in listing_value:
    for i in range(7):
        each[i] = each[i][each[i].find(':')+1:].lstrip()

complete_list = []
listing_key = []
file = open("property-attributes.txt", "r")
for each in file:
    complete_list.append(each.strip())
file.close()
for each in complete_list:
    listing_key.append(each)
for i in range(len(listing_key)):
    listing_key[i] = listing_key[i][listing_key[i].find('.')+1:].lstrip()



 #%% importing CSV folder in a dictionary
import csv

with open('property-listing.csv', mode='r') as csv_file:
CRITERIA_HIEARCHY = [3, 4, 2, 1, 5, 6, 7, 8] # Hierarchy when it comes to filtering

chosen_criteria = {}
for criteria_option in CRITERIA_HIEARCHY:
    chosen_criteria[criteria_option] = False

# Read CSV File
with open('./property-listing.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    list_of_rows = list(csv_reader)
    print(list_of_rows)
    
    row_number = 2
    col_number = 3
    value = list_of_rows[row_number - 1][col_number - 1]
    print('area is at:', value)

    
#%%  turning attributes into criteria

@ -26,7 +28,7 @@ for each in attributes_list:
str= attributes[-1][1:]
attributes.pop(-1)
attributes.append(str)
attributes_key = ["A","B","C","D","E","F","G","H"]
attributes_key = [1,2,3,4,5,6,7,8]
attributes_value = attributes
my_dict = {}
for i in range(len(attributes_key)):
@ -38,17 +40,18 @@ while True:
        print(f"{key}: {value}")
    
    user_choices = input('Please select one or more property criteria of your choice (type "all" for all options):').split(",")
    user_choices = [choice.upper().strip() for choice in user_choices]  # Convert each choice to upper case and strip any whitespace
    user_choices = [int(choice.upper().strip()) for choice in user_choices]  # Convert each choice to upper case and strip any whitespace
    
    valid_choices = []
    chosen_criteria = []
    
    for choice in user_choices:
        if choice == "ALL":
            valid_choices = list(my_dict.keys())
            for key in chosen_criteria.keys():
                chosen_criteria[key] = True
            valid_choices += my_dict.keys()
            break
        elif choice in my_dict.keys() and choice not in valid_choices:
            valid_choices.append(choice)
            valid_choices.append(int(choice))
        else:  # If the user entered an invalid input
            print(f"Invalid input: {choice}. Please enter a valid property criteria.")
            valid_choices = []  # Reset valid_choices to force the user to input again
@ -57,8 +60,8 @@ while True:
        print("You chose the following property criteria:")
        for choice in valid_choices:
            print(f" - {choice}: {my_dict[choice]}")
        
        chosen_criteria += valid_choices
            chosen_criteria[choice] = True

        
        confirm = input("Are these all the property criteria you want? If not you can renter your selection again or quit the program (y/n/q):  ")
        if confirm.lower() == "y":
@ -72,44 +75,66 @@ while True:
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
def criteria_options(ind, filters):
    ind_criteria = my_dict.get(ind)

    print(f'''Here is a list of {ind_criteria}'s available for your property: ''')
    print('{:<15}{}'.format(*["Option", ind_criteria]))
    print('-' * 25)
    index = []
    for i in range(1,len()+1):
        index.append(i)
    for j in range(len()):
        print(f"{index[j]:<15} {list_of_rows[j]}") 

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
        
    option = input("Please input one or more property numbers separated by commas: ").split(",")
    option = [int(choice.strip()) for choice in option]  # Convert each choice to int and strip any whitespace
    #criteria values are in area_choices
    print("You selected the following areas:")
    for choice in option:
        print(f" - {csv_reader[headers[ind+1].lower()][choice-1]}")
        if(filtering() == False):
            continue
        
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

option_selectionABC()
option_selection()
