---
title: CS 326
separator: <!--s-->
verticalSeparator: <!--s-->
theme: serif
revealOptions:
  transition: 'none'
---

<div class = "header-slide">

# Introduction to the Data Science Pipeline
## L.02 Data Collection & Structure

</div>
<!--s-->

## Announcements

**H.01**
- 82% of you have completed H.01 and received a grade on canvas. 🎉!
- If you still need help with H.01 or do not yet have a grade on Canvas, please reach out to myself or Chongyang. I am holding an office hour today from after lecture until 1PM in G32 for troubleshooting.
- H.01 will be due on 04.04.2024.

**P.01**
- P.01 is due on 04.09.2024. We will start that today.

**Attendance**
- A friendly reminder that attendance is **mandatory**.
- We will use iClicker for attendance and questions.

**Thursday (04.04.2024)** 
- Thursday's lecture will be pre-recorded. I will aim to have this up by early Wednesday afternoon.
- Chongyong will be available for office hours during the lecture time, right here in G15.

<!--s-->

<div class="header-slide">

# Closing out L.01

</div>

<!--s-->

## H.01 | Homework Grading

The highest score will be recorded, so long as it is submitted before the deadline! You have 3 attempts for every homework. 

Late homeworks will be penalized 10% per day.

<!--s-->

## H.01 | Expected Learnings / TLDR;

With the <span class="code-span">hello_world</span> assignment, we worked on the following:

1. Environment installation practice (<span class="code-span">conda</span>)
2. Exposure to git management (<span class="code-span">GitHub</span>)
3. Local development IDE practice (<span class="code-span">vscode</span>)
4. Familiarity with unit testing (<span class="code-span">pytest</span>)

These tools are all critical for any industry position and are often expected for entry level positions. Please continue to familiarize yourself with them over the course of the quarter.

<!--s-->

<div class = "header-slide">

# L.02 Attendance
Please check-in.

https://join.iclicker.com/KVYY

</div>

<!--s-->

<div class = "header-slide">

# L.02 Data Sources

</div>

<!--s-->

## Data Sources

Data is at the heart of all data science. It's the raw material that we use to build models, make predictions, and draw conclusions. Data can be gathered from a variety of sources, and it comes in many different forms. 

Some common data sources include:

- Bulk Downloads
- APIs
- Scraping, web crawling
- BYOD (Bring Your Own Data)

<!--s-->

## Data Sources | Bulk Downloads

Large datasets that are available for download from the internet.


| Source | Examples | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Government | data.gov | often free, very large datasets | Non-specific |
| Academic | UCI Machine Learning Repository | usually free, large datasets | Non-specific |
| Industry | Kaggle, HuggingFace | sometimes free, large datasets | Non-specific, sometimes expensive |


```python
# Demonstration of pulling from the UCI machine learning repository.
import pandas as pd
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(url, header=None)
```

```python
# Demonstration of pulling from the HuggingFace datasets library.
from datasets import load_dataset
dataset = load_dataset('imdb')
```

<!--s-->

## Data Sources | APIs

Data APIs are often readily available for sign up (usually for a fee).

While offering a lot of data, APIs can be restrictive in terms of the data they provide (and the rate at which you can pull it!).

API's often have better structure (usually backed by a db), and they often have the additional benefit of streaming or real-time data that you can poll for updates.

```python
import requests

API_KEY = 'your_api_key'
url = f'https://api.yourapi.com/data?api_key={API_KEY}'
r = requests.get(url)
data = r.json()
```

<!--s-->

## Data Sources | Scraping, web crawling

Web crawling is a free way to collect data from the internet. But be **cautious**. Many websites have terms of service that prohibit scraping, and you can easily overstep those.

Examples of packages built for webscraping in Python include <span class="code-span">beautifulsoup</span> and <span class="code-span">scrapy</span>.

```python
import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
soup.find_all('p')
```

<!--s-->

## Data Sources | BYOD (Bring Your Own Data)

Data that you collect yourself. In this case, you determine the format.

Examples for collecting survey data include Qualtrics and SurveyMonkey.

```python
import pandas as pd
df = pd.read_csv('survey_data.csv')
```
<!--s-->

## Data Sources | BYOD (Bring Your Own Data)
Collecting data yourself is common in academia and industry. But be careful!

<div class = "col-wrapper">
<div class = "c1" style = "width: 70%;">

**Policies Exist**
- *GDPR*: Controllers of personal data must put in place appropriate technical and organizational measures to implement the data protection principles.
- *HIPAA*: Covered entities must have in place appropriate administrative, technical, and physical safeguards to protect the privacy of protected health information.

**Bias *Always* Exists** Bias is everywhere. It's in the data you collect, the data you don't collect, and the data you use to train your models. In almost all cases, we perform a *sampling*. It's your job to ensure it is a reasonable sample.

