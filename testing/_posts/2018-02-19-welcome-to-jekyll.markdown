---
layout:     post
title:      Developing an Aggregate Metric for Measuring District Court Performance
date:       2018-02-18
summary:   
categories: jekyll update
---

As a part of my undergraduate thesis, I have been working on collecting a large sample of court case summaries of Indian district courts. While collecting the data is a ~~challenging task~~ nightmare, and deserves a blog post in itself, let that be reserved for some other time.

The point is, we have a sample for more than 350 districts, and the sample is reasonably large - on an average there are more than 11000 disposed cases per district. Information on a particular case includes the case act, case section, casetype, hearing dates, petitioners, respondents, etc.

## Anomaly Detection

How do we make sense of this data? Specifically, what part of the data do we look at, to draw comparisons across various district courts, on various metrics, to come up with useful insights? We decided to have a focus on case duration time. Duration time of a case, is defined as the time gap (in days) between the first hearing date, and the final decision date. This choice was made for two reasons - first, the time that a court takes in disposing off a case is particularly useful metric for gauging performance, and secondly, the metric is numeric, so it makes performing analysis much easier for us.

So around 6-7 odd metrics were chosen along which the distribution of the case duration time was analysed. These are - 

* Mean Case Duration Time
* Coefficient of Variation (Ratio of Standard Deviation and Mean)
* Tail Bounds (Percentage of cases taking more time than X) 
	* 3 Months
	* 6 Months
	* 1 Year		
	* 3 Years
* Zero Day Disposal Percentage (Percentage of cases for which final decision happens on the first hearing date)

Zero Day Disposal Percentage may not be the best metric out there because a lot of cases simply get transferred, that transfer is said to be the final decision, and the act of transferring does not speak much about the merit of the court itself; however, it is still worth analysing districts along this.

We have also applied the convention throughout that the lower the time taken to dispose off a case, the better. So low mean case duration time is good, low percentage tail bounds is good, etc. Keep in mind that this is a statistical judgement, and not a value judgement; there may be several courts that may be taking more time to dispose off cases, however, their judgements would be more 'just'. The problem is, such an assessment is very qualitative, and pretty much impossible to make from our dataset, and we are steering clear from that.

## Aggregate Measure

Now that we have had a look at various districts along these different metrics, a question naturally arises - is it possible for us to develop a metric that encompasses perfomance along all these metrics, and gives an idea of an overall good, or an overall bad district? How do we go about developing one? Many districts may end up being good performers along one metric but bad ones along another, and therefore it is incredibly useful to have a metric which gives an idea of which one is a good or which is one is a bad performer in an overall sense, even if it is somewhat hand-waivey.

