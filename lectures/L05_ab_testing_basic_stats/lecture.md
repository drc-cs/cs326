---
title: COMP_SCI 396
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
    - 3 of you have already submitted H.02! 🎉!
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

A study within a new social network app revealed that users who tagged a friend during their trial period had a **31**% higher conversion rate.

This insight suggests that encouraging social interactions can significantly affect user retention.

An immediate reaction might be to prioritize features solely based on this correlation, such as pushing all new installs to tag a friend. But this would be problematic, because this perspective overlooks the complexity of user behavior and external factors that could influence the observed outcome.

<!--s-->

## Case Study | Considering External Influences

Factors such as:

1. The ability to link other accounts
2. Support for multi-factor authentication
3. Improvements in the app's user interface

Could all contribute to conversion rate changes. Thus, it's imperative not to jump to conclusions about causality based solely on passively observed correlations.

<!--s-->

## Case Study | Implementing Effective A/B Testing

To understand the impact of tagging a friend during a trial period, a structured A/B testing approach is essential:

1. **Construct a Hypothesis:** Begin with a clear, testable hypothesis.
    - **H0**: Tagging a friend during the trial period has no effect on their conversion rate.
    - **H1**: Tagging a friend during the trial period increases their conversion rate.

2. **Determine Sample Size:** Establish how many subjects are necessary for a statistically significant test and estimate the duration of the experiment. 
    - Resources exist to make this process easier [[link]](https://www.evanmiller.org/ab-testing/sample-size.html)

3. **Measure Results:** Use hypothesis testing to assess if there's a significant difference between the two groups.
    - We'll cover these tests in more detail later in the lecture.

4. **Take Action:** Based on the findings, make informed decisions and continue the cycle of experimentation and learning.

<!--s-->

## Avoiding Common Pitfalls in A/B Testing

To ensure the reliability of A/B test results, ensure the following is true:

- Sample sizes are sufficient and comparable between groups.
- Adequate time has been allotted for the experiment.
- Overlap and conflict between concurrent experiments is avoided.
- Data collection and instrumentation are consistent and reliable.

<!--s-->

<div class="header-slide">

# Hypothesis Testing

</div>

<!--s-->

## What is Hypothesis Testing?

Hypothesis testing uses statistical methods to determine whether there is enough evidence to reject a null hypothesis in favor of an alternative hypothesis.

The null hypothesis ($H_0$) is a statement that there is no effect or no difference between groups, while the alternative hypothesis ($H_1$) posits that there is an effect or difference.

<!--s-->

## Common Hypothesis Tests

The following are some of the most common hypothesis tests used in statistics:

<div style="font-size: 0.8em;">

| Test | Assumptions | Usage (Easy ~ Rule) |
| --- | --- | --- |
| t-test | 1. Data are independently and identically distributed. <br> 2. Normal distribution of the groups' means. <br> 3. Equal variances between the two groups (homoscedasticity).* | When comparing the means of two independent groups. |
| t-test (paired)  | 1. The differences within pairs are independent. <br> 2. The differences are normally distributed.<br> 3. The pairs are selected randomly and are representative.| When comparing the means of two related groups. |
| chi-square test of independence | 1. Observations are independent. <br> 2. All expected frequencies are at least 5. | When comparing categorical data counts. |
| One-way ANOVA  | 1. Responses for each group are normally distributed. <br> 2. Variances across groups are approximately equal. <br> 3. Observations are independent. | When comparing the means of three or more groups. |

</div>
<!--s-->

## Common Hypothesis Tests | T-Test Setup

**Scenario:** Comparing the effect of two medications. Medication A has been used on 40 subjects, having an average recovery time of 8 days, with a standard deviation of 2. Medication B (new) has been used on 50 subjects, with an average recovery time of 7 days and a standard deviation of 2.5. 

**Hypotheses:**
- H0: μ1 = μ2 (No significant difference in mean recovery time)
- H1: μ1 ≠ μ2 (Significant difference in mean recovery time)

**Assumptions:**
- Groups are independent of each other.
- Normal distribution of the groups' means.
- Equal variances between the two groups (homoscedasticity). *

<!--s-->

## Common Hypothesis Tests | T-Test Calculation

**Calculation:**

To calculate the t-statistic, we use:

$ t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{ \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} }} $

where:

- $ \bar{x}_1, \bar{x}_2 $ are the sample means
- $ s_1^2, s_2^2 $ are the sample variances
- $ n_1, n_2 $ are the sample sizes

The t-statistic measures the difference between the two sample means relative to the variability in the data. 

We also need to calculate the degrees of freedom (df) for the t-distribution. Degrees of freedom can be defined as the maximum number of independent values that can vary in a statistical calculation. In this case, df is calculated as:

$df = n_1 + n_2 - 2$

Where $n_1$ and $n_2$ are the sample sizes. We subtract 2 because we have two samples.

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

