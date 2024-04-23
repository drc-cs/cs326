---
title: COMP_SCI 326
separator: <!--s-->
verticalSeparator: <!--v-->
theme: serif
revealOptions:
    transition: 'none'
---

<div class="header-slide">

# Introduction to the Data Science Pipeline
## L.09 | Supervised Machine Learning III

</div>

<!--s-->

## Announcements



<!--s-->

<div class = "header-slide">

# L.04 Attendance
Please check in.

https://join.iclicker.com/KVYY

</div>

<!--s-->

## L.08 | Supervised Machine Learning III

In today’s lecture, we will delve deeper into some fundamental concepts and algorithms underpinning supervised machine learning. 

Specifically, we will explore:

1. Decision Trees (Classic)
2. Ensemble Models


<div class="header-slide">

# Decision Trees

</div>

<!--s-->

## Decision Trees | Overview

**Decision Trees** are a non-parametric supervised learning method used for classification and regression tasks. They are simple to **understand** and **interpret**, making them a popular choice for exploratory data analysis.

A decision tree is a tree-like structure where each internal node represents a feature or attribute, each branch represents a decision rule, and each leaf node represents the outcome of the decision.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220831135057/CARTClassificationAndRegressionTree.jpg" height="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks, 2024</p>

<!--s-->

## Decision Trees | ID3 Algorithm

The construction of a decision tree involves selecting the best feature to split the dataset at each node. One of the most common algorithms for constructing decision trees is the ID3 algorithm.

**ID3 Algorithm**:

1. Calculate the entropy of the target variable.
2. For each feature, calculate the information gained by splitting the data.
3. Select the feature with the highest information gain as the new node.

The ID3 algorithm recursively builds the decision tree by selecting the best feature to split the data at each node.

<!--s-->

## Decision Trees | Entropy

**Entropy** is a measure of the impurity or disorder in a dataset. The entropy of a dataset is 0 when all instances belong to the same class and is maximized when the instances are evenly distributed across all classes. It is defined as: 

$$ H(S) = - \sum_{i=1}^{n} p_i \log_2(p_i) $$

Where:

- $H(S)$ is the entropy of the dataset $S$.
- $p_i$ is the proportion of instances in class $i$ in the dataset.
- $n$ is the number of classes in the dataset.

<img src="https://miro.medium.com/v2/resize:fit:565/1*M15RZMSk8nGEyOnD8haF-A.png" width="40%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Provost, Foster; Fawcett, Tom. </p>

<!--s-->

## Decision Trees | Information Gain

**Information Gain** is a measure of the reduction in entropy achieved by splitting the dataset on a particular feature. IG is the difference between the entropy of the parent dataset and the weighted sum of the entropies of the child datasets.

$$ IG(S, A) = H(S) - H(S|A)$$

Where:

- $IG(S, A)$ is the information gain of splitting the dataset $S$ on feature $A$.
- $H(S)$ is the entropy of the parent dataset.
- $H(S | A)$ is the weighted sum of the entropies of the child datasets.


<br><br>
<img src="https://miro.medium.com/max/954/0*EfweHd4gB5j6tbsS.png" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">KDNuggets</p>


<!--s-->

## Decision Trees | ID3 Pseudo-Code

```text
ID3 Algorithm:
1. If all instances in the dataset belong to the same class, return a leaf node with that class.
2. If the dataset is empty, return a leaf node with the most common class in the parent dataset.
3. Calculate the entropy of the dataset.
4. For each feature, calculate the information gain by splitting the dataset.
5. Select the feature with the highest information gain as the new node.
6. Recursively apply the ID3 algorithm to the child datasets.
```

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220831135057/CARTClassificationAndRegressionTree.jpg" height="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks, 2024</p>


<!--s-->

## Decision Trees | Overfitting

**Overfitting** is a common issue with decision trees, where the model captures noise in the training data rather than the underlying patterns. Overfitting can lead to poor generalization performance on unseen data.

**Strategies to Prevent Overfitting**:

1. **Pruning**: Remove branches that do not improve the model's performance on the validation data.
    - This is similar to L1 regularization in linear models!
2. **Minimum Samples per Leaf**: Set a minimum number of samples required to split a node.
3. **Maximum Depth**: Limit the depth of the decision tree.
4. **Maximum Features**: Limit the number of features considered for splitting.


