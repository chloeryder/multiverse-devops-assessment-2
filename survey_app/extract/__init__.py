#Ticket 1: Read a CSV file - read each line of input file into a new array item
def get_input(filename):
    rows = []
    with open(filename,"r") as f:
        for line in f.readlines():
            rows.append(line.strip().split(","))
            
    return rows   

#Ticket 2: Remove duplicate entries (retain first entry where duplicates are found)
#Ticket 3: Ignore empty lines 
def get_cleaned_input(inputarray):
    user_list = []
    output_array = []
    
    for row in inputarray:
        if not any(row):                   #Ignore empty lines 
            continue
        if row[0] not in user_list:        #Ignore duplicates
            user_list.append(row[0])
            output_array.append(row)
    
    return output_array


#Ticket 4: Capitalise user name fields
def get_formatted_input(inputarray):
    
    #Use upper function on first letter of each name entry to retain bicapitalisation e.g. mcDonald --> McDonald
    format_array = [inputarray[0]] + [[row[item][0].upper() + row[item][1:] if item in [1,2] else row[item] for item in range(len(row))] for row in inputarray[1:]]
    
    return format_array


#Ticket 5: Validate responses to answer_3, accept only answers within range of 1 to 10
def validate_third_answer(inputarray):
    
    validated_array = [inputarray[0]] + [row for row in inputarray[1:] if 1 <= int(row[5]) <= 10]
    
    return validated_array


#Ticket 6: Output the cleansed result data to a new file called clean_results.csv
def get_output_file(inputarray):
    
    with open("clean_results.csv","w") as f:
        for line in inputarray[:-1]:                #Don't add new line character after final row. 
            f.write(','.join(line) + '\n') 
        f.write(','.join(inputarray[-1]))           #Write final row without line break. 
    
    return f


#Ticket 7: Read in the clean_results.csv file and output the results to the command line, row by row.
#Stretch: The printed output will be formatted with fixed length strings. 

#define function to print the final output array to command line:
def print_final_output(final_output):
    
    #get max string length of entries in output array to use as fixed width for formatting.
    max_string_length = max(len(element) for row in final_output for element in row)
    #add a buffer 
    fixed_string_length = max_string_length + 4

    #print each line in output to command line with fixed string length
    for line in final_output:
        print ([f'{item:<{fixed_string_length}}' for item in line])
