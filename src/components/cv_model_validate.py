import os
import argparse
from src.utils.functions import log_message, read_files_from_directory
from src.utils.constants import LOG_FILE_NAME, VALIDATION_SUCCESS_MESSAGE

def main(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create log file in the output directory
    log_file_path = os.path.join(output_dir, LOG_FILE_NAME)
    log_message(VALIDATION_SUCCESS_MESSAGE, log_file_path)

    # Read and collect contents of all files in the input directory
    file_contents = read_files_from_directory(input_dir)

    # Create a single string output with file contents separated by commas
    output_data = ','.join(file_contents)

    # Save the output data to a file for the next component to consume
    output_file_path = os.path.join(output_dir, 'validation_output.txt')
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validation component")
    parser.add_argument("--input_dir", type=str, help="Path to the input directory", required=True)
    parser.add_argument("--output_dir", type=str, help="Path to the output directory", required=True)
    args = parser.parse_args()
    main(args.input_dir, args.output_dir)