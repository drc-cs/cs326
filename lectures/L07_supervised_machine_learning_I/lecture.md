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
## L.07 | Supervised Machine Learning I

</div>

<!--s-->

## Announcements

- P.01. I had several great conversations with groups on Tuesday (04.16) regarding their quarter project! 

  - I would like to chat with the remaining groups today. If I haven't spoken with your team yet and you would like to discuss your project prior to P.02, please let me know after lecture today.

- H.02. There was some confusion around the submission count for H.02. You get 3 submissions per homework assignment. 
  - If you locked in a low score by mistake (because you thought you had unlimited attempts), please come to office hours today to earn those points back. This is a one-time offer for H.02 only. 

- H.03. Homework 3 will be released on Tuesday (04.23). 
  - Fair warning: I'll be updating the server to only show you **which** tests fail, but not **how** they fail. 

<!--s-->

<div class = "header-slide">

# L.04 Attendance
Please check in.

https://join.iclicker.com/KVYY

</div>

<!--s-->

## Data Science Pipeline

Before diving into today's content, let's revisit the data science pipeline we've been discussing throughout the quarter. You will be expected to hit these components for your quarter project, so it's worth reviewing.

<div class = "col-wrapper">
<div class="c1" style = "width: 90%">

1. **Data Source (L.01 / L.02)**
    - L.02 covered common sources.
2. **Data Exploration (L.03 / L.04)**
    - L.03 covered summarization / visualization.
    - L.04 covered quantification / correlation.
    - L.05 covered hypothesis testing.
3. **Data Preprocessing (L.06)**
    - L.06 covered cleaning / transformation.
4. **Data Modeling**
    - L.07 (today) will cover modeling methods.
5. **Data Interpretation**
6. **Data Action**

</div>
<div class="c2" style = "width: 20%">

<img src="https://img.freepik.com/free-vector/location_53876-25530.jpg?size=338&ext=jpg&ga=GA1.1.523418798.1711497600&semt=ais" width="100%">
</div>
</div>

<!--s-->

## Question | Supervised Machine Learning (Pre-L.07)

On a scale of 1-10, how comfortable are you with the concept of supervised machine learning using the following methods:

1. k-Nearest Neighbors (KNN)
2. Linear Regression
3. Logistic Regression with Gradient Descent


<!--s-->

## L.07 | Supervised Machine Learning I

Today we will discuss the first of three of supervised machine learning lectures, focusing on fundamental algorithms for classification and regression.

Supervised machine learning tasks accept a feature matrix $X$ as input and predict a label $y$ as output. To achieve this aim, we will cover the following topics today:

1. Splitting Data into Sets
2. **Classification**: k-Nearest Neighbors (KNN)
3. **Regression**: Linear Regression
4. **Classification**: Logistic Regression with Gradient Descent

<!--s-->

## Splitting Data into Training, Validation, and Testing Sets

Splitting data into training, validation, and testing sets is crucial for model evaluation and selection.

- **Training Set**: Used for fitting the model.
- **Validation Set**: Used for parameter tuning and model selection.
- **Test Set**: Used to evaluate the model performance.

A good, general rule of thumb is to split the data into 70% training, 15% validation, and 15% testing. In practice, k-fold cross-validation is often used to maximize the use of data. We will discuss this method in future lectures.

<img src="https://miro.medium.com/v2/resize:fit:1160/format:webp/1*OECM6SWmlhVzebmSuvMtBg.png" width="500" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Chavan, 2023</p>

<!--s-->

## Methods of Splitting

- **Random Split**: Ensure you shuffle the data to avoid bias.
- **Stratified Split**: Used with imbalanced data to ensure each set reflects the overall distribution of the target variable.

```python
from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
```

<img src="https://miro.medium.com/v2/resize:fit:1160/format:webp/1*OECM6SWmlhVzebmSuvMtBg.png" width="500" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Chavan, 2023</p>

<!--s-->

## Classification vs Regression

### Classification

Classification is a supervised learning task where the goal is to predict the categorical class labels of new instances based on past observations. We'll discuss k-Nearest Neighbors (KNN) classification and logistic regression today.

### Regression

Regression is a supervised learning task where the goal is to predict a continuous value based on the input features. We'll also discuss linear regression today.

<!--s-->

<div class="header-slide">

# K-Nearest Neighbors (KNN) Classification

</div>

<!--s-->

## k-Nearest Neighbors (KNN) | Concept of KNN Classification

KNN is a non-parametric method used for classification (and regression!). The principle behind nearest neighbor methods is to find a predefined number of samples closest in distance to the new point, and predict the label from these using majority vote.

<iframe width = "100%" height = "100%" src="https://storage.googleapis.com/cs326-bucket/lecture_7/knn_setup.html" padding=2em;></iframe>

