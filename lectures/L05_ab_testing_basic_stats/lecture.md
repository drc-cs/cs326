---
title: COMP_SCI 326
separator: <!--s-->
verticalSeparator: <!--v-->
theme: serif
revealOptions:
  transition: 'none'
---

<div class = "header-slide">

# Introduction to the Data Science Pipeline
## A/B Testing and Statistical Inference
</div>

<!--s-->

## Announcements

- H.02 is due on **04.16.2024**
    - 5 of you have already submitted H.02! 🎉!
    - We'll work on finishing up the last few parts of the assignment today.
- Office Hours today from 12:20P - 1P in Annenberg G31

<!--s-->

<div class = "header-slide">

# L.04 Attendance
Please check in.

https://join.iclicker.com/KVYY

</div>

<!--s-->

<div class="header-slide">

# A/B Testing

</div>

<!--s-->

## Introduction to A/B Testing

A/B testing, a critical methodology widely used in tech companies and various industries, plays a pivotal role in optimizing user experience and boosting key performance indicators such as engagement and conversion rates.

This approach tests two variants, A and B, in a randomized experiment to make data-driven decisions regarding changes to products, websites, or apps.

<div class="col-centered">
<img src = "https://www.optimizely.com/contentassets/08726e145f1b4743a0ba2f30c0447b76/ab-testing.png" style="border-radius:15px; height: 20%; width: 50%;">
</div>
<p style="text-align: center; font-size: 0.6em; color: grey;">Optimizely (2024)</p>

<!--s-->

## Understanding A/B Testing

At its core, A/B testing involves comparing two versions of a web page, product feature, or other elements to determine which one performs better.

This process enables businesses to make incremental changes that can lead to significant improvements in user satisfaction and business outcomes.

<div class="col-centered">
<img src = "https://www.optimizely.com/contentassets/08726e145f1b4743a0ba2f30c0447b76/ab-testing.png" style="border-radius:15px; height: 20%; width: 50%;">
</div>
<p style="text-align: center; font-size: 0.6em; color: grey;">Optimizely (2024)</p>


<!--s-->

## Why Implement A/B Testing?

- **Innovation and Improvement:** Whether it's deciding which photograph leads to better retention of subscribers or testing a new feature's impact on user engagement, A/B testing provides a systematic method for assessing the potential benefits of new ideas.

- **Data-driven Decisions:** By relying on empirical data, companies can move beyond guesswork and make informed decisions that align with their strategic goals.

<!--s-->



## Case Study | Social Network App

A study within a new social network app revealed that users who tagged a friend during their trial period had a **31**% increase in daily usage after the trial period ended.

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

This insight suggests that encouraging social interactions may **increase user retention**.

An immediate reaction might be to prioritize features solely based on this correlation, such as pushing all new installs to tag a friend.

</div>
<div class="c2" style = "width: 50%">

<iframe width = "100%" height = "60%" src="https://lottie.host/embed/6a06ca79-cb9c-48e2-bdac-a8bbbcb03815/j0VNBrf81N.json"></iframe>

</div>
</div>

<!--s-->

## Question 0 | A/B Testing Considerations

**Question:** After observing the correlation between tagging a friend and increased user retention, should the app developers immediately implement this feature for all new users?

<p style="margin-left: 25px;">
A. Yes<br>
B. No<br>
</p>

<!--s-->

## Case Study | Considering External Influences

Factors such as:

- **Seasonality:** Changes in user behavior due to holidays or seasonal trends.
- **Marketing Campaigns:** The impact of marketing campaigns on user engagement.
- **Product Updates:** Changes in the app's features or design.
- **User Demographics:** Variations in user behavior based on age, location, or other factors.

Could all contribute to conversion rate changes. Thus, it's imperative not to jump to conclusions about causality based solely on passively observed correlations.

<!--s-->

## Case Study | Implementing Effective A/B Testing

To understand the impact of tagging a friend during a trial period, a structured A/B testing approach is essential:

1. **Construct a Hypothesis:** Begin with a clear, testable hypothesis.
    - **H0**: Tagging a friend during the trial period has no effect on the original users' retention.
    - **H1**: Tagging a friend during the trial period increases the original users' retention.

