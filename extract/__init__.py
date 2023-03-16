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


#Ticket 4: Capitalise user name fields
def get_formatted_input(inputarray):
    
    format_array = [inputarray[0]] + [[i[j][0].upper() + i[j][1:] if j in [1,2] else i[j] for j in range(len(i))] for i in inputarray[1:]]
    
    return format_array


#Ticket 5: Validate responses to answer_3, accept only answers within range of 1 to 10
def validate_third_answer(inputarray):
    
    validated_array = [inputarray[0]] + [i for i in inputarray[1:] if 1 <= int(i[5]) <= 10]
    
    return validated_array