<!--s-->

## k-Nearest Neighbors (KNN) | What is it doing?

Given a new instance $ x' $, KNN classification computes the distance between $ x' $ and all other examples. The k closest points are selected and the predicted label is determined by majority vote.

<div class = "col-wrapper">
<div class="c1" style = "width: 50%; font-size: 0.8em;">

Euclidean Distance

$$ d(x, x') = \sqrt{\sum_{i=1}^n (x_i - x'_i)^2} $$

Jaccard Distance

$$ d(x, x') = 1 - \frac{|x \cap x'|}{|x \cup x'|} $$

Cosine Distance 

$$ d(x, x') = 1 - \frac{x \cdot x'}{||x|| \cdot ||x'||} $$

Hamming Distance (useful for strings!)

$$ d(x, x') = \frac{1}{n} \sum_{i=1}^n x_i \neq x'_i $$

</div>

<div class="c2 col-centered" style = "width: 60%;">

```python
from sklearn.neighbors import KNeighborsClassifier

# Default is Minkowski distance.
knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(X_train, y_train)
```
</div>
</div>

<!--s-->

## k-Nearest Neighbors (KNN) | Example

Given the following data points (X) and their corresponding labels (y), what is the predicted label for the point (3.5, 3.5) using KNN with k=3?

<div class = "col-wrapper">
<div class="c1 col-centered" style = "width: 50%">

<p style="margin-left: -10em;">A. 0<br><br>B. 1</p>

</div>
<div class="c2" style = "width: 50%">

<iframe width = "100%" height = "50%" src="https://storage.googleapis.com/cs326-bucket/lecture_7/knn_actual.html" padding=2em;></iframe>

```python
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
knn.predict([[3.5, 3.5]])
```

</div>
</div>

<!--s-->

## k-Nearest Neighbors (KNN) | Hyperparameters

- **Number of Neighbors (k)**: The number of neighbors to consider when making predictions.

- **Distance Metric**: The metric used to calculate the distance between points.

- **Weights**: Uniform weights give equal weight to all neighbors, while distance weights give more weight to closer neighbors.

- **Algorithm**: The algorithm used to compute the nearest neighbors. Some examples include Ball Tree, KD Tree, and Brute Force.

<!--s-->

## k-Nearest Neighbors (KNN) | Pros and Cons

### Pros

- Simple and easy to understand.
- No training phase.
- Can be used for both classification and regression.

### Cons

- Computationally expensive.
- Sensitive to the scale of the data.
- Requires a large amount of memory.

<!--s-->

## k-Nearest Neighbors (KNN) | Model Evaluation

To evaluate a binary classification model like this, we can use metrics such as accuracy, precision, recall, F1 score, and ROC-AUC.

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

| Metric | Formula |
| --- | --- |
| Accuracy | $\frac{TP + TN}{TP + TN + FP + FN}$ |
| Precision | $\frac{TP}{TP + FP}$ |
| Recall | $\frac{TP}{TP + FN}$ |
| F1 Score | $2 \times \frac{Precision \times Recall}{Precision + Recall}$ |
| ROC-AUC | Area under the ROC curve |

</div>
<div class="c2" style = "width: 50%">

<img src="https://assets-global.website-files.com/6266b596eef18c1931f938f9/64760779d5dc484958a3f917_classification_metrics_017-min.png" width="100%">
<p style="text-align: center; font-size: 0.6em; color: grey;">Source: EvidentlyAI</p>
</div>
</div>


<!--s-->

<div class="header-slide">

# Linear Regression

</div>

<!--s-->

## Linear Regression | Concept

Linear regression attempts to model the relationship between two or more variables by fitting a linear equation to observed data. The components to perform linear regression: 

$$ \widehat{y} = X\beta $$

Where $ \widehat{y} $ is the predicted value, $ X $ is the feature matrix, and $ \beta $ is the coefficient vector. The goal is to find the coefficients that minimize the error between the predicted value and the actual value.


<img src="http://www.stanford.edu/class/stats202/figs/Chapter3/3.1.png" width="600" style="margin: 0 auto; display: block;">


<!--s-->

## Linear Regression | Cost Function

The objective of linear regression is to minimize the cost function $ J(\beta) $:

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

$$ J(\beta) = \frac{1}{2m} \sum_{i=1}^m (\hat{y}_i - y_i)^2 $$

Where $ \hat{y} = X\beta $ is the prediction. This is most easily solved by finding the normal equation solution:

$$ \beta = (X^T X)^{-1} X^T y $$

The normal equation is derived by setting the gradient of $J(\beta) $ to zero. To add a bias term (aka a y intercept), we can add a column of ones to the feature matrix $ X $. Your homework will illustrate this concept.

</div>
<div class="c2" style = "width: 50%">

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

<img src="http://www.stanford.edu/class/stats202/figs/Chapter3/3.1.png" width="100%">

</div>
</div>

<!--s-->

## Linear Regression | Gradient Descent

For large datasets, the normal equation can be computationally expensive. Instead, we can use gradient descent to minimize the cost function iteratively. We'll talk about gradient descent within the context of logistic regression later.

<!--s-->

## Linear Regression | Model Evaluation

To evaluate a regression model, we can use metrics such as mean squared error (MSE), mean absolute error (MAE), mean absolute percentage error (MAPE), and R-squared.

<div style="font-size: 0.8em;">

**Mean Squared Error (MSE)**: The mean of the squared errors.

$$ MSE = \frac{1}{m} \sum_{i=1}^m (\hat{y}_i - y_i)^2 $$

**Mean Absolute Error (MAE)**: The mean of the absolute errors.

$$ MAE = \frac{1}{m} \sum_{i=1}^m |\hat{y}_i - y_i| $$

**Mean Absolute Percentage Error (MAPE)**: The mean of the absolute percentage errors.

$$ MAPE = \frac{1}{m} \sum_{i=1}^m \left| \frac{\widehat{y}_i - y_i}{y_i} \right| \times 100 $$

**R-squared**: The proportion of the variance in the dependent variable that is predictable from the independent variables.

$$ R^2 = 1 - \frac{\sum(\hat{y}_i - y_i)^2}{\sum(\bar{y} - y_i)^2} $$

</div>

<!--s-->

## Linear Regression | Pros and Cons

### Pros

- Simple and easy to understand.
- Fast to train.
- Provides a good, very interpretable baseline model.

### Cons

- Assumes a linear relationship between the features and the target variable.
- Sensitive to outliers.

<!--s-->

## Linear Regression | A Brief Note on Regularization

Regularization is a technique used to prevent overfitting by adding a penalty term to the cost function. The two most common types of regularization are L1 (Lasso) and L2 (Ridge) regularization.

**L1 Regularization**: Adds the absolute value of the coefficients to the cost function. This effectively performs feature selection by setting some coefficients to zero.

$$ J(\beta) = \frac{1}{2m} \sum_{i=1}^m (\hat{y}_i - y_i)^2 + \lambda \sum_{j=1}^n |\beta_j| $$

**L2 Regularization**: Adds the square of the coefficients to the cost function. This shrinks the coefficients, but does not set them to zero. This is useful when all features are assumed to be relevant.

$$ J(\beta) = \frac{1}{2m} \sum_{i=1}^m (\hat{y}_i - y_i)^2 + \lambda \sum_{j=1}^n \beta_j^2 $$

<!--s-->

<div class="header-slide">

# Logistic Regression with Gradient Descent

</div>


<!--s-->

## Logistic Regression | Concept

Logistic regression measures the relationship between the categorical dependent variable and one or more independent variables by estimating probabilities using a logistic function.

$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*G3imr4PVeU1SPSsZLW9ghA.png" width="400" style="margin: 0 auto; display: block;">
<span style="font-size: 0.8em; text-align: center; display: block; color: grey;">Joshi, 2019</span>

<!--s-->

## Logistic Regression | Formula

This model is based on the sigmoid function $\sigma(z)$:

$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

Where 

$$ z = X\beta $$

Note that $\sigma(z)$ is the probability that the dependent variable is 1 given the input $X$. Consider the similar form of the linear regression model:

$$ \hat{y} = X\beta $$

The key difference is that the output of logistic regression is passed through the sigmoid function to obtain the probability. This works because the sigmoid function maps any real number to the range [0, 1]. While linear regression predicts the value of the dependent variable, logistic regression predicts the probability that the dependent variable is 1.

<!--s-->

## Logistic Regression | No Closed-Form Solution

In linear regression, we can calculate the optimal coefficients $\beta$ directly. However, in logistic regression, we cannot do this due to the non-linearity (and thus, non-convexity) of the cost function.

Instead, we use gradient descent to minimize the cost function. Gradient descent is an optimization algorithm that iteratively updates the parameters to minimize the cost function, and forms the basis of many machine learning algorithms.

<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3BIDGdKjh88SLF0YTBz5oA.png" width="600" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Source: Medium</p>

<!--s-->

## Logistic Regression | Cost Function

The cost function used in logistic regression is the cross-entropy loss:

$$ J(\beta) = -\frac{1}{m} \sum_{i=1}^m [y_i \log(\widehat{y}_i) + (1 - y_i) \log(1 - \widehat{y}_i)] $$

$$ \widehat{y} = \sigma(X\beta) $$

Let's make sure we understand the intuition behind this cost function. If the true label ($y$) is 1, we want the predicted probability ($\widehat{y}$) to be close to 1. If the true label ($y$) is 0, we want the predicted probability ($\widehat{y}$) to be close to 0. The cost goes up as the predicted probability diverges from the true label.


<!--s-->

## Logistic Regression | Gradient Descent

To minimize $ J(\beta) $, we update $ \beta $ iteratively using the gradient of $ J(\beta) $:

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

$$ \beta := \beta - \alpha \frac{\partial J}{\partial \beta} $$

Where $ \alpha $ is the learning rate, and the gradient $ \frac{\partial J}{\partial \beta} $ is:

$$ \frac{\partial J}{\partial \beta} = \frac{1}{m} X^T (\sigma(X\beta) - y) $$


Where $ \sigma(X\beta) $ is the predicted probability, $ y $ is the true label, $ X $ is the feature matrix, $ m $ is the number of instances, $ \beta $ is the coefficient vector, and $ \alpha $ is the learning rate.

This is a simple concept that forms the basis of many gradient-based optimization algorithms, and is widely used in deep learning. 

Similar to linear regression -- if we want to include a bias term, we can add a column of ones to the feature matrix $ X $.

</div>
<div class="c2 col-centered" style = "width: 50%">

<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3BIDGdKjh88SLF0YTBz5oA.png" width="400" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Source: Medium</p>

</div>
</div>

<!--s-->

## Question | Gradient Descent

Okay, so let's walk through an example. Suppose you have already done the following: 

1. Obtained the current prediction ($\widehat{y}$) with $ \sigma(X\beta) $.
2. Calculated the gradient $ \frac{\partial J}{\partial \beta} $.

What do you do next?

<!--s-->

## Logistic Regression | Classifier

Once we have the optimal coefficients, we can use the logistic function to predict the probability that the dependent variable is 1. We can then use a threshold to classify the instance as 0 or 1. The following code snippet shows how to use the scikit-learn library to fit a logistic regression model and make predictions.


```python
from sklearn.linear_model import LogisticRegression

X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]
logistic_regression_model = LogisticRegression()
logistic_regression_model.fit(X_train, y_train)
logistic_regression_model.predict([[3.5, 3.5]])
```

```python
array([[0.3361201, 0.6638799]])
```

<!--s-->

## Question | Logistic Regression Output

Our logistic regression model was trained with $X = [[1, 2], [2, 3], [3, 4], [4, 5]]$ and $y = [0, 0, 1, 1]$. We then made a prediction for the point $[3.5, 3.5]$.

What does this output represent?

```python
array([[0.3361201, 0.6638799]])
```

<!--s-->

## Summary

- We discussed the importance of splitting data into training, validation, and test sets.
- We delved into k-Nearest Neighbors, Linear Regression, and Logistic Regression with Gradient Descent, exploring practical implementations and theoretical foundations.
- Understanding these foundational concepts is crucial for advanced machine learning and model fine-tuning! 

<!--s-->

## Question | Supervised Machine Learning (Post-L.07)

On a scale of 1-10, how comfortable are you with the concept of supervised machine learning using the following methods:

1. k-Nearest Neighbors (KNN)
2. Linear Regression
3. Logistic Regression with Gradient Descent


<!--s-->

<div class="header-slide">

# P.01 Feedback & P.02 Guidelines

</div>

<!--s-->

## P.01 Feedback

We would prefer to give feedback on P.01 for all groups in person prior to P.02. If you have not met with me yet, or want to discuss your projects more with either Chongyang or myself, please send us an email! You are also welcome to come to office hours any Thursday.


<div class = "col-wrapper">
<div class="c1" style = "width: 50%;">

### Groups We Have Met With

1. Dumbledore's Army
2. Beautiful Soups
3. Data Sciencers
4. Andromeda
5. Data Pipeliners

</div>
<div class="c2" style = "width: 50%;">

### Groups We Have Not Met With

1. Group 326
2. jake
3. Data Dogs
4. hello world
5. Segmentation Fault
</div>
</div>

<!--s-->

## P.02 Guidelines

Lots of great ideas for projects! Now, we're going to adjust them to fit into the Data Science Pipeline. Specifically, each project must include:

<div style="font-size: 0.6em; padding: 1em;">

1. **Data Source**: 
  
      Where are you getting your data from?
2. **Data Exploration**: 

      How are you summarizing and visualizing your data? If you do some hypothesis testing or correlation analysis, that is excellent.
3. **Data Preprocessing**: 

      How are you cleaning and transforming your data?
4. **Data Modeling**: 

      What models are you using? The most straightforward approach here is to create a prediction task and use supervised ML to solve it. Recommendation models are welcome, but performance must be quantifiable for Data Interpretation (this is usually done by making your recommendation model a prediction task).

5. **Data Interpretation**: 

      How are you interpreting your results?
6. **Data Action**: 

      What are you doing with your results?
</div>