from extract import get_input

#Ticket 1
def test_input_is_list():
   
    filename = 'results.csv'
    expected_output = list     

    output = get_input(filename)

    assert type(output) == expected_output

#Ticket 1 
def test_input_is_correct():
    
    filename = 'results.csv'
    expected_first_line = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    expected_row_count = 25

    output = get_input(filename)
    output_first_line = output[0]
    output_row_count = len(output[1:])

    assert output_first_line == expected_first_line
    assert output_row_count == expected_row_count