import sys
from extract import get_input, print_final_output

def output_main():

    final_results = get_input('./clean_results.csv')
    print_final_output(final_results)

if __name__ == '__main__':
    sys.exit(output_main())