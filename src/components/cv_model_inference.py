import os
import argparse
from utils.functions import utils_fun
from utils.constants import UTILS_CONST
from utils.prompts import UTILS_PROMPT

def main(input_data_path, output_dir):
    
    print("Running model inference...")
    print(UTILS_CONST)
    print(UTILS_PROMPT)
    utils_fun()

if __name__ == "__main__":
    main()