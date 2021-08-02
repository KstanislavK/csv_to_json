import csv
import json
import sys

csv_file = sys.argv[1]

json_file = f'{csv_file[(csv_file.rfind("/") + 1):csv_file.rfind(".")]}.json'
csv_rows = []


def read_csv(c_file, j_file):
    with open(c_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        titles = reader.fieldnames
        for row in reader:
            line = {}
            for i in range(len(titles)):
                line[titles[i]] = row[titles[i]]
            csv_rows.append(line)
        write_json(csv_rows, j_file)


def write_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        new_file = json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
        f.write(new_file)


read_csv(csv_file, json_file)
