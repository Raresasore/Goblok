# data_list = List of row list - Each row is a property
# attribute_mapping_dict = {fieldKey: indexNumber} - Tied to the positioning of data in a row list
# user_choice_dict = {fieldKey: [data]}

def summarise(data_list, attribute_mapping_dict, user_choice_dict):
    # Sorting
    output_sort = {}
    print("You have chosen to find properties that matches the following criteria(s)")
    for chosen_attribute in user_choice_dict:
        print(f'''{chosen_attribute}:''', end= " ")
        for value in user_choice_dict[chosen_attribute]:
            print(f'''{value}''', end= ",")
            # marked = False
            for index in range(len(data_list)):
                data = data_list[index]
                compareAttribute = str(data[attribute_mapping_dict[chosen_attribute]])
                # Assign a ranking number to each row depending on what matches the user input

                # add = ""
                if (compareAttribute == str(value)):
                    output_sort[index] = output_sort[index] + 1 if output_sort.get(index) else 1
                    # add = "✔"
                else:
                    output_sort[index] = output_sort[index] if output_sort.get(index) else 0
                #     add = "✖"
                    
                # if (marked == False):
                #     data_list[index][attribute_mapping_dict[chosen_attribute]] = compareAttribute + add
                #     marked = True
        print("\n")
    output_list = []
    # Create x number of array matching the number items in user_choice_dict
    for _ in range(len(user_choice_dict.keys())+1):
        output_list.append([])
    for key in output_sort.keys():
        # Filter out properties that do not fit any criteria
        if (output_sort[key] == 0):
            continue

        row = data_list[key]
        output_list[output_sort[key]].append(row)

    big_fields = ["address"]
    big_fields_width = 40
    default_fields_width = 20
    def printSummary(attribute, default_fields_width, big_fields, big_fields_width):
        width = default_fields_width
        for big_field in big_fields:
            if (big_field == attribute):
                width = big_fields_width
                break
        format_row = "{:<{width}}"
        print(format_row.format(attribute, width=width), end=" | ")

    print("Here are the list of all properties sorted according to the matching")
    for attribute in attribute_mapping_dict.keys():
        printSummary(attribute, default_fields_width, big_fields, big_fields_width)
    print("\n")

    for ranked in output_list[::-1]:
      for property in ranked:
        for property_attribute in property:
            printSummary(property_attribute, default_fields_width, big_fields, big_fields_width)
        print("\n")

