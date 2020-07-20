# pywid-csv
Two tools to graph, sort and parse through CSV files. Specifically designed around the OWID COVID-19 CSV. Made in Python 3.

---

## Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How to Use](#how-to-use)
    - [Requirements](#requirements)
    - [pywid-graph](#pywid-graph)
    - [pywid-parse](#pywid-parse)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

This repo comes with two tools: ```pywid-graph.py``` and ```pywid-parse.py```.

### pywid-graph.py

This tool was created to facilitate the process of graphing two variables from the "Our World in Data" COVID-19 .csv reports. It comes with a plethora of options and parameters that allow for further customization of the output graph. With this tool, you could (for example) quickly visualize the effect of COVID-19 on every country as of today, or visualize the effect on a specific country through time.

### pywid-parse.py

This tool can help you simplify OWID's .csv reports. Select any amount of the header variables to pass to the new output file. Like the grapher, it comes with several options to help you include exactly what you want to include.


[Back To The Top](#pywid-csv)

---

## How To Use

### Requirements
Matplotlib and you're ready to start graphing!
```html
    pip3 install matplotlib
```
That is, assuming you already have ```python3``` and ```pip3``` installed.

### pywid-graph

Let's take a look at the respective ```--help``` pages, shall we?

```html
usage: python3 pywid-graph.py A [options]

positional arguments:
  A                     The fields to be sorted, in x y format.

optional arguments:
  -h, --help            show this help message and exit
  -I <label>, --include_label <label>
                        Choose an extra field to label the points.
  -S <type> <filter>, --sort <type> <filter>
                        Sorting method to be used. Default is 'date today.'
  -F <file>, --file <file>
                        Use a local file instead of the repository.
  -W, --world           Include world in results.
  -O [file], --output [file]
                        Output the graph to a file, in PNG format.

All possible (default) fields are:
['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'new_deaths_per_million', 'total_tests', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cvd_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy', 'random']

Recommended sorting methods are:
  date          <yyyy-mm-dd OR 'today'>
  iso_code      <iso>
```

- ```pywid-graph.py``` expects exactly two fields to be entered as argument A, so that each field can correspond to an x or y axis. 
- An additional field can be entered as a ```-I```, an independent label for each of the points graphed. 
- To help you change the underlying functionality of the grapher, you can utilize the ```--sort``` arguments. By default, the graph will retrieve entries by date and those that match today's date. To change whichever day you wish to match, say, you want to match the first of January 2020, you'd do ```--sort date 2020-01-01```. To change from date altogether and graph the values of a specific country, you'd do ```--sort iso_code USA```. These two are the recommended sorting methods, but there are no restrictions on what can classify as a sorting method. The sorting itself hinges on the ```type``` value matching the given ```filter``` for each entry.
- As mentioned, this tool can also utilize other CSV files, with the help of the ```-F``` argument. 
- The "World" entry is naturally excluded for every graph. If one wishes to override this behavior, it can be done so with the help of the ```-W``` argument.
- ```-O``` is used to output the graph into a PNG file. The default name will be ```graph.png```, but this can be modified.

#### Examples

So, let's start with the basics: Suppose you wish to analyze the worldwide relationship between the percentage of populations that are aged 65 or older and the total amount of deaths. With ```pywid-graph.py```, you'd do:
```html
python3 pywid-graph aged_65_older total_deaths
```
That'll return something like this:

<p align="center">
    <img src=https://user-images.githubusercontent.com/39423011/87971430-f3a20280-ca8a-11ea-8190-61c82ce48064.png width="350" title="graph.png">
</p>

Now we know that there is no linear correlation between these two variables! But who's that one guy really far on the right? Let's label the points to find out!

```html
python3 pywid-graph aged_65_older total_deaths --include_label iso_code
```

<p align="center">
    <img src=https://user-images.githubusercontent.com/39423011/87980158-ba708f00-ca98-11ea-94b0-e1dd00bd8e03.png width="350" title="graph.png">
</p>

With this information, we can now tell that it is Japan that has the highest percentage of people aged 65 or older in the world! Even so, they have still been able to maintain a low amount of total deaths. Let's try and analyze how Japan has faired when compared to the entirety of the world:

```html
python3 pywid-graph aged_65_older total_deaths --include_label iso_code --world
```

<p align="center">
    <img src=https://user-images.githubusercontent.com/39423011/87981075-39b29280-ca9a-11ea-99db-b68016965874.png width="350" title="graph.png">
</p>

We can see that Japan is minimized even more when the entirety of the world is factored in. Cool! Let's try and analyze how the landscape looked during the early stages of the pandemic, say the second of February. 

```html
python3 pywid-graph aged_65_older total_deaths --include_label iso_code --world --sort date 2020-02-02
```

<p align="center">
    <img src=https://user-images.githubusercontent.com/39423011/87981398-d1b07c00-ca9a-11ea-84f9-21dcf1f16c3c.png width="350" title="graph.png">
</p>

Here we can appreciate a very different landscape. China leads the majority of the unfortunate passings, while their prevalence seems to be rising in Iran, Korea, and Italy; Japan seems to remain unchanged, but we can be sure that they haven't been unaffected by the pandemic. Let's take a closer look at how they have faired through the pandemic by changing our sorting type. Of course, we should change the x-axis to reflect change over time (dates), and we can remove the world from the graph. We could also declutter the graph from the labels, as it is obvious every point will be labeled as Japan; alternatively, we could label the points with the respective dates. We will do the former:

```html
python3 pywid-graph date total_deaths --sort iso_code JPN
```

<p align="center">
    <img src=https://user-images.githubusercontent.com/39423011/87982635-b2b2e980-ca9c-11ea-8a4b-46fa2ac205f6.png width="350" title="graph.png">
</p>

Now, we can see that Japan did struggle at first with the pandemic, but has been able to maintain the total deaths under a thousand.


This is all very interesting and everything, but we haven't been saving any of these graphs for later use! Let's do that with ```-O```. Let's also specify a name for this graph.

```html
python3 pywid-graph date total_deaths --sort iso_code JPN -O japans-responje.png
```

With that, you have become an expert with this tool! Good on you!

[Back To The Top](#pywid-csv)

---

## References
[Back To The Top](#pywid-csv)

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

[Back To The Top](#pywid-csv)

---

## Author Info

- Twitter - [@jamesqquick](https://twitter.com/jamesqquick)
- Website - [James Q Quick](https://jamesqquick.com)

[Back To The Top](#pywid-csv)
