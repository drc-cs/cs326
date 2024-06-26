---
title: COMP_SCI 326
separator: <!--s-->
verticalSeparator: <!--v-->
theme: serif
revealOptions:
    transition: 'none'
---

<div class = "col-wrapper">
<div class="c1 col-centered">

<div style="font-size: 0.8em; left: 0; width: 70%; position: absolute;">

# Introduction to the Data Science Pipeline
## L.15 | Quiz Review

</div>

</div>


<div class="c2 col-centered" style = "bottom: 0; right: 0; width: 100%; padding-top: 20%;">

</div>
</div>

<!--s-->

<div class = "header-slide">

# L.15 Attendance
Please check in.

https://join.iclicker.com/KVYY

</div>

<!--s-->

# Announcements

- [H.04](https://github.com/drc-cs/cs326/tree/main/homeworks/H04) is due on 05.21.2024
    - Several of you have already submitted this assignment. Great job! 🎉

- Quiz on 05.23.2024
    - The quiz will cover all material up to and including L.14.
    - Anything on the homework and lectures is fair game, but the quiz will be multiple choice and short answer. Focus on the overall concepts. You will not be expected to memorize any formulas. Follow the study guide on 05.16 and you will be well-prepared!

- P.03 & P.04 Rubrics will be posted by 05.21.2024.
    - Refer to [P.02](https://drc-cs.github.io/cs326/lectures/L10_recommendation_modeling/#/26) for an outline of expectations. Expectations for P.03 (final presentation) and P.04 (technical writeup) will follow this general format.

<!--s-->

# Lockdown Browser (Canvas)

1. [Download Lockdown Browser](https://download.respondus.com/lockdown/download7.php?id=171646780).
2. Install the browser on your computer.
3. Ensure that you can log in to your Northwestern University Canvas account using the browser.
4. Take the [practice](https://canvas.northwestern.edu/courses/211880/quizzes/238854) quiz on Canvas to ensure that everything is working correctly.

You will then be able to access the quiz on Canvas and take the quiz on your computer. **Note**: I have enabled the Monitoring feature for students that are unable to join us in-person, but I ask that everyone use it to ensure a fair testing environment.

<!--s-->

<div class="header-slide">

# Quiz Review

</div>

<!--s-->

# L.02

- Be able to identify structured, semi-structured, and unstructured data, as well as the advantages and disadvantages of each. [[🔗]](https://drc-cs.github.io/cs326/lectures/L02_data_sources/#/16)

- Given a scenario with missing data, pick the appropriate method to handle it. [[🔗]](https://drc-cs.github.io/cs326/lectures/L02_data_sources/#/25)

- Be able to describe a visual or summary process for identifying outliers in a dataset. [[🔗]](https://drc-cs.github.io/cs326/lectures/L02_data_sources/#/27)

<!--s-->

# H.01

- Understand the roles of conda, GitHub, vscode, and pytest in your development workflow. [[🔗]](https://drc-cs.github.io/cs326/lectures/L02_data_sources/#/4)

<!--s-->

# L.03

- Identify skew (positive, negative). [[🔗]](https://drc-cs.github.io/cs326/lectures/L03_exploratory_data/#/8)

- Identify kurtosis (leptokurtic, mesokurtic, platykurtic). [[🔗]](https://drc-cs.github.io/cs326/lectures/L03_exploratory_data/#/10)

- Differentiate between boxplots and violin plots. [[🔗]](https://drc-cs.github.io/cs326/lectures/L03_exploratory_data/#/18)

<!--s-->

# L.04

- Differentiate when to use Pearson or Spearman correlation, and how to interpret their results (negative / positive / no relationship). [[🔗]](https://drc-cs.github.io/cs326/lectures/L04_correlation_association/#/8)

- Identify a scenario as Simpson's Paradox. [[🔗]](https://drc-cs.github.io/cs326/lectures/L04_correlation_association/#/13)

<!--s-->

# L.05 & H.02

- Construct an A/B Test to test a hypothesis. [[🔗]](https://drc-cs.github.io/cs326/lectures/L05_ab_testing_basic_stats/#/10)

- Define hypothesis testing for a scenario in terms of $H_0$ and $H_1$. [[🔗]](https://drc-cs.github.io/cs326/lectures/L05_ab_testing_basic_stats/#/13)

- Provided a scenario, identify the type of test to use (t-test, paired t-test, chi-squared test, anova). [[🔗]](https://drc-cs.github.io/cs326/lectures/L05_ab_testing_basic_stats/#/16)

- Know the non-parametric analogs to the tests we covered in lecture. [[🔗]](https://drc-cs.github.io/cs326/lectures/L05_ab_testing_basic_stats/#/33)


<!--s-->

# L.06

- Define feature engineering in the context of machine learning applications. [[🔗]](https://drc-cs.github.io/cs326/lectures/L06_data_preprocessing/#/9)

- Define and be able to identify data that has been scaled (min-max, standard). [[🔗]](https://drc-cs.github.io/cs326/lectures/L06_data_preprocessing/#/16)

- Describe the curse of dimensionality and how it affects machine learning models. [[🔗]](https://drc-cs.github.io/cs326/lectures/L06_data_preprocessing/#/25)

- Choose a method for dimensionality reduction (Feature Selection, Feature Sampling, Random Projection, or PCA) and detail how it works. [[🔗]](https://drc-cs.github.io/cs326/lectures/L06_data_preprocessing/#/25)

<!--s-->

# L.07

- Define the terms: training set, validation set, and test set and their primary uses. [[🔗]](https://drc-cs.github.io/cs326/lectures/L07_supervised_machine_learning_I/#/6)

- Identify a scenario as a classification or regression problem. [[🔗]](https://drc-cs.github.io/cs326/lectures/L07_supervised_machine_learning_I/#/8)

- Explain the KNN algorithm and how it works. [[🔗]](https://drc-cs.github.io/cs326/lectures/L07_supervised_machine_learning_I/#/10)

- Explain where the normal equation for linear regression comes from. [[🔗]](https://drc-cs.github.io/cs326/lectures/L07_supervised_machine_learning_I/#/18)

- Be able to identify L1 and L2 regularization and explain at a high level how they work. [[🔗]](https://drc-cs.github.io/cs326/lectures/L07_supervised_machine_learning_I/#/22)

- Understand the intuition behind the cross-entropy loss function. [[🔗]](https://drc-cs.github.io/cs326/lectures/L07_supervised_machine_learning_I/#/27)

<!--s-->

# H.03

- Be able to look at code for logistic regression gradient descent and identify missing or incorrect components. [[🔗]](https://drc-cs.github.io/cs326/lectures/L07_supervised_machine_learning_I/#/28)

- Provided with a **simple** numpy operation, identify the shape of the output. This may include an axis argument. [[🔗]](https://numpy.org/doc/stable/user/basics.broadcasting.html)

<!--s-->

# L.08

- Explain ROC curves (axes) and what the AUC represents (random / not-random). [[🔗]](https://drc-cs.github.io/cs326/lectures/L08_supervised_machine_learning_II/#/5)

- Explain the value of a softmax function in the context of a multi-class classification problem. [[🔗]](https://drc-cs.github.io/cs326/lectures/L08_supervised_machine_learning_II/#/16)

<!--s-->

# L.09

- Explain the ID3 algorithm and how it works at a high level (understand entropy & information gain). [[🔗]](https://drc-cs.github.io/cs326/lectures/L09_supervised_machine_learning_III/#/8)

- Be able to identify a decision tree as overfitting or underfitting. [[🔗]](https://drc-cs.github.io/cs326/lectures/L09_supervised_machine_learning_III/#/13)

- Differentiate between and be able to explain different ensemble modeling methods (bagging, boosting, stacking). [[🔗]](https://drc-cs.github.io/cs326/lectures/L09_supervised_machine_learning_III/#/19)

<!--s-->

# L.10

- Differentiate between content and collaborative filtering. [[🔗]](https://drc-cs.github.io/cs326/lectures/L10_recommendation_modeling/#/5)

- Explain the intuition behind matrix factorization in collaborative filtering. [[🔗]](https://drc-cs.github.io/cs326/lectures/L10_recommendation_modeling/#/10)

<!--s-->

# L.11 & H.04

- Explain the intuition behind partitional clustering / K-means algorithm (and know where it fails!). [[🔗]](https://drc-cs.github.io/cs326/lectures/L11_unsupervised_machine_learning/#/15)

- Explain the intuition behind density-based clustering / DBScan algorithm (and know where it fails!). [[🔗]](https://drc-cs.github.io/cs326/lectures/L11_unsupervised_machine_learning/#/25)

<!--s-->

# L.13

- Identify additive vs multiplicative decomposition in time series data. [[🔗]](https://drc-cs.github.io/cs326/lectures/L13_time_series/#/8)

- Know the value of differencing in time series data (e.g. what does it do, and why is that important?). [[🔗]](https://drc-cs.github.io/cs326/lectures/L13_time_series/#/11)

- Look at ACF / PACF plots and determine what order of AR or MA to use in an ARIMA model. [[🔗]](https://drc-cs.github.io/cs326/lectures/L13_time_series/#/26)

- Explain walk-forward validation in the context of time series data. [[🔗]](https://drc-cs.github.io/cs326/lectures/L13_time_series/#/30)

<!--s-->

# L.14

- Explain the benefits of word embeddings over one-hot encoding. [[🔗]](https://drc-cs.github.io/cs326/lectures/L14_natural_language_processing/#/17)

- Differentiate between a CBOW and Skip-Gram model. [[🔗]](https://drc-cs.github.io/cs326/lectures/L14_natural_language_processing/#/18)

- Explain what a vector database is and how it can be used in a RAG application. [[🔗]](https://drc-cs.github.io/cs326/lectures/L14_natural_language_processing/#/22)

<!--s-->

<div class = "col-wrapper">
<div class="c1 col-centered" style = "width: 70%">

<div style="font-size: 0.7em;">

# H.04 | clustering_and_time_series.py
Due: 05.21.2024

</div>

</div>
<div class="c2 col-centered" style = "width: 30%">
<div>
<img src="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*WunYbbKjzdXvw73a4Hd2ig.gif" height="100%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Seo, 2023</p>
</div>
</div>
</div>

<!--s-->

