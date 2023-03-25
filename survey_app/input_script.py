
import sys
from extract import get_input, get_cleaned_input, get_formatted_input, validate_third_answer, get_output_file, print_final_output

def main():
    
    filename = './survey-app/results.csv'

    input_list = get_input(filename)
    cleaned_list = get_cleaned_input(input_list)
    formatted_list = get_formatted_input(cleaned_list)
    validated_list = validate_third_answer(formatted_list)
    
    get_output_file(validated_list) 
    
      
if __name__ == '__main__':
    sys.exit(main())

