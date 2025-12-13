import os
import argparse

import yaml

parser = argparse.ArgumentParser(
    description="Churn CSV data into yaml.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    "csv_input_filepath", type=str, help="The csv data."
)
parser.add_argument(
    "-o","--output-filepath", type=str, default=None, help="The yaml filepath. If None, merely replaces extension of input filepath."
)

args = parser.parse_args()

if args.output_filepath is None:
    args.output_filepath = f"{os.path.splitext(args.csv_input_filepath)[0]}.yaml"


def gather_csv_contents_as_dicts(csv_filepath):
    dicts = []
    with open(csv_filepath, "r") as fio:
        headers = None
        for line in fio:
            line_parts = line.strip().split(",")
            
            if headers is None:
                headers = line_parts
                continue
            
            dicts.append({
                headers[index]: line_part.strip()
                for index, line_part in enumerate(line_parts[0:len(headers)])
                if len(line_part.strip()) != 0
            })
    return dicts

yaml_contents = gather_csv_contents_as_dicts(args.csv_input_filepath)

with open(args.output_filepath, "w") as fio:
    yaml.dump(yaml_contents, fio)

print(args.output_filepath)