import argparse
from data_loader import load_csv_files
from reports.average_gdp import generate_average_gdp_report
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument('--files', nargs='+', required=True)
parser.add_argument('--report', required=True)
args = parser.parse_args()

if args.report != 'average-gdp':
    raise ValueError(f"Неизвестный отчет: {args.report}")

data = load_csv_files(args.files)
result = generate_average_gdp_report(data)
print(tabulate(result, headers="keys", tablefmt="grid", floatfmt=".2f"))


