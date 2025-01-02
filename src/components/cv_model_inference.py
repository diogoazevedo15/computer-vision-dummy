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

    input_dir = args.input_url
    output_dir = args.output_url

    print("Running model inference...")
    print(UTILS_CONST)
    print(UTILS_PROMPT)
    utils_fun()
    print(f'Input dir: {input_dir}')
    print(f'Output dir: {output_dir}')

    with open((Path(args.output_dir) / "inference.txt"), "a") as f:
        f.write("Inference step ran successfully")

if __name__ == "__main__":
    main()