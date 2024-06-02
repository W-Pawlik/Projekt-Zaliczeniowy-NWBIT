import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="File format converter")
    parser.add_argument("input_file", help="Path to input file")
    parser.add_argument("output_file", help="Path to output file")

    if len(sys.argv) != 3:
        print("Wrong count of arguments! Two args are required!")
        sys.exit(1)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    input_file = args.input_file
    output_file = args.output_file
    print(f"Input file: {input_file}")
    print(f"Input file: {output_file}")