2. **Design Study / Trial:** Establish how many subjects are necessary for a statistically significant test and estimate the duration of the experiment. 
    - Resources exist to make this process easier [[link]](https://www.evanmiller.org/ab-testing/sample-size.html)

3. **Measure Results:** Use hypothesis testing to assess if there's a significant difference between the two groups.
    - We'll cover these tests in more detail later in the lecture.

4. **Take Action:** Based on the findings, make informed decisions and continue the cycle of experimentation and learning.

<!--s-->

## Proper A/B Testing Highlights

1. **Randomization:** Randomly assign subjects to the control and treatment groups to avoid selection bias.

2. **Statistical Significance:** Use statistical tests to determine if the observed differences are significant.

3. **Sample Size:** Ensure that the sample size is large enough to detect meaningful differences.

4. **Duration:** Run the experiment for a sufficient duration to capture the effects of the changes.

5. **Segmentation:** Analyze results across different segments to identify potential variations in the treatment effect.

<!--s-->

<div class="header-slide">

# Hypothesis Testing

</div>

<!--s-->

## What is Hypothesis Testing?

Hypothesis testing uses statistical methods to determine whether there is enough evidence to reject a null hypothesis in favor of an alternative hypothesis.

The null hypothesis ($H_0$) is a statement that there is no difference between groups, while the alternative hypothesis ($H_1$) posits that there is a difference.

<!--s-->

## Question 1.1.0 | Hypothesis Testing

**Question:** You have data on the average time it takes for two groups of students to complete a test. Group A has an average time of 45 minutes +/- 5 minutes, while Group B has an average time of 50 minutes +/- 5 minutes. You want to determine if there is a significant difference between the two groups. 

**What test would you use to compare the two groups, assuming all conditions are met?**

<p style="margin-left: 25px;">
A. Chi-Square Test of Independence<br>
B. One-Way ANOVA<br>
C. T-Test (Independent)<br>
D. T-Test (Paired)<br>
</p>

<!--s-->

## Question 1.1.1 | Hypothesis Testing

**Question:** You have data on the average time it takes for two groups of students to complete a test. Group A has an average time of 45 minutes +/- 5 minutes, while Group B has an average time of 50 minutes +/- 5 minutes. You want to determine if there is a significant difference between the two groups. 

**How would you rate your confidence on the answer to Question 1, on a scale of 1-10?**

<!--s-->

## Common Hypothesis Tests

The following are some hypothesis tests used in statistics:

<div style="font-size: 0.8em;">

| Test | Assumptions | Usage (Easy ~ Rule) |
| --- | --- | --- |
| t-test | 1. Data are independently and identically distributed. <br> 2. Both groups follow a normal distribution. | When comparing the means of two independent groups. |
| t-test (paired)  | 1. Data are independently and identically distributed. <br> 2. The differences are normally distributed.<br> 3. The pairs are selected randomly and are representative.| When you have pre / post test information on subjects or a matched pairs experiment. |
| chi-square test of independence | 1. Data are independently and identically distributed. <br> 2. All empirical frequencies are 5 or greater. | When comparing proportions across categories. |
| One-way ANOVA  | 1. Responses for each group are normally distributed. <br> 2. Variances across groups are approximately equal. <br> 3. Data are independently and identically distributed. | When comparing the means of three or more groups. |

</div>

<!--s-->

## Question 1.2.0 | Hypothesis Testing

**Question:** You have data on the average time it takes for two groups of students to complete a test. Group A has an average time of 45 minutes +/- 5 minutes, while Group B has an average time of 50 minutes +/- 5 minutes. You want to determine if there is a significant difference between the two groups. 

**What test would you use to compare the two groups, assuming all conditions are met?**

<p style="margin-left: 25px;">
A. Chi-Square Test of Independence<br>
B. One-Way ANOVA<br>
C. T-Test (Independent)<br>
D. T-Test (Paired)<br>
</p>

<!--s-->

## Question 1.2.1 | Hypothesis Testing

**Question:** You have data on the average time it takes for two groups of students to complete a test. Group A has an average time of 45 minutes +/- 5 minutes, while Group B has an average time of 50 minutes +/- 5 minutes. You want to determine if there is a significant difference between the two groups. 

**How would you rate your confidence on the answer to Question 1, on a scale of 1-10?**

<!--s-->


## Question 2 | Hypothesis Testing

**Question:** Propose I wanted to do an analysis on the efficacy of Slide 17. Let's say I collected your level of confidence of Question 1 before and after seeing Slide 17 (1 to 10). 

**What test would you use to compare the before / after confidence of students, assuming all conditions are met?**

<p style="margin-left: 25px;">
A. Chi-Square Test of Independence<br>
B. One-Way ANOVA<br>
C. T-Test (Independent)<br>
D. T-Test (Paired)<br>
</p>

<!--s-->

## Common Hypothesis Tests | T-Test Setup

**Scenario:** Comparing the effect of two medications. Medication A has been used on 40 subjects, having an average recovery time of 8 days, with a standard deviation of 2 days. Medication B (new) has been used on 50 subjects, with an average recovery time of 7 days and a standard deviation of 2.5 days. 

**Hypotheses:**
- H0: μ1 = μ2 (No difference in mean recovery time)
- H1: μ1 ≠ μ2 (Difference in mean recovery time)

**Assumptions:**
- Groups are I.I.D.
    - I.I.D. stands for independent and identically distributed.
- Both groups follow a normal distribution.*
    - Once you have enough samples, the central limit theorem will ensure normality.
- Equal variances between the two groups (homoscedasticity).*
    - If variances are not equal, a Welch's t-test can be used.

<!--s-->

## Common Hypothesis Tests | T-Test Calculation

<div style="font-size: 0.85em">

**Calculation:**

To calculate the t-statistic, we use the following formula (variances not assumed to be equal):

$ t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} $