**Ethical Concerns**
Don't collect data that you don't need. Definitely don't collect data that you don't have permission to collect.

</div>
<div class = "c2 col-centered"  style = "width: 30%">
<iframe width="256" height="256" src="https://www.youtube.com/embed/R2vhjC5qCQk?si=m3ImvZqhDawRoMTo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
</div>

<!--s-->

## Data Sources | Question

You're building a model to predict the price of a house based on its location, size, and number of bedrooms. Which of the following data sources would be a great first place to look?

&emsp;A. Bulk Downloads <br>
&emsp;B. APIs <br>
&emsp;C. Scraping, web crawling <br>
&emsp;D. BYOD (Bring Your Own Data) <br>

<!--s-->

## Data Sources | Question

You just built an amazing stock market forecasting model. Congrats! Now, you want to test it on real-time data. Which of the following data sources would be a great first place to look?

&emsp;A. Bulk Downloads <br>
&emsp;B. APIs <br>
&emsp;C. Scraping, web crawling <br>
&emsp;D. BYOD (Bring Your Own Data) <br>

<!--s-->

<div class = "header-slide">

# Data Structures

</div>
<!--s-->


## Data Structures

| Type | Example | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Structured | Relational Database | easy to query, fast | not flexible, hard to update data |
| Semi-Structured | XML, CSV, JSON | moderate flexibility, easy to add more data | slow, harder to query |
| Unstructured | Plain Text, Images, Audio, Video | very flexible, easy to add more data | slow, hardest to query |

<!--s-->

## Data Structures | Structured Example (Relational Database)

| Type | Example | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Structured | Relational Database | easy to query, fast | not flexible, hard to update data |
| Semi-Structured | XML, CSV, JSON | moderate flexibility, easy to add more data | slow, harder to query |
| Unstructured | Plain Text, Images, Audio, Video | very flexible, easy to add more data | slow, hardest to query |

```sql
CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  name VARCHAR(100),
  hire_date DATE
);
```
<!--s-->

## Data Structures | Semi-Structured Example (JSON)

| Type | Example | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Structured | Relational Database | easy to query, fast | not flexible, hard to update data |
| Semi-Structured | XML, CSV, JSON | moderate flexibility, easy to add more data | slow, harder to query |
| Unstructured | Plain Text, Images, Audio, Video | very flexible, easy to add more data | slow, hardest to query |

```json
employeeData = {
  "employee_id": 1234567,
  "name": "Jeff Fox",
  "hire_date": "1/1/2013"
};
```

<!--s-->

## Data Structures | Unstructured Example (Plain Text)

| Type | Example | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Structured | Relational Database | easy to query, fast | not flexible, hard to update data |
| Semi-Structured | XML, CSV, JSON | moderate flexibility, easy to add more data | slow, harder to query |
| Unstructured | Plain Text, Images, Audio, Video | very flexible, easy to add more data | slow, hardest to query |

```text
Dear Sir or Madam,

My name is Jeff Fox (employee id 1234567). I'm excited to start on 1/1/2013.

Sincerely,
Jeff Fox
```

<!--s-->

<div class = "header-slide">

# Data Cleaning

</div>
<!--s-->

## Data Cleaning

Data is often dirty! Don't ever give your machine learning or statistical model dirty data.

Remember the age-old adage:

> Garbage in, garbage out.

 Data cleaning is the process of converting source data into target data without errors, duplicates, or inconsistencies. You will often need to structure data in a way that is useful for your analysis, so learning some basic data manipulation is **essential**.

<!--s-->

## Data Cleaning | Common Data Issues

1. Incompatible data
2. Missing values
3. Extreme Outliers

<!--s-->

## Data Cleaning | Handling Incompatible Data

<div style = "font-size: 0.85em;">

| Data Issue | Description | Example | Solution |
| --- | --- | --- | --- |
| Unit Conversions | Numerical data conversions can be tricky. | 1 mile != 1.6 km | Measure in a common unit, or convert with caution. |
| Precision Representations | Data can be represented differently in different programs. | 64-bit float to 16-bit integer | Use the precision necessary and hold consistent. |
| Character Representations | Data is in different character encodings. | ASCII, UTF-8, ... | Create using the same encoding, or convert with caution. |
| Text Unification | Data is in different formats. | D'Arcy -> Darcy -> DArcy -> D Arcy | Use a common format, or convert with caution. <span class="code-span">RegEx</span> will be your best friend.| 
| Time / Date Unification | Data is in different formats. | 10/11/2019 vs 11/10/2019 | Use standard libraries & UTC. A personal favorite is seconds since epoch. |

</div>
<!--s-->

