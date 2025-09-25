"""
Use .tsv instead of .csv as importing a CSV fundamentally messes up the data.
There are commas in the sizing already, hence we use tabs ask our delimiter here.

Also, I'm NOT doing complexity analysis for this. I'm lazy, and its not my assignment.
Either way no special data structures are used other than the basic python data structures,
i.e. lists, tuples, dictionaries, hence most of the operations aren't fully optimized,
resulting in O(N) or O(N^2). Other than that, everything works as intended, unless it doesn't
so submit a bug report or send me a message or go ahead and make a copy of the file to debug.

Buh-bye.

Author: Ethan Lim Dao-Cheng
Version: 1.0 
"""

import datetime
from typing import Tuple

# Merchandise Quantity for Each Size
cotton = {
    "S": 0,
    "M": 0,
    "L": 0,
    "XL": 0,
    "2XL": 0,
    "3XL": 0
}
dri_fit = {
    "2XS": 0,
    "XS": 0,
    "S": 0,
    "M": 0,
    "L": 0,
    "XL": 0,
    "2XL": 0,
    "3XL": 0,
    "5XL": 0,
    "7XL": 0
}
towels = 0

# All merchandise in a list to simplify...
merch_overall_data = [cotton, dri_fit, towels]

def file_reader(filename: str) -> None:
    """
    Function to read the merch data in both .csv and .tsv format, but do use .tsv files as there are
    commas in the data itself, resulting in inconsistent column data.
    
    Input:
        filename: str - Name of the file to read
        
    Output:
        None
    """
    
    # Determines whether the filename is a .csv or .tsv
    if filename[-3] == "c":
        delimiter = ","
    else:
        delimiter = "\t"
    
    # Opens the file and extracts the header and data separately
    with open(filename, "r") as file:
        header = file.readline().strip().split(delimiter)
        data = []
        
        for line in file:
            line = line.strip()
            cols = line.split(delimiter)
            
            data.append(cols)
    
    return (header, data)


def update_merch_data(single_merch_order: str, merch_index: int) -> None:
    """
    Updates the amount of merch needed to purchase based on the previously extracted data.
    Yes, I could have made it easier by making a helper function but nah.
    
    Input:
        single_merch_order: str - order to consider, the "row" in the .csv file
        merch_index: int - current merch item to look at, i.e. Cotton, Dri-Fit, Towel
    
    Output:
        None
    """
    
    # Early exit condition if the customer did not order a merch item.
    if single_merch_order == "Not applicable.":
        return
    
    multiple_sizes = False
    merch = merch_overall_data[merch_index]
    
    # Finds if in the current order for the merch, the customer has selected multiple sizes
    if "," in single_merch_order:
        # Turns the order into a list of strings following the pattern "Size(Quantity)"
        order_for_merch = single_merch_order.strip().split(", ")
        multiple_sizes = True
    
    # Analyze each size and quantity if there were multiple sizes in the order
    if multiple_sizes:
        # Iterate to analyze sizes and quantity of each size, then add it to the total merchandise quantity of that item
        for order in order_for_merch:
            current_size, current_qty = analyze_size_and_quantity(order)
            add_qty_to_size(current_size, current_qty, merch)
    
    # If the order was just a single size, perform same operations as above but without the for loop.
    else:
        current_size, current_qty = analyze_size_and_quantity(single_merch_order)
        add_qty_to_size(current_size, current_qty, merch)
  
        

def analyze_size_and_quantity(unformatted_string: str) -> Tuple[str, int]:
    """
    Based on the given format by the regular expression, extract the size and quantity of the order
    
    Input:
        unformatted_string: str - String representation of the Size(Quantity) from the regular expression
    
    Output:
        (size, quantity): Tuple[str, int] - Tuple output of the string and integer values of the size and quantity
    """
    
    size, qty = unformatted_string.split("(") # Split by the opening bracket to separate size and quantity
    qty = int(qty.removesuffix(")")) # Remove the closing bracket from the quantity and convert to integer
    
    return size, qty


