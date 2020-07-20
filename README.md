# pywid-csv
Two tools to graph, sort and parse through CSV files. Specifically designed around the OWID COVID-19 CSV.

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

This tool was created to facilitate the process of graphing two variables from the "Our World in Data" COVID-19 .csv reports. It comes with a plethora of options and parameters that allow for further customization of the output graph. With this tool, you could (for example) quickly visualize the effect of COVID-19 on every country as of today, or visualize the effect on a specific country through time.

#### Technologies

- Technology 1
- Technology 2

[Back To The Top](#pywid-csv)

---

## How To Use

#### Requirements
Matplotlib and you're ready to start graphing!
```html
    pip3 install matplotlib
```


#### Usage

Let's take a look at the ```--help``` page, shall we?

```html
usage: pywid.py F [options]

positional arguments:
  F                     The fields to be sorted, in x y format.

optional arguments:
  -h, --help            show this help message and exit
  -I <label>, --include_label <label>
                        Choose an extra field to label the points.
  -L <file>, --file <file>
                        Use a local file instead of the repository.
  -W, --world           Include world in results.
  -S <type> <filter>, --sort <type> <filter>
                        Sorting method to be used. Default is 'date today.'
  -O [<file>], --output [<file>]
                        Output the graph to a file, in PNG format.

All possible (default) fields are:
['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'new_deaths_per_million', 'total_tests', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cvd_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy', 'random']

Recommended sorting methods are:
  date          [yyyy-mm-dd OR 'today']
  iso_code      [iso]

```
[Back To The Top](#read-me-template)

---

## References
[Back To The Top](#read-me-template)

---

## License

MIT License

Copyright (c) [2017] [James Q Quick]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- Twitter - [@jamesqquick](https://twitter.com/jamesqquick)
- Website - [James Q Quick](https://jamesqquick.com)

[Back To The Top](#read-me-template)
