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
## L.16 | Storytelling and Ethics

</div>

</div>

<div class="c2 col-centered" style = "bottom: 0; right: 0; width: 100%; padding-top: 20%;">

<iframe src="https://lottie.host/embed/02b9bf18-7fb2-454b-b5d4-5196357a8ecf/YTCoN4ouWw.json"></iframe>

</div>
</div>

<!--s-->

# Announcements

- [H.04](https://github.com/drc-cs/cs326/tree/main/homeworks/H04) due tonight (05.21.2024)
    - Most of you have already submitted this assignment. Great job! 🎉

- Quiz on 05.23.2024
    - The quiz will cover all material up to and including L.14.
    - Anything on the homework and lectures is fair game, but the quiz will be multiple choice and short answer. Focus on the overall concepts. You will not be expected to memorize any formulas. Follow the study guide on 05.16 and you will be well-prepared!

<!--s-->

<div class = "header-slide">

# L.16 Attendance
Please check in.

https://join.iclicker.com/KVYY

</div>

<!--s-->

<div class="header-slide">

# L.16 | Storytelling and Ethics

</div>

<!--s-->

## Agenda

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### **Part 1**: Storytelling
- Importance of storytelling in data science.
- What every good data story should include.
- What every good presentation should include.

</div>
<div class="c2" style = "width: 50%; border-left: 1px solid black;">

### **Part 2**: Ethics of Data Science

- Consent for Data
- Privacy
- Examining Bias
- Who is Held Accountable?
- Radicalization and Misinformation

</div>
</div>

<!--s-->

<div class = "col-wrapper">
<div class="c1 col-centered">

<div>

# Storytelling

</div>

</div>

<div class="c2 col-centered" style="width: 100%;">

<iframe src="https://lottie.host/embed/be87d8ec-8c45-4e5f-8fa5-a7c51ba95111/AeEwvQMzRj.json" width="100%" height="100%"></iframe>

</div>
</div>

<!--s-->

## Storytelling | Importance

Data science is not just about the results. It is about the **story** that the data tells.

An often-overlooked aspect of data science is the ability to **communicate** and **convince** others of the results of your analysis.

<img src="https://justinsighting.com/wp-content/uploads/2016/05/housing-price-and-square-feet-predicted.jpg" style="margin: 0 auto; display: block; width: 50%;">
<p style="text-align: center; font-size: 0.6em; color: grey;">JustInsighting, 2024</p>

<!--s-->

## Storytelling | Every Data Story Must Include ...

1. **Background of Problem**

2. **Statement of Assumptions**

3. **Motivation for Solving the Problem**

4. **Explanation of your Analysis**

5. **Declared Limitations & Future Improvements**

<!--s-->

## Storytelling | Background of Problem

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### What is the problem you are trying to solve?

We are trying to predict the price of a house based on its square footage.

</div>
<div class="c2" style = "width: 50%">

<img src="https://justinsighting.com/wp-content/uploads/2016/05/housing-price-and-square-feet-predicted.jpg" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">JustInsighting, 2024</p>

</div>
</div>


<!--s-->

## Storytelling | Statement of Assumptions

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### What assumptions are you making in your analysis?

We assume that the data we are training on represents the general population.

### What are the implications of these assumptions?

If this assumption is incorrect, the model may fail to generalize.

</div>
<div class="c2" style = "width: 50%">
<img src="https://justinsighting.com/wp-content/uploads/2016/05/housing-price-and-square-feet-predicted.jpg" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">JustInsighting, 2024</p>

</div>
</div>


<!--s-->

## Storytelling | Motivation for Solving the Problem

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### Why is it important to solve this problem?

Predicting the price of a house can help buyers and sellers make informed decisions.

</div>
<div class="c2" style = "width: 50%">

<img src="https://justinsighting.com/wp-content/uploads/2016/05/housing-price-and-square-feet-predicted.jpg" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">JustInsighting, 2024</p>

</div>
</div>

<!--s-->

## Storytelling | Explanation of your Analysis

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### How did you analyze the data?

We used linear regression to predict the price of a house based on its square footage.

### How do you interpret the results?

Our linear model predicts that the price of a house increases by **$100 per square foot**. Note that we don't report MSE or RMSE here.

</div>
<div class="c2" style = "width: 50%">

<img src="https://justinsighting.com/wp-content/uploads/2016/05/housing-price-and-square-feet-predicted.jpg" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">JustInsighting, 2024</p>

</div>
</div>

<!--s-->

## Storytelling | Declared Limitations & Future Improvements

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### What are the limitations of your analysis?

The model may not be accurate for houses with unique features, such as a swimming pool.

### How can you improve the analysis in the future?

You can collect more data on houses with swimming pools to improve the accuracy of the model.

</div>
<div class="c2" style = "width: 50%">

<img src="https://justinsighting.com/wp-content/uploads/2016/05/housing-price-and-square-feet-predicted.jpg" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">JustInsighting, 2024</p>

</div>
</div>

<!--s-->

## Storytelling Recap | Every Data Story Must Include ...

1. **Background of Problem**

2. **Statement of Assumptions**

3. **Motivation for Solving the Problem**

4. **Explanation of your Analysis**

5. **Declared Limitations & Future Improvements**

<!--s-->

## Storytelling | Every Good **Presentation** Must Include ...

1. Clear and concise slides

2. A compelling narrative

3. Energy and confidence 

<!--s-->

## Storytelling | Clear and Concise Slides

### What makes a slide **clear** and **concise**?

- Use bullet points to summarize key points.
- Use visuals to illustrate complex concepts.
- Use a consistent font and color scheme.

<!--s-->

## Storytelling | A Compelling Narrative

### What makes a narrative **compelling**?

- Tell a story that engages the audience.
- Use examples and anecdotes to illustrate key points.
- Use humor and emotion to connect with the audience.

<!--s-->

## Storytelling | Energy and Confidence

### How can you project **energy** and **confidence**?

- Speak clearly and with sufficient volume.
- Make eye contact with the audience.
- Use body language to emphasize key points.

<!--s-->

## Storytelling | Every Good **Presentation** Must Include ...

1. Clear and concise slides

2. A compelling narrative

3. Energy and confidence 

<!--s-->

<div class = "col-wrapper">
<div class="c1 col-centered" style="width: 60%;">

<div>

# Ethics of Data Science

</div>

</div>

<div class="c2 col-centered" style="width: 40%;">

<iframe src="https://lottie.host/embed/0059f4db-7136-402f-89a4-36b9230ca9aa/Jb6iMtHqzR.json" width="100%" height="100%"></iframe>

</div>
</div>

<!--s-->

## Ethics of Data Science | Topics

1. Consent for Data
2. Privacy
3. Examining Bias
4. Accountability
5. Radicalization and Misinformation

<!--s-->

## Ethics of Data Science | Consent for Data

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### Why is consent important in data science?

- To protect the privacy of individuals.
- To ensure that data is used ethically and responsibly.

### How can you obtain consent for data?

- Inform individuals about how their data will be used.
- Obtain explicit consent before collecting or using data.

</div>
<div class="c2 col-centered" style = "width: 50%">
<div>
<img src="https://www.euractiv.com/wp-content/uploads/sites/2/2024/02/shutterstock_1978079195-800x450.jpg" style="margin: 0 auto; display: block; width: 100%; border-radius: 5px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Euractiv, 2024</p>
</div>
</div>
</div>


<!--s-->

## Ethics of Data Science | Consent for Data

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### **Opt-in** vs. **Opt-out**

- Opt-in: Individuals must actively consent to the use of their data.
- Opt-out: Individuals must actively decline the use of their data.

### **Granular** vs. **Broad**

- Granular: Individuals can choose how their data is used.
- Broad: Individuals have limited control over how their data is used.

</div>
<div class="c2 col-centered" style = "width: 50%">
<div>
<img src="https://www.euractiv.com/wp-content/uploads/sites/2/2024/02/shutterstock_1978079195-800x450.jpg" style="margin: 0 auto; display: block; width: 100%; border-radius: 5px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Euractiv, 2024</p>
</div>
</div>
</div>

<!--s-->

## Ethics of Data Science | Privacy


<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### Why is privacy important in data science?

- To protect the personal information of individuals.
- To prevent the misuse of data for malicious purposes.

### How can you protect privacy in data science?

- Anonymize data to remove personally identifiable information.
- Encrypt data to prevent unauthorized access.
- Limit access to data to authorized individuals.

</div>
<div class="c2 col-centered" style = "width: 50%">
<div>
<img src="https://images.theconversation.com/files/218904/original/file-20180514-100697-ig8lqn.jpg?ixlib=rb-4.1.0&q=45&auto=format&w=926&fit=clip" style="margin: 0 auto; display: block; width: 100%; border-radius: 5px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">SBPhotos, 2018</p>
</div>
</div>
</div>

<!--s-->

## Ethics of Data Science | Privacy Compliance with Regulations

<div style="font-size: 0.8em;">

**General Data Protection Regulation**: GDPR is a European Union regulation that protects the personal data of EU citizens and residents.

**Fair Credit Reporting Act**: Provides data protection for the personal financial information collected by credit agencies.

**The Privacy Act of 1974**: Prevents the federal government from making unauthorized disclosure of personal information under its control.

**Computer Fraud and Abuse Act**: A federal anti-hacking statute that prohibits the unauthorized use of protected computers without prior authorization, including smartphones or other devices connected to the internet.

**Children's Online Privacy Protection Act**: COPPA imposes requirements on online services directed at children under 13, as well as those that knowingly collect information from children under the age of 13. These entities must post their privacy policies, have an opt-out option, and provide certain parental controls.

**Financial Monetization Act**: Requires financial institutions to explain their information-sharing practices to their customers and to safeguard sensitive customer information.

**Health Information Portability and Accountability Act**: HIPAA assures that an individual’s health information is properly protected by setting use and disclosure standards.

</div>

<!--s-->

## Ethics of Data Science | Examining Bias

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### Why is bias a concern in data science?

- Bias can lead to unfair or discriminatory outcomes.
- Bias can perpetuate stereotypes and reinforce inequality.

### How can you identify and address bias in data science?

- Examine the data for bias in the collection or labeling process.
- [Fairness-aware machine learning](https://en.wikipedia.org/wiki/Fairness_(machine_learning)) to mitigate bias.

</div>
<div class="c2 col-centered" style = "width: 50%">
<div>
<img src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gender-before-after.width-1000.format-webp.webp" style="margin: 0 auto; display: block; width: 100%; border-radius: 5px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Google, 2018</p>
</div>
</div>
</div>

<!--s-->

## Ethics of Data Science | Accountability

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

### **Scenario**: A self-driving car causes an accident, resulting in injury or death.

### Who should be held accountable?

- The manufacturer of the car.
- The developer of the software.
- The owner of the car.
- The government.

</div>
<div class="c2 col-centered" style = "width: 50%">
<div>
<img src="https://dda.ndus.edu/ddreview/wp-content/uploads/sites/18/2021/10/selfDriving.png" style="margin: 0 auto; display: block; width: 100%; border-radius: 5px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Nygard, 2021</p>
</div>


</div>
</div>


<!--s-->

<div class = "col-wrapper">
<div class="c1" style = "width: 70%; font-size: 1em;">

## Ethics of Data Science | Radicalization and Misinformation

### How can data science be used to **radicalize** and **misinform** people?

- By manipulating data to support false narratives.
- By targeting vulnerable populations with misleading information.
- By hyper-recommending content that reinforces extremist views.

### How can you combat radicalization and misinformation in data science?

- Fact-checking and verifying sources.
- Promoting trust, media literacy, and critical thinking.
- Implementing algorithms that prioritize accuracy and credibility.

</div>
<div class="c2 col-centered" style = "width: 30%">

<div>
<img src="https://p16-va-tiktok.ibyteimg.com/obj/musically-maliva-obj/4a2a1776a08f761c6464f596c0c5e8e6.png" style="margin: 0 auto; display: block; width: 50%; border-radius: 5px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">TikTok, 2024</p>
</div>
</div>
</div>

<!--s-->

## Ethics of Data Science | Recap

1. Consent for Data
2. Privacy
3. Examining Bias
4. Accountability
5. Radicalization and Misinformation

<!--s-->



<div class = "col-wrapper">
<div class="c1 col-centered" style = "width: 70%">

<div>

# **Unstructured Time**

<div style="font-size: 0.7em;">

# H.04 | clustering_and_time_series.py
- **Due: 05.21.2024**
# Quiz Review
- **On: 05.23.2024**
# P.03 / P.04 | Project Presentations
- **Due: 05.28.2024**

</div>
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