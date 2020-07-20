import csv
import datetime
import requests

# If you feel like the code could use any improvements, don't hesitate to send me a
# message and tell me about it!

# Many thanks to the folks at "Our World in Data," without whom this project would
# not be possible. Chek them out!
# https://github.com/owid/covid-19-data/tree/master/public/data


def get_request(url):
    request = requests.get(url)
    return request


def set_reader(file):

    if file.startswith("http://") or file.startswith("https://"):
        local = False
        response = get_request(file)
        iterable = response.text.splitlines()
        reader = csv.DictReader(iterable)

    else:
        local = True
        opened_file = open(file, "r")
        reader = csv.DictReader(opened_file)
    
    for line in reader:
        yield line

    if local:
        opened_file.close()


def clean_line(line, selected_keys):
    copied_line = line.copy()

    keys_to_delete = []

    for key in copied_line:
        if key not in selected_keys:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del copied_line[key]

    return copied_line
            

def sort_file(file, *fields, world=False, sort, **kwargs):
    reader = set_reader(file)

    for line in reader:

        if ("location" in line and line["location"] == "World" and world == False) or \
           ("" in [line[key] for key in fields[1:]]):
            continue

        if line[sort[0]] == sort[1]:
            yield clean_line(line, fields)
