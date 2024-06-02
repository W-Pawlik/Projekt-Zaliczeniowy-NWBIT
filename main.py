import argparse
import sys
import json
import yaml

def parse_args():
    parser = argparse.ArgumentParser(description="File format converter")
    parser.add_argument("input_file", help="Path to input file")
    parser.add_argument("output_file", help="Path to output file")

    if len(sys.argv) != 3:
        print("Wrong count of arguments! Two args are required!")
        sys.exit(1)

    return parser.parse_args()

def load_json(input_file):
    with open(input_file, 'r') as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError as e:
            print("JSON parsing error: ", e)
            sys.exit(1)

def save_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

def load_yaml(input_file):
    with open(input_file, 'r') as f:
        try:
            data = yaml.safe_load(f)
            return data
        except yaml.YAMLError as e:
            print("YAML parsing error: ", e)
            exit(1)

if __name__ == '__main__':
    args = parse_args()
    input_file = args.input_file
    output_file = args.output_file
