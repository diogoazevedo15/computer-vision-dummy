def main():
    import argparse
    from pathlib import Path
    from utils.functions import utils_fun
    from utils.constants import UTILS_CONST
    from utils.prompts import UTILS_PROMPT

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_url', type=str, required=True)
    parser.add_argument('--output_url', type=str, required=True)
    args = parser.parse_args()


    print("Running model validation...")
    print(UTILS_CONST)
    print(UTILS_PROMPT)
    utils_fun()
    print(f'Input dir: {args.input_url}')
    print(f'Output dir: {args.output_url}')

    with open((Path(args.output_url) / "validate.txt"), "a") as f:
        f.write("Validation step ran successfully")


    print('hello')
if __name__ == "__main__":
    main()