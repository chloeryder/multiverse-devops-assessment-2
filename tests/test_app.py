import os.path
from survey_app.extract import get_input, get_cleaned_input, get_formatted_input, validate_third_answer, get_output_file

#Ticket 1
def test_input_is_list():
   
    filename = 'survey_app/results.csv'
    expected_output = list     

    output = get_input(filename)

    assert type(output) == expected_output

#Ticket 1 
def test_input_is_correct():
    
    filename = 'survey_app/results.csv'
    expected_first_line = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    expected_row_count = 25

    output = get_input(filename)
    output_first_line = output[0]
    output_row_count = len(output[1:])

    assert output_first_line == expected_first_line
    assert output_row_count == expected_row_count

#Ticket 2 & 3
def test_duplicates_removed():
  
    filename = 'survey_app/results.csv'  
    initial_input = get_input(filename)
    cleaned_input = get_cleaned_input(initial_input)
    expected_row_count = 20
    expected_value_of_answer_3_for_user_id_6 = 6

    cleaned_input_row_count = len(cleaned_input[1:])

    #Check number of rows after duplicates and empty lines have been removed             
    assert cleaned_input_row_count == expected_row_count  
    
    #Check example to assert that first occurrence of any duplicated records is retained
    for i in cleaned_input:
        if i[0] == 6:
            assert i[5] == expected_value_of_answer_3_for_user_id_6     

#Ticket 4
def test_format():
    filename = 'survey_app/results.csv'
    initials_list = []
    output = get_formatted_input(get_cleaned_input(get_input(filename)))

    #Get list of initials for each entry in name fields 
    for row in output[1:]:
        for i in [1,2]:
            initials_list.append(row[i][0])
    
    #Check that all initials in list are upper-case
    assert all([initial.isupper() for initial in initials_list])

#Ticket 5
def test_validate_third_answer():
    filename = 'survey_app/results.csv'
    output = validate_third_answer(get_formatted_input(get_cleaned_input(get_input(filename))))
   
    #Check that all answer-3 values are between 1 and 10
    for row in output[1:]:
        assert 1 <= int(row[5]) <= 10

#Ticket 6
def test_output_file_exists():
    
    filename = 'survey_app/results.csv'
    output_array = validate_third_answer(get_formatted_input(get_cleaned_input(get_input(filename))))
    get_output_file(output_array)

    #Assert that clean_results.csv file exists
    assert os.path.isfile('clean_results.csv')


