#%% importing CSV folder in a dictionary
import csv

with open('property-listing.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        print(f'\t{row["address"]} loacted at {row["area"]} , and is in the {row["town"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
