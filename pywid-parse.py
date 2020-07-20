#!/usr/bin/env python3

import argparse
import csv

from funcs import *

# If you feel like the code could use any improvements, don't hesitate to send me a
# message and tell me about it!

# Many thanks to the folks at "Our World in Data," without whom this project would
# not be possible. Chek them out!
# https://github.com/owid/covid-19-data/tree/master/public/data


def clean_file(file, fields, sort, output_file, **kwargs):
    data = sort_file(file, *fields, sort=sort, **kwargs)

    with open(output_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()

        for line in data:
            writer.writerow(line)


def parse_args(url, full_fieldnames):
    parser = argparse.ArgumentParser(usage="python3 %(prog)s A [options]",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=f"""All possible (default) fields are:\n{full_fieldnames}\n\n
Recommended sorting methods are:
  date          <yyyy-mm-dd OR 'today'>
  iso_code      <iso>""")

    parser.add_argument("fields", metavar="A", type=str, nargs="+",
                        help = "The fields to be sorted.")

    parser.add_argument("-S", "--sort", metavar=("<type>", "<filter>"), nargs=2, default=("date","today"),
                        help="Sorting method to be used. Default is 'date today.'")

    parser.add_argument("-F", "--file", default=url, metavar="<file>",
                        help="Use a local file instead of the repository.")
    
    parser.add_argument("-W", "--world", action="store_true",
                        help="Include world in results.")

    parser.add_argument("-O", "--output", action="store", default="owid_sipmlified.csv",
                        metavar="<file>", dest="output_file",
                        help="Select name/path for output file.")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    full_fieldnames = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'new_deaths_per_million', 'total_tests', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cvd_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy']

    kwargs = vars(parse_args(url, full_fieldnames))
    
    if kwargs["sort"][1] == "today":
        kwargs["sort"] = [kwargs["sort"][0], str(datetime.date.today())]
        
    print(kwargs)

    clean_file(**kwargs)