<!--s-->

<div class="header-slide">

# Ensemble Models

</div>

<!--s-->

## Ensemble Models | Overview

**Ensemble Models** combine multiple individual models to improve predictive performance. The key idea behind ensemble models is that a group of weak learners can come together to form a strong learner. Ensemble models are widely used in practice due to their ability to reduce overfitting and improve generalization.

We will discuss three types of ensemble models:

1. **Bagging**: Bootstrap Aggregating
2. **Boosting**: Sequential Training
3. **Stacking**: Meta-Learning

<!--s-->

## Ensemble Models | Bagging

**Bagging (Bootstrap Aggregating)** is an ensemble method that involves training multiple models on different subsets of the training data and aggregating their predictions. The key idea behind bagging is to reduce variance by averaging the predictions of multiple models.

**Intuition**: By training multiple models on different subsets of the data, bagging reduces the impact of outliers and noise in the training data. The final prediction is obtained by averaging the predictions of all models.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230731175958/Bagging-classifier.png" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Bagging | Example: Random Forests

**Random Forests** are an ensemble learning method that combines multiple decision trees to create a more robust and accurate model. Random Forests use bagging to train multiple decision trees on different subsets of the data and aggregate their predictions.

**Key Features of Random Forests**:
- Each decision tree is trained on a random subset of the features.
- The final prediction is obtained by averaging the predictions of all decision trees.

Random Forests are widely used in practice due to their robustness, scalability, and ability to handle high-dimensional data.

<img src="https://tikz.net/janosh/random-forest.png" height="40%" style="margin: 0 auto; display: block; padding: 10">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Boosting

**Boosting** is an ensemble method that involves training multiple models sequentially, where each model learns from the errors of its predecessor.

**Intuition**: By focusing on the misclassified instances in each iteration, boosting aims to improve the overall performance of the model. The final prediction is obtained by combining the predictions of all models.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210707140911/Boosting.png" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Boosting | Example: AdaBoost

**AdaBoost (Adaptive Boosting)** is a popular boosting algorithm that combines multiple weak learners to create a strong learner. AdaBoost works by assigning weights to each instance in the training data and adjusting the weights based on the performance of the model.

**Key Features of AdaBoost**:

1. Train a weak learner on the training data.
2. Increase the weights of misclassified instances.
3. Train the next weak learner on the updated weights.
4. Repeat the process until a stopping criterion is met.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210707140911/Boosting.png" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Boosting | Example: Gradient Boosting

**Gradient Boosting** is another popular boosting algorithm that combines multiple weak learners to create a strong learner. Gradient Boosting works by fitting a sequence of weak learners to the residuals of the previous model. This differs from AdaBoost, which focuses on the misclassified instances.

**Key Features of Gradient Boosting**:

1. Fit a weak learner to the training data.
2. Compute the residuals of the model.
3. Fit the next weak learner to the residuals.
4. Repeat the process until a stopping criterion is met.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200721214745/gradientboosting.PNG" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Stacking

**Stacking (Stacked Generalization)** is an ensemble method that combines multiple models using a meta-learner. The key idea behind stacking is to train multiple base models on the training data and use their predictions as input to a meta-learner.

**Intuition**: By combining the predictions of multiple models, stacking aims to improve the overall performance of the model. The final prediction is obtained by training a meta-learner on the predictions of the base models.

<img src="https://miro.medium.com/v2/resize:fit:946/1*T-JHq4AK3dyRNi7gpn9-Xw.png" height="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Setunga, 2020</p

<!--s-->

## Ensemble Models | Stacking | Example

**Stacked Generalization** involves training multiple base models on the training data and using their predictions as input to a meta-learner. The meta-learner is trained on the predictions of the base models to make the final prediction.

**Key Features of Stacked Generalization**:

1. Train multiple base models on the training data.
2. Use the predictions of the base models as input to the meta-learner.
3. Train the meta-learner on the predictions of the base models.
4. Use the meta-learner to make the final prediction.

Stacking is often trained end-to-end, where the base models and meta-learner are trained simultaneously to optimize the overall performance.

<img src="https://miro.medium.com/v2/resize:fit:946/1*T-JHq4AK3dyRNi7gpn9-Xw.png" height="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Setunga, 2020</p