Turns out that there does exist such a method! We construct the probability density histograms for the case duration time for each district, and then compare the probabilistic distance measures (the fancy-speak term is known as [f-divergence](https://en.wikipedia.org/wiki/F-divergence)) between 2 such districts. 

The histogram of the all the cases across all the districts is calculated and labelled the national histogram. This becomes the reference probability distribution against which other districts are compared. The probabilistic distance between the histogram of the district, and the national histogram is calculated. The districts with higher distance measures are said to be more deviant from the norm.

We will now look at the various distance measures we can use. Keep in mind that, in all of these measures, \\( P(x) \\) is the histogram of the case duration time of a particular district (also called the observed probability distribution), and \\( Q(x) \\) is the corresponding national histogram (also called the reference probability distribution).

## Probabilistic Distances

#### Kullback-Leibler Divergence

The first method for doing so comes from information theory, and is known as Kullback-Leibler (KL) divergence. The divergence between two probability distributions \\( P(x) \\) and \\( Q(x) \\) is given by - 

$$ D_{\text{KL}}(P||Q) = \sum_{x \epsilon X}^{}P(x)\log_2{\frac{P(x)}{Q(x)}} $$

In information theory, the expression for "_entropy_" of a probability distribution is given by -

$$ H(P) = -\sum_{x \epsilon X}^{}P(x)\log_2{P(x)} $$

The entropy gives us a measure of the minimum number of bits required to store the information contained in this distribution. KL divergence can also be written in the following manner - 

$$ D_{\text{KL}}(P||Q) = \sum_{x \epsilon X}^{}P(x)(\log_2{P(x)} - \log_2{Q(x)}) $$

So KL divergence can be thought of as the "_information difference_" that would arise, if the data was represented using \\( Q(x) \\) instead of \\( P(x) \\). For that reason KL divergence is also called the **relative entropy of P with respect to Q**. Even though a lot of people use KL divergence to measure the probabilistic distance between two distributions, it is important to keep in mind that it is not a distance metric, simply because \\( D_{\text{KL}}(P\|\|Q) \neq D_{\text{KL}}(Q\|\|P) \\)

#### Jensen-Shannon Divergence

A slight application of KL divergence gives us the \\( \lambda \\) divergence - 

$$ D_{\lambda}(P||Q) = \lambda D_{\text{KL}}(P||\lambda P + (1-\lambda) Q ) + (1-\lambda) D_{\text{KL}}(Q||\lambda P + (1-\lambda) Q) $$ 

If we choose \\(\lambda = 0.5 \\), we get the Jensen-Shannon Divergence.

$$ D_{\text{JS}}(P||Q) = \frac{1}{2}D_{\text{KL}}(P||M) + \frac{1}{2}D_{\text{KL}}(Q||M) $$ 

where \\( M = \frac{P+Q}{2} \\).

2 important points to be kept in mind are that first, JS divergence is bounded between 0 and 1, and that second, it is symmetric, i.e., \\( D_{\text{JS}}(P\|\|Q) = D_{\text{JS}}(Q\|\|P) \\)

#### Bhattacharyya Distance

This metric was created by Anil Kumar Bhattacharyya at the Indian Statistical Institute in the 1930s. The expression for the Bhattacharyya Coefficient (BC) is given by - 

$$ BC(P||Q) = \sum_{x \epsilon X}^{}\sqrt{P(x)Q(x)} $$

The expression for Bhattacharyya Distance is given from the Bhattacharyya Coefficient as - 

$$ D_B(P||Q) = -\log{BC(P||Q)} $$

The intuition behind this is that if the probability distributions are exactly identical, BC would break down to a simple sum of probabilities across the entire domain of \\( x \\), which we know is 1. That gives a value of 0 for \\( D_B(P\|\|Q) \\). However, if they are not identical, whenever \\( P(x) \neq Q(x) \\), the probability sum gets distorted, leading to a \\( BC(P\|\|Q) \\) value less than 1, which results in a positive \\( D_B(P\|\|Q) \\). The greater the divergence between the P and Q, the more positive the distance will be.

#### Hellinger Distance

This metric is also based on the Bhattacharyya Coefficient, as defined above. The Hellinger Distance is given by - 

$$ D_H(P||Q) = \sqrt{1 - BC(P||Q)} $$

Where, BC is as defined before.

$$ BC(P||Q) = \sum_{x \epsilon X}^{}\sqrt{P(x)Q(x)} $$

The intuition for this is similiar to the intution we apploed for Bhattacharyya Distance. If the distributions are absolutely identical, BC is 1, and thus \\( D_H(P\|\|Q) \\) is 0. As the distributions start diverging more, the value of BC reduces further, resulting in a higher positive value of distance. It's important to keep in mind that, unlike Bhattacharyya Distance, which was unboundedly positive, Hellinger Distance is bounded between 0 and 1.

#### Total Variation Distance

The equation for this metric is given by - 

$$ D_{\text{TV}}(P||Q) = \sup_{x \epsilon X}{|P(x) - Q(x)|} $$

Since we are dealing with finite discrete probabilities, supremum can be replaced by maximum.

$$ D_{\text{TV}}(P||Q) = \max_{x \epsilon X}{|P(x) - Q(x)|} $$ 

All of these distances are a part of a larger class of probabilistic distances called f-divergences. The interested reader can read about this further [here](https://en.wikipedia.org/wiki/F-divergence)

## Appending Sign

Yay! So we have calculated the probabilistic distances for all districts using the above 5 metrics. A sample of the results obtained.

<!-- | Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 | -->

|State				|District	|KL Div	|JS Div |Bhatt Dist|
| ----------------- |:---------:|:-----:|:-----:|:--------:|
|Odisha				|Kendujhar	|0.068	|0.017  |0.013     |
|Karnataka			|Koppal		|0.320	|0.052  |0.040     |
|Gujarat			|Rajkot		|0.052	|0.012  |0.008     |
|Gujarat			|Sabarkantha|0.063	|0.019  |0.015	   |
|Jammu and Kashmir	|Budgam 	|0.037	|0.011  |0.009     |



|State				|District	|Hell Dist|TV Dist |
| ----------------- |:---------:|:-------:|:------:|
|Odisha				|Kendujhar	|0.112    |0.0004  |
|Karnataka			|Koppal		|0.198    |0.0004  |
|Gujarat			|Rajkot		|0.093    |0.0002  |
|Gujarat			|Sabarkantha|0.121    |0.0008  |
|Jammu and Kashmir	|Budgam 	|0.095    |0.0002  |

Now, higher values of distance implies greater deviation from average behaviour. But how do we determine whether that deviation is positive or negative, where positive is defined as faster disposal of cases? High value of distance gives no indication about whether the anomaly is positive or negative.

Before we tackle this, let us check how efficient our metrics are in encapsulating information from each anomaly detection metric we had defined at the start of this blog. Corresponding to each anomaly detection metric, we bifurcate the dataset into 2 parts - one has all the set of districts which perform better than the national average performance corresponding to this metric, and one which has the set of districts which perform worse. Now, we calculate the Pearson Correlation Coefficient of each of our distance metrics with respect to the 2 bifurcated sets separately. This is done precisely because high values of distance can mean both positive and negative behaviour.

Here are some of the scatter plots of the results. Here, both the bifurcated sets, along with their corresponding regressed lines, are plotted together, so we get a "_V plot_". The correlation coefficients above in the title are for the left, and the right halves, respectively. I will put up a link to interactive plots of these soon.

![KL_plot](regression_kl.png)

![JS_plot](regression_js.png)

![Bhatt_plot](regression_bhatt.png)

![Hell_plot](regression_hell.png)

![TV_plot](regression_tv.png) 

|Parameter					 |KL Div	  |JS Div	   |Bhatt Dist  |Hell Dist 	 |
|							 |Left  |Right|Left  |Right|Left  |Right|Left  |Right|
| --------------------------:|:----:|:---:|:----:|:---:|:----:|:---:|:----:|:---:|
|% Cases, Duration > 3 months|-0.849|0.646|-0.868|0.666|-0.845|0.618|-0.849|0.621|
|% Cases, Duration > 6 months|-0.849|0.646|-0.868|0.666|-0.845|0.618|-0.849|0.621|
|% Cases, Duration > 1 year	 |-0.849|0.646|-0.868|0.666|-0.845|0.618|-0.849|0.621|
|% Cases, Duration > 3 years |-0.849|0.646|-0.868|0.666|-0.845|0.618|-0.849|0.621|






