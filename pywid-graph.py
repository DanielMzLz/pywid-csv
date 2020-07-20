#!/usr/bin/env python3

import argparse
import csv
import datetime
import matplotlib.pyplot as plt
import random

from funcs import *

# If you feel like the code could use any improvements, don't hesitate to send me a
# message and tell me about it!

# Many thanks to the folks at "Our World in Data," without whom this project would
# not be possible. Chek them out!
# https://github.com/owid/covid-19-data/tree/master/public/data

def sort_to_xy(file, xlabel, ylabel, sort, include_label="location", *args, **kwargs):
    lines = sort_file(file, include_label, xlabel, ylabel, sort=sort, *args, **kwargs)

    if include_label == None:
        input_labels = (xlabel, ylabel)
        output_labels = ("x", "y")
    else:
        input_labels = (include_label, xlabel, ylabel)
        output_labels = ("label", "x", "y")
    print(input_labels)
    print(output_labels)
    retrieved_info = dict()

    for label in output_labels:
        retrieved_info[label] = []

    for line in lines:
        for ilabel, olabel in zip(input_labels, output_labels):
            
            try:
                retrieved_info[olabel].append(float(line[ilabel]))
            except ValueError:
                retrieved_info[olabel].append(line[ilabel].replace("2020-", ""))

    return retrieved_info


def graph(info, xlabel, ylabel, include_label=None, output=False, *args, **kwargs):
    plt.scatter(info["x"], info["y"])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    #plt.autofmt_xdate()
    #plt.xticks(rotation=90)# ha='right')

    if include_label:
        for point in range(len(info["x"])):
            plt.annotate(info["label"][point], (info["x"][point], info["y"][point]))

    if output:
        plt.savefig(output, bbox_inches="tight")

    plt.show()


def parse_args(url, full_fieldnames):
    parser = argparse.ArgumentParser(usage="python3 %(prog)s A [options]",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=f"""All possible (default) fields are:\n{full_fieldnames + ['random']}\n\n
Recommended sorting methods are:
  date          <yyyy-mm-dd OR 'today'>
  iso_code      <iso>""")

    parser.add_argument("fields", metavar="A", type=str, nargs=2,
                        help = "The fields to be sorted, in x y format.")

    parser.add_argument("-I", "--include_label", default=None, metavar="<label>",
                        help="Choose an extra field to label the points.")

    parser.add_argument("-S", "--sort", metavar=("<type>", "<filter>"), nargs=2, default=("date","today"),
                        help="Sorting method to be used. Default is 'date today.'")

    parser.add_argument("-F", "--file", default=url, metavar="<file>",
                        help="Use a local file instead of the repository.")
    
    parser.add_argument("-W", "--world", action="store_true",
                        help="Include world in results.")

    parser.add_argument("-O", "--output", action="store", default=False,
                        const="graph.png", nargs="?", metavar="file",
                        help="Output the graph to a file, in PNG format.")

    args = parser.parse_args()
    return args


def prettify(label):
    return label.replace("_", " ").title().replace("Gdp", "GDP").replace("Older", "or Older").replace("Per", "per").replace("Iso", "ISO")


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    full_fieldnames = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'new_deaths_per_million', 'total_tests', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cvd_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy']
    
    kwargs = vars(parse_args(url, full_fieldnames))

    if "random" in kwargs["fields"]:
        kwargs["fields"] = [random.choice(full_fieldnames) if x == "random" else x for x in kwargs["fields"]]

    if kwargs["sort"][1] == "today":
        kwargs["sort"] = [kwargs["sort"][0], str(datetime.date.today())]

    print(kwargs)

    xlabel = kwargs["fields"][0]
    ylabel = kwargs["fields"][1]

    data = sort_to_xy(xlabel=xlabel, ylabel=ylabel, **kwargs)

    graph(data, prettify(xlabel), prettify(ylabel), **kwargs)