## Data Cleaning | Handling Missing Values

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

  Data is often missing from datasets. It's important to identify why it's missing. Once you have established that it is **missing at random**, you can proceed with **substitution**.

  When missing data, we have a few options at our disposal:

  1. Drop the entire row
  2. Drop the entire column
  3. Substitute with a reasonable value

</div>
<div class="c2" style = "width: 50%">

  ``` [1-5|4]
  id    col1    col2    col3    col4
  p1    2da6    0.99    32     43
  p2    cd2d    1.23    55      38
  p3    9999    89.2    NaN     32
  p4    4e7c    0.72    9.7     35
  ```

</div>
</div>

<!--s-->

## Data Cleaning | Handling Missing Values with Substitution

<div class = "col-wrapper"> 
<div class = "c1" style = "width: 60%; font-size: 0.85em;">


| Method | Description | When to Use |
| --- | --- | --- |
| Forward fill | Fill missing value using the last valid value. | Time Series |
| Backward fill | Fill missing value using the next valid value. | Time Series |
| Imputation by interpolation | Use linear interpolation to predict missing values. | Time Series |
| Mean value imputation | Fill missing value with mean from column. | Random missing values |
| Conditional mean imputation | Estimate mean from other variables in the dataset. | Random missing values |
| Random value imputation | Sample random values from the column. | Random missing values | 
| Multiple Imputation | Uses many regression models and other variables to fill missing values. | Random missing values |

</div>

<div class = "c2" style = "width: 40%">

```python
import pandas as pd

# Load data.
df = pd.read_csv('data.csv')

# Forward fill.
df_ffill = df.fillna(method='ffill')

# Backward fill.
df_bfill = df.fillna(method='bfill')

# Mean value imputation.
df_mean = df.fillna(df.mean())

# Random value imputation.
df_random = df.fillna(df.sample())

# Imputation by interpolation.
df_interpolate = df.interpolate()
```

</div>
</div>

<!--s-->

## Data Cleaning | Question

You have streaming data that is occasionally dropping values. Which of the following methods would be appropriate to fill missing values when signal fails to update? 

*Please note, in this scenario, you can't use the future to predict the past.*

&emsp;A. Forward fill <br>
&emsp;B. Imputation by interpolation <br>
&emsp;C. Mean value imputation <br>
&emsp;D. Backward fill <br>

<!--s-->

## Data Cleaning | Handling Outliers

Outliers are extreme values that deviate from other observations on data. They may indicate a variability in a measurement, experimental errors, or a novelty.

Outliers can be detected using:

- **Boxplots**: A visual representation of the five-number summary.
- **Scatterplots**: A visual representation of the relationship between two variables.
- **z-scores**: A measure of how many standard deviations a data point is from the mean.
- **IQR**: A measure of statistical dispersion, being equal to the difference between the upper and lower quartiles.

Handling outliers should be done on a case-by-case basis. Don't throw away data unless you have a very compelling (and **documented**) reason to do so!

<!--s-->

## Data Cleaning | Keep in Mind

- Cleaning your data is an iterative process.
  - **Hot tip**: Focus on making your data preprocessing *fast*. You will be doing it a lot, and you'll want to be able to iterate quickly. Look into libraries like <span class="code-span">dask</span>, <span class="code-span">pyspark</span>, and <span class="code-span">ray</span> for large datasets.
- Data cleaning is often planned with visualization. 
  - Always look at the data. Always. We'll go over plotting approaches for L.03.
- Data cleaning can fix modeling problems.
  - Your first assumption should always be "something is wrong with the data", not "I should try another model".
- Data cleaning is not a one-size-fits-all process, and often requires domain expertise.

<!--s-->

<div class = "header-slide">

# P.01 | Group Formation & Project Proposal
Due: 04.09.2024 <br>
Canvas Assignment Link: [P.01](https://canvas.northwestern.edu/courses/211880/assignments/1404904)

</div>

<!--s-->


## P.01 | Creating a Group

### **Group Creation**
You can create a group on Canvas using this [[link]](https://canvas.northwestern.edu/courses/211880/groups).

1. Click on the "People" tab on the left-hand side.
2. Click on the "Groups" tab.
3. Click on the "Create Group" button OR "Join Group" button.

### **Group Name**
Your group name can be anything you like, but it should be unique.

### **Communication**
I suggest creating a group chat on Slack, Discord, or WhatsApp. This will make it easier to communicate with your group members.

<!--s-->

## P.01 | Project Proposal

**One person** per group should submit the project proposal using the text editor on Canvas. Please follow the format provided on canvas.

Your proposal should include:

1. **Team Name**: The name of your team.
2. **Team Members**: The names of your team members.
3. **Project Title**: The title of your project.
4. **Project Description**: A brief description of your project.
5. **Data Source**: Where you plan to get your data.
6. **Project Goals**: What you hope to achieve, or what findings you expect with your project.

<!--s-->

<div class="header-slide">

# Questions?

</div>