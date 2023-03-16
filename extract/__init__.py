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
    
    for i in inputarray:
        if not any(i):                   #Ignore empty lines 
            continue
        if i[0] not in user_list:        #Ignore duplicates
            user_list.append(i[0])
            output_array.append(i)
    
    return output_array

