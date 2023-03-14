#Ticket 1: Read a CSV file - read each line of input file into a new array item
def get_input(filename):
    rows = []
    with open(filename,"r") as f:
        for line in f.readlines():
            rows.append(line.strip().split(","))
            
    return rows   