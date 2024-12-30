import os
import argparse
from utils.functions import utils_fun
from utils.constants import UTILS_CONST
from utils.prompts import UTILS_PROMPT

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data_path', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    args = parser.parse_args()

    input_data_path = args.input_data_path
    output_dir = args.output_dir

    print("Running model inference...")
    print(f"Input data path: {input_data_path}")
    print(UTILS_CONST)
    print(UTILS_PROMPT)
    utils_fun()

    print(f"Output directory: {input_data_path}")
    print(f"Output directory: {output_dir}")

if __name__ == "__main__":
    main()