def add_qty_to_size(size: str, qty: int, merch_to_add: dict) -> None:
    """
    Based on the merch item, add the quantity to that item's size.
    
    Input:
        size: str - Size to be added to
        qty: int - Amount of items of that size to add
        merch_to_add: dict - Merch to add
        
    Output:
        None
    """
    
    merch_to_add[size] += qty
    
        
def csv_writer(merch: dict , filename: str) -> str:
    """
    Writes a .csv file to export with the sizes and quantities of a certain merch item.
    
    Input:
        merch: dict - Updated merch data to export to .csv
        filename: str - Name of the file to be written
        
    Output:
        return_message: str - Success message of writing the .csv file
    """
    
    filename += ".csv" # Appends the .csv extension/suffix to the filename.
    return_message = f"Sucessfully written {filename}."
        
    # Create a file to write to...
    with open(filename, "w") as file:
        # Write header columns
        file.write("Size,Quantity\n")
        
        # Write out the size and quantity required to order separated by a comma (.csv delimiter)
        for key in merch.keys():
            file.write(f"{key},{merch[key]}\n")
    
    return return_message
    
    
def csv_generator(merch: dict | int) -> None:
    """
    Generates all the export .csv files required, excluding towels because it's just 1 line smh
    are you that lazy D:<
    
    Input:
        merch: dict | int - Merch to consider for export
        
    Output:
        None
    """
    
    # Retrieve current time to append as a suffix to the export files required
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    # Write a .csv file if the merchandise considered is a dictionary type (i.e. Cotton, Dri-Fit)
    if isinstance(merch, dict):
        
        # Generate export file for cotton shirts
        if len(merch.keys()) == 6:
            file = f"cotton_statistics - {timestamp}"
            print(csv_writer(cotton, file))
        
        # Generate export file for dri-fit shirts
        elif len(merch.keys()) == 10:
            file = f"dri_fit_statistics - {timestamp}"
            print(csv_writer(dri_fit, file))
    
    # No love (.csv file) for towels </3
    else:
        print("\ni'm not making a csv with 1 line. towel data:")
        print(f"Towels: {towels}\n") # you get the numbers though lol
    
    
def print_merch_data(merch: str, data: dict) -> None:
    """
    Print out data of the selected merch item (shirts only).
    
    Input:
        merch: str - Name of the merch item
        data: dict - Dictionary storing the merch data
        
    Output:
        None
    """
    
    # Get the sizes of the merch (shirt) chosen
    keys = data.keys()
    
    # Print out the data for each size
    print(f"{merch} Data")
    for key in keys:
        print(f"    {key}: {data[key]}")
    print("===========================")


def print_statistics() -> None:
    """
    Print out overall statistics of each merch, including quantity ordered for each size.
    
    Input:
        None
    
    Output:
        None
    """
    
    counter = 0
    
    print("")
    print("===========================")
    
    # Print out all merch (I used a while loop cuz why not lol)
    while counter <= (len(merch_overall_data) - 1):
        if isinstance(merch_overall_data[counter], dict):
            current_data: dict = merch_overall_data[counter]
        else:
            current_data: int = merch_overall_data[counter] 
        
        if counter == 0:
            print_merch_data("Cotton T-Shirt", current_data)
            
        elif counter == 1:
            print_merch_data("Dri-Fit T-Shirt", current_data) 
            
        else:  
            print(f"Towels: {current_data}") 
            print("===========================")
            
        counter += 1            
            
if __name__ == "__main__":
    # csv = input("Enter the file you would like to analyze: ").strip()
    # headers, data = file_reader(csv)
    headers, data = file_reader("merch-data-sample.tsv")
    
    for order in data:
        for col in range(len(headers)):
            if col in (0, 1):
                current_merch = merch_overall_data[col]
                current_order: str = order[col]
                
                update_merch_data(current_order, col)
        
            elif col == 2 and order[col] != "Not applicable.":
                merch_overall_data[col] += int(order[col])
            
    print_statistics()
    
    for merch in merch_overall_data:
        csv_generator(merch)
    
    print("Finished writing csv files.")
            
            