where:

- $ \bar{x}_1, \bar{x}_2 $ are the sample means.
- $ \mu_1, \mu_2 $ are the population means.
- $ s_1^2, s_2^2 $ are the estimated variances, where s is the standard error for the sample.
- $ n_1, n_2 $ are the sample sizes.

The t-statistic measures the difference between the two sample means relative to the variability in the data. 

We also need to calculate the degrees of freedom (df) for the t-distribution. Degrees of freedom can be defined as the maximum number of independent values that can vary in your calculation. In this case, df is calculated as:

$ df = \frac{(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2})^2}{\frac{(\frac{s_1^2}{n_1})^2}{n_1 - 1} + \frac{(\frac{s_2^2}{n_2})^2}{n_2 - 1}} $

</div>
<!--s-->

## Common Hypothesis Tests | T-Test Decision

**Decision Process**

1. Compare the computed t-value against the critical t-value from the t-distribution table with $\alpha = 0.05$ and $df$.
2. If the computed t-value falls within the critical range, reject the null hypothesis.

<div class="col-centered">
<img src="https://www.researchgate.net/publication/12025083/figure/fig1/AS:352960891637763@1461163842564/Extract-of-the-t-table-The-first-column-lists-the-degrees-of-freedom-n-1-The.png">
</div>
<!--s-->

## Common Hypothesis Tests | T-Test (Paired) Setup

**Scenario:** A group of 25 patients is measured for cholesterol levels before and after a particular treatment, aiming to evaluate the treatment's effect on cholesterol.

**Hypotheses:**
- H0: $d=0$ (No difference in mean cholesterol levels)
- H1: $d \ne 0$ (Difference in mean cholesterol levels)

**Assumptions:**
- The differences within pairs are independent.
- The differences are normally distributed.
- The pairs are selected randomly and are representative.

<!--s-->

## Common Hypothesis Tests | T-Test (Paired) Calculation

**Calculation:**

First, find the difference ($d$) for each pair. Then, calculate the mean ($\bar{d}$) and standard deviation ($s_d$) of those differences.

$ t = \frac{\bar{d}}{s_d / \sqrt{n}} $

where $n$ is the number of pairs.

The t-statistic measures the difference between the mean differences and the expected mean differences. Degrees of freedom can be calculated with $df = n - 1$.

<!--s-->

## Common Hypothesis Tests | T-Test (Paired) Decision

**Decision Process**

1. Using the t-distribution table with $df = n - 1$, compare the calculated t-value.
2. If the computed t-value falls within the critical range, reject the null hypothesis.

<div class="col-centered">
<img src="https://www.researchgate.net/publication/12025083/figure/fig1/AS:352960891637763@1461163842564/Extract-of-the-t-table-The-first-column-lists-the-degrees-of-freedom-n-1-The.png">
</div>


<!--s-->

## Common Hypothesis Tests | Chi-Square Test Setup

**Scenario:** You have two penguin species, Adelie and Chinstrap. They are observed in the wild, and the following data is collected from two islands (A and B):

| Species | Island A | Island B |
|---------|----------|----------|
| Adelie  | 15       | 5       |
| Chinstrap | 5     | 15       |


**Hypotheses:**
- H0: The species distribution is independent of the island.
- H1: The species distribution is dependent on the island.

**Assumptions:**
- Observations are independent.
- All expected frequencies are at least 5.

<!--s-->

## Question 3 | Ch-Square Expectation Calculation

**Question:** Calculate the expected frequency for Adelie penguins on Island A. Assuming the null hypothesis is true, what is the expected frequency?

