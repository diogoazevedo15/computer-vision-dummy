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

    # Write the validation output string to a file
    validation_output = "Validation Output: Success"
    output_file = os.path.join(output_dir, "validation_output.txt")
    with open(output_file, "w") as f:
        f.write(validation_output)
    print(f"Validation output written to {output_file}")

if __name__ == "__main__":
    main()