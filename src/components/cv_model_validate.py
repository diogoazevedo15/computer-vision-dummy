def main():
    import os
    import argparse
    from utils.functions import utils_fun
    from utils.constants import UTILS_CONST
    from utils.prompts import UTILS_PROMPT

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    print("Running model validation...")
    print(UTILS_CONST)
    print(UTILS_PROMPT)
    utils_fun()

    # Define the output string
    output_string = "Model validation completed successfully."

    # Write the string to a file in the output directory
    output_file_path = os.path.join(output_dir, 'validation_output.txt')
    with open(output_file_path, 'w') as f:
        f.write(output_string)

if __name__ == "__main__":
    main()