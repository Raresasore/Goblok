#%% CREATING FUNCTION FOR USER DETAIL COLLECTION
global name
global age
global marital_status
global income

def user_input_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
def start():
    print("Welcome to your very own property search program!\n")
    while True:
        name = input("Hi! What is your name?\n Name:")
        if not all(c.isalpha() or c.isspace() for c in name):
            print("Invalid input. Name can only contain alphabets and spaces.")
            continue
        age = user_input_int(f"Hi {name}! What is your age?")
        if age > 122:
            print("Invalid input. Age cannot be greater than 122.")
            continue
        while True:
            marital_status = user_input_int(f"Dear {name}, is your marital status currently \n [1] Single \n [2] Married \n Your reply:")
            if marital_status not in [1, 2]:
                print("Invalid input. Please enter 1 for Single or 2 for Married.")
            else:
                break
        if marital_status == 2:
            income1 = user_input_int(f"Dear {name}, what is your estimated monthly income after CPF deduction rounded nearest thousands:")
            income2 = user_input_int(f"Dear {name}, what is your spouse's estimated monthly income after CPF deduction rounded nearest thousands:")
            total_income = income1 + income2
        else:
            income1 = user_input_int(f"Dear {name}, what is your estimated monthly income after CPF deduction (rounded to nearest thousand):")
            total_income = income1 // 1000 * 1000
        return name, age, marital_status, total_income


#%% RUNNING USER DETAIL COLLECTION CODE

name, age, marital_status, total_income = start()
print(f"""
------------------------------------------
Hi there {name}, your age is {age}. 
Your marital status is: {'Married' if marital_status == 2 else 'Single'} 
and your income after CPF deduction is: {total_income}.
------------------------------------------
      """)
while True:
    confirm_name = input("Please check If the above details are correct. If not you can renter your selection again or quit the program (y/n/q): ")
    if confirm_name.lower() == "y":
        print("""Thank you for confirming your choices. 
         ~  Welcome to the Property Search Program ~""")
        break
    elif confirm_name.lower() == "n":
        print("Please try again and select the criteria again.")
        continue
    elif confirm_name.lower() == "q":  # Check if the user wants to quit
        print("Thank you for using this program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter y, n or q")




#%% importing CSV folder in a dictionary
# The attributes are arranged in hierarchy from most important to least important
CHOSEN_ATTRIBUTES = ["property_type", "floor_size", "town", "area", "TOP", "bedrooms", "bathroom", "asking_price"]

chosen_criteria = {}
for criteria_option in CHOSEN_ATTRIBUTES:
    chosen_criteria[criteria_option] = False

def readListingTxt():
    raw_prop_list = []
    file = open("property-listing.txt", "r")
    for each in file:
        raw_prop_list.append(each[each.find(":") + 1:].lstrip().rstrip("\n"))
    file.close()

    prop_list = []

    start = 0
    for ind in range(len(raw_prop_list)):
        if "---" in raw_prop_list[ind]:
            # +1 is to ignore the "Property x" attribute
            prop_list.append(raw_prop_list[start + 1 : ind])
            start = ind + 1
            continue
        
    return prop_list

# def readListingCSV():
#     # Read CSV File
#     with open('property-listing.csv', mode='r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         list_of_rows = list(csv_reader)
#     return list_of_rows


list_of_rows = readListingTxt()
    
#%%  turning attributes into criteria
def readAttributesTxt():
    attributes_list = []
    file = open("property-attributes.txt", "r")
    for each in file:
        attributes_list.append(each.strip())
    file.close()
    attributes = []
    for each in attributes_list:
        attributes.append(each[2:])
    str= attributes[-1][1:]
    attributes.pop(-1)
    attributes.append(str)
    attributes_value = attributes
    my_dict = {}
    for i in range(len(attributes_value)):
        my_dict[attributes_value[i]] = i
    return my_dict

attributes_dict = readAttributesTxt()

#%%  getting user input of what criteria they want
while True:
    for x in range(len(CHOSEN_ATTRIBUTES)):
        print(f"{x + 1}: {CHOSEN_ATTRIBUTES[x]}")
    
    user_choices = input('Please select one or more property criteria of your choice (type "all" for all options):').split(",")

    # user choice is based on the position in the CHOSEN_ATTRIBUTE
    user_choices = [int(choice.upper().strip()) - 1 for choice in user_choices]  # Convert each choice to upper case and strip any whitespace
    
    valid_choices = []
    
    for choice in user_choices:
        # TODO Fix option "All" bug
        if choice == "ALL":
            for key in chosen_criteria.keys():
                chosen_criteria[key] = True
            valid_choices += CHOSEN_ATTRIBUTES.keys()
            break

        elif CHOSEN_ATTRIBUTES[choice] in chosen_criteria.keys() and choice not in valid_choices:
            valid_choices.append(choice)

        else:  # If the user entered an invalid input
            print(f"Invalid input: {choice + 1}. Please enter a valid property criteria.")
            valid_choices = []  # Reset valid_choices to force the user to input again
            break  # Exit the loop if any invalid input is detected    

    if valid_choices:
        print("You chose the following property criteria:")
        for choice in valid_choices:
            print(f" - {choice + 1}: {CHOSEN_ATTRIBUTES[choice]}")
            chosen_criteria[CHOSEN_ATTRIBUTES[choice]] = True

        
        confirm = input("Are these all the property criteria you want? If not you can renter your selection again or quit the program (y/n/q): ")
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
def criteria_options(attribute, filters):
    print(f'''Here is a list of {attribute}'s available for your property: ''')
    print('{:<15}{}'.format(*["Option", attribute]))
    print('-' * 25)

    counter = 1
    criteria_values = []
    for row in list_of_rows:
        def filtering():
            for filterCriteriaAttribute in filters.keys():
                filterIndex = attributes_dict[filterCriteriaAttribute]
                comparedCriteriaValue = row[filterIndex]
                individualFound = False
                for filterValues in filters[filterCriteriaAttribute]:
                    if (filterValues == comparedCriteriaValue):
                        individualFound = True
                        break
                if (individualFound == False):
                    return False
            return True
        
        if(filtering() == False):
            continue
        
        criteria_value = row[attributes_dict[attribute]]
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
    print(f'''You selected the following {attribute}:''')
    choice_values = []
    for choice in options:
        choice_value = criteria_values[choice - 1]
        print(f''' - {choice_value}''')
        choice_values.append(choice_value)
    filters[attribute] = choice_values
    return filters


def option_selection():
    filters = {}
    for criteria_attribute in CHOSEN_ATTRIBUTES:
        if (chosen_criteria[criteria_attribute]):
            filters = criteria_options(criteria_attribute, filters=filters)
            
while True:
    option_selection()