**Scenario:** A group of 25 patients is measured for cholesterol levels before and after a particular treatment, aiming to evaluate the treatment's effect.

**Hypotheses:**
- H0: $d=0$ (No significant difference in mean cholesterol levels)
- H1: $d \ne 0$ (Significant difference in mean cholesterol levels)

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

The t-statistic measures the difference between the mean differences and the expected mean difference. Degrees of freedom can be calculated with $df = n - 1$.

<!--s-->

## Common Hypothesis Tests | T-Test (Paired) Decision

**Decision Process**

1. Using the t-distribution table with $df = n - 1$, compare the calculated t-value.
2. Reject H0 if the t-value is outside the range predicted for no effect.

<div class="col-centered">
<img src="https://www.researchgate.net/publication/12025083/figure/fig1/AS:352960891637763@1461163842564/Extract-of-the-t-table-The-first-column-lists-the-degrees-of-freedom-n-1-The.png">
</div>


<!--s-->

## Common Hypothesis Tests | Chi-Square Test Setup

**Scenario:** Observing if a die is fair, you roll it 60 times, resulting in:

| Side | Count |
| --- | --- |
| 1 | 11 |
| 2 | 9 |
| 3 | 10 |
| 4 | 10 |
| 5 | 10 |
| 6 | 10 |

**Hypotheses:**
- H0: The die is fair (expected frequency for each side is 10).
- H1: The die is not fair.

**Assumptions:**
- Observations are independent.
- All expected frequencies are at least 5.

<!--s-->

## Common Hypothesis Tests | Chi-Square Test Calculation

**Calculation:**

The chi-square statistic is calculated as:

$\chi^2 = \sum \frac{(O - E)^2}{E}$

where $O$ is the observed frequency and $E$ is the expected frequency. Degrees of freedom is $ df = (r - 1)(c - 1) $, where $r$ is the number of rows and $c$ is the number of columns.

Plugging in the values: 

$\chi^2 = \frac{(11 - 10)^2}{10} + \frac{(9 - 10)^2}{10} + \ldots$

<!--s-->

## Common Hypothesis Tests | Chi-Square Test Decision

**Decision Process**

1. Compare the $\chi^2$ value against the critical values from the chi-square distribution table with $df$
2. If $\chi^2 > \chi_{critical}$, reject H0.

<div class="col-centered">
<img src="https://www.scribbr.com/wp-content/uploads/2022/05/chi-square-distribution-table-critical-value.png">
</div>

<!--s-->

## Common Hypothesis Tests | One-Way ANOVA Setup

**Scenario:** Testing if there's a difference in the mean test scores across three teaching methods used across different groups.

**Hypotheses:**

- H0: $ \mu_1 = \mu_2 = \mu_3 $ (no significant difference among the group means)
- H1: At least one group mean is different.

**Assumptions**
- Responses for each group are normally distributed.
- Variances across groups are approximately equal.
    - A good rule of thumb is a ratio of the largest to the smallest variance less than 4.
- Observations are independent.

<!--s-->

## Common Hypothesis Tests | One-Way ANOVA Calculation

**Calculation:**

Sample variance is defined as: 

$ s^2 = \frac{SS}{df} = \frac{\sum (x - \bar{x})^2}{n - 1} $

where $SS$ is the sum of squares, $df$ is the degrees of freedom, $x$ is the data point, $\bar{x}$ is the sample mean, and $n$ is the sample size.

Anova calculates the F-statistic:

$ F = \frac{MS_{between}}{MS_{within}} $

where $MS_{between} = \frac{SS_{between}}{df_{between}}$ and $MS_{within} = \frac{SS_{within}}{df_{within}}$.

The F-statistic measures the ratio of the variance between groups to the variance within groups. 

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

If the assumptions for parametric tests are not met, non-parametric tests can be used. These tests are distribution-free and do not require the data to be normally distributed. These may make less powerful inferences than parametric tests but are more robust to violations of assumptions.

<div style="font-size: 0.8em">

| Predictor Variable    | Outcome Variable | Use in place of | Description |
|-----------------------|------------------|-------------------------|-----------------------------------------------------|
| Spearman’s r  | Quantitative | Pearson’s r | For quantitative variables with non-linear relation. |
| Chi square test | Categorical | Pearson’s r | For independence between categorical variables.  |
| Sign test  | Categorical  | One-sample t-test| For median tests with quantitive outcomes. |
| Kruskal–Wallis H  | Categorical  | ANOVA | For 3 or more groups of quantitative data |
| ANOSIM  | Categorical  | MANOVA| For 3 or more groups with 2+ quantitative variables. |
| Wilcoxon Rank-Sum | Categorical  | Independent t-test  | For 2 groups, different populations. |
| Wilcoxon Signed-rank  | Categorical  | Paired t-test| For 2 groups from the same population. |

<p style = "text-align: center; color: grey"> © Scribbr, 2024 </p>

</div>

<!--s-->

<!--s-->