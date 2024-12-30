import os
import argparse
import pandas as pd

def main(input_data_path, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the validation output file
    with open(input_data_path, 'r') as input_file:
        data = input_file.read()

    # Split the data into individual file contents
    file_contents = data.split(',')

    # Create a DataFrame with each file content as a row
    df = pd.DataFrame({
        'file_content': file_contents
    })

    # Save the DataFrame to a CSV file in the output directory
    output_file_path = os.path.join(output_dir, 'inference_results.csv')
    df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inference component")
    parser.add_argument("--input_data_path", type=str, help="Path to the input data file", required=True)
    parser.add_argument("--output_dir", type=str, help="Path to the output directory", required=True)
    args = parser.parse_args()
    main(args.input_data_path, args.output_dir)