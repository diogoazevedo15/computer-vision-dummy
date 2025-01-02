def main():
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

    print("Running model validation...")
    print(UTILS_CONST)
    print(UTILS_PROMPT)
    utils_fun()
    print(f'Input dir: {input_dir}')
    print(f'Output dir: {output_dir}')

if __name__ == "__main__":
    main()