| Species | Island A | Island B |
|---------|----------|----------|
| Adelie  | 15       | 5       |
| Chinstrap | 5     | 15       |

<p style="margin-left: 25px;">
A. 10<br>
B. 5<br>
C. 7.5<br>
D. 12.5<br>
</p>

<!--s-->

## Common Hypothesis Tests | Chi-Square Test Calculation

**Calculation:**

The chi-square statistic of independence is calculated as:

$\chi^2 = \sum \frac{(O - E)^2}{E}$

where $O$ is the observed frequency and $E$ is the expected frequency. 

Degrees of freedom for the chi-square test of independence: 

$df = (r - 1) \times (c - 1)$

where $r$ is the number of rows and $c$ is the number of columns in the contingency table.

Plugging in the values: 

$ \chi^2 = \frac{(15 - 10)^2}{10} + \frac{(5 - 10)^2}{10} + \frac{(5 - 10)^2}{10} + \frac{(15 - 10)^2}{10} = 10 $

*Where the expected frequency is calculated as the row total times the column total divided by the grand total.*

<!--s-->

## Common Hypothesis Tests | Chi-Square Test Decision

**Decision Process**

1. Compare the $\chi^2$ value against the critical values from the chi-square distribution table with $df$
2. If $\chi^2 > \chi_{critical}$, reject H0.

<div class="col-centered">
<img src="https://www.mun.ca/biology/scarr/IntroPopGen-Table-D-01-smc.jpg" style = "border-radius: 10px; height: 40%; width: 40%;">
</div>
<p style="text-align: center; font-size: 0.6em; color: grey;">© 2022, Steven M. Carr</p>

<!--s-->

## Common Hypothesis Tests | One-Way ANOVA Setup

**Scenario:** Testing if there's a difference in the mean test scores across three teaching methods used across different groups.

**Hypotheses:**

- H0: $ \mu_1 = \mu_2 = \mu_3 $ (no difference among the group means)
- H1: At least one group mean is different.

**Assumptions**
- Groups are I.I.D.
- Groups follow a normal distribution.
- Variances across groups are approximately equal.
    - A good rule of thumb is a ratio of the largest to the smallest variance less than 4.

<!--s-->

## Common Hypothesis Tests | One-Way ANOVA Calculation

**Calculation:**

The total sum of squares (SS) is calculated as:

$ s^2 = \frac{SS}{df} = \frac{\sum (x - \bar{x})^2}{n - 1} $

where $SS$ is the sum of squares, $df$ is the degrees of freedom, $x$ is the data point, $\bar{x}$ is the sample mean, and $n$ is the sample size.

Anova breaks down the variance explained by the groups ($SS_{between}$) and the variance not explained by the groups ($SS_{within}$). The F-statistic measures the ratio of the variance between groups to the variance within groups. Anova calculates the F-statistic:

$ F = \frac{SS_{between} / df_{between}}{SS_{within} / df_{within}} $


The degrees of freedom are $df_{between} = k - 1$ and $df_{within} = N - k$. Where $k$ is the number of groups and $N$ is the total number of observations.

<!--s-->

## Common Hypothesis Tests | One-Way ANOVA Decision

**Decision Process**

1. Compare the calculated F-value with the critical F-value from the F-distribution table at $df_{between}$ and $df_{within}$.
2. Reject H0 if $F > F_{critical}$, indicating significant differences among means.

<div class="col-centered">
<img src="https://graziano-raulin.com/images/part%20of%20F%20table.png">
</div>

<!--s-->

## Choosing a Non-Parametric Test

If the assumptions for parametric tests are not met, non-parametric tests can be used. 

These tests are distribution-free and do not require the data to be normally distributed. These may make less powerful inferences than parametric tests, because parametric tests derive power from the strong assumptions they make about the shape of the data.

<div style="font-size: 0.8em">

| Test    | Use in place of | Description |
|-----------------------|------------------|-------------------------|
| Spearman’s r  | Pearson’s r | For quantitative variables with non-linear relation. |
| Kruskal–Wallis H  | ANOVA | For 3 or more groups of quantitative data |
| Wilcoxon Rank-Sum | Independent t-test  | For 2 groups, different populations. |
| Wilcoxon Signed-rank  | Paired t-test| For 2 groups from the same population. |
| Fisher’s Exact Test | Chi-Square | For 2 categorical variables. |

<p style = "text-align: center; color: grey"> © Adapted from Scribbr, 2024 </p>

</div>

<!--s-->

<div class="header-slide">

# Homework Assignment
## H.02 Data Exploration and Basic Statistics

Due: 04.16.2024

</div>

<!--s-->