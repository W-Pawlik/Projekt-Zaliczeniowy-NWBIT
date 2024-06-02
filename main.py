import argparse
import sys
import json
import yaml
import xmltodict
import xml.dom.minidom

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
            sys.exit(1)

def save_yaml(data, output_file):
    with open(output_file, 'w') as f:
        yaml.dump(data, f)

def load_xml(input_file):
    with open(input_file, 'r') as f:
        xml_data = f.read()
        try:
            data = xmltodict.parse(xml_data)
            return data
        except Exception as e:
            print("XML parsing error: ", e)
            sys.exit(1)

def save_xml(data, output_file):
    try:
        xml_string = xmltodict.unparse(data, pretty=True)
        dom = xml.dom.minidom.parseString(xml_string)
        formatted_xml = dom.toprettyxml(indent="    ")

        with open(output_file, 'w') as f:
            f.write(formatted_xml)
    except Exception as e:
        print("XML save error: ", e)
        sys.exit(1)


if __name__ == '__main__':
    args = parse_args()
    input_file = args.input_file
    output_file = args.output_file

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)        
    else:
        print("This format of input file is unsupported")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
        save_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        save_xml(data, output_file)
    else:
        print("This format of output file is unsupported")
        sys.exit(1)