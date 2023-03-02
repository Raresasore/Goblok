def summarise(data_list, attribute_mapping_dict, user_choice_dict):
    # Sorting
    output_sort = {}
    for chosen_attribute in user_choice_dict:
        print(f'''{chosen_attribute}:''', end= " ")
        for value in user_choice_dict[chosen_attribute]:
            print(f'''{value}''', end= " ")
            for index in range(len(data_list)):
                data = data_list[index]
                compareAttribute = data[attribute_mapping_dict[chosen_attribute]]
                # Assign a ranking number to each row depending on what matches the user input

                # Fix the checkmark and cross problem
                if (compareAttribute == value):
                    output_sort[index] = output_sort[index] + 1 if output_sort.get(index) else 1
                    data_list[index][attribute_mapping_dict[chosen_attribute]] = str(compareAttribute) + "✔"
                else:
                    output_sort[index] = output_sort[index] if output_sort.get(index) else 0 
                    data_list[index][attribute_mapping_dict[chosen_attribute]] = str(compareAttribute) + "✖"
    print("\n")
    output_list = []
    # Create x number of array matching the number items in user_choice_dict
    for _ in range(len(user_choice_dict.keys())+1):
        output_list.append([])
    for key in output_sort.keys():
        row = data_list[key]
        output_list[output_sort[key]].append(row)
  
    for x in output_list[::-1]:
      print(x)

    # for columnIndex in range(len(attribute_mapping_dict)):
    #     print(columnIndex)