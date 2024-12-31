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

    input_data_path = args.input_data_path
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    print("Running model inference...")
    print(f"Input data path: {input_data_path}")
    print(UTILS_CONST)
    print(UTILS_PROMPT)
    utils_fun()

    # Read the validation output string from the file
    input_file = os.path.join(input_data_path, "validation_output.txt")
    with open(input_file, "r") as f:
        validation_output = f.read()
    print(f"Validation output received: {validation_output}")


if __name__ == "__main__":
    main()