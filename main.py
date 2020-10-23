#!/usr/bin/python3.8

import csv

def write_csv(header, rows, output):
    """
    A utility function to write csv file.
    Takes header list, rows list and output directory name as argument 
    creates a csv file at output location with given attributes.
    """
    try: 
        with open(output, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header
            csv_writer.writerow(header)

            csv_writer.writerows(rows)
        print(output)
        print("File write complete\n")
    except:
        print("An exception has occured")
    
def filter_country():
    """
    The function reads the input csv file from input folder 
    and filters records which have country "USA".
    These records are stored in a file called "filteredCountry.csv"
    saved in the output folder.
    """
    input_file = "input/main.csv"
    output_file = "output/filteredCountry.csv"
    fields = []
    col = 8                 # Index of country column in csv file
    with open(input_file) as f:
        csv_reader = csv.reader(f)
        fields = next(csv_reader)
        results = []
        for row in csv_reader:
            if "USA" in row[col][:3]:
                results.append(row)
        print("Writing USA filtered csv file")
        write_csv(fields, results, output_file)

def lowest_price():
    """
    Takes the filtered csv file as input and outputs the file lowestPrice.csv 
    in the output dir with the specified attributes.
    """
    input_file = "output/filteredCountry.csv"
    output_file = "output/lowestPrice.csv"
    header = ["SKU", "FIRST_MINIMUM_PRICE", "SECOND_MINIMUM_PRICE"]
    price_col = 5
    tmp = dict()
    with open(input_file) as f:
        csv_reader = csv.reader(f)
        results = []

        for row in csv_reader:
            try:
                price = float(row[price_col][1::])
                sku = row[0]

                # Adding first minimum price in the dictonary
                if sku not in tmp:
                    tmp[sku] = [price]
                elif sku in tmp:        # Add second minimum
                    if len(tmp[sku]) == 1:
                        tmp[sku].append(price)
                        tmp[sku].sort()
                    else:           # If the second price found is lower than the first
                        if tmp[sku][0] > price:
                            tmp[sku][1], tmp[sku][0] = tmp[sku][0], price
            except:
                pass

        # Write result
        for key, value in tmp.items():
            if len(value) > 1:
                new_row = []
                new_row.append(key)
                new_row.extend(value)
                results.append(new_row)
        print("Writing Lowest prices csv file")
       #output result into csv
        write_csv(header, results, output_file)


filter_country()
lowest_price()

