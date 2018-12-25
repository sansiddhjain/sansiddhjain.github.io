---
title: "Projects"
--- 

This is a brief overview of some of my research projects. For a more technical description, please refer to my CV [here](https://sansiddhjain.github.io/cv-sansiddh.pdf), or refer the individual repositories.

<p>
<font size="+3"> Tracking Social Development From Satellite Data </font>
<br>
Master's Thesis
<br>
<i> Advisor - Aaditeshwar Seth, IIT Delhi </i>
</p>

<img src="../images/iitd-logo.jpeg" style="float: left; width: 15%; margin: 12px" >

Can satellite data, specifically images and nightlight data, be used to track social development indicators, such as household infrastructure, healthcare, and literacy? That is the question we are trying to answer with this project. The possibilities with even a reasonably-accurate model are endless - coming to conclusions about development much more robustly by not relying on extremely extensive, once-in-a-decade Censuses.
My work has focused more on the spatial variation of social development indicators - what is the variation in social development indicators as we move further away from district centers? Do underdeveloped and developed districts exhibit a significant difference in spatial variation? Is the spatial variation across various social development indicators the same?

[\[repo-1\]](https://github.com/sansiddhjain/MTP-spatial-clustering) [\[repo-2\]](https://github.com/sansiddhjain/MTP-accessibility)

<p>
<font size="+3"> Neonate Weight Estimation From Images </font>
<br>
<i> Wadhwani AI, Mumbai </i>
</p>

<p>
<!-- <img style="float: left; width: 50%;" src="https://sansiddhjain.github.io/graph4.svg"> -->
<img src="../images/wadhwani-ai-logo.jpg" style="float: left; width: 15%; margin: 12px" >
<!-- wadhwani-ai-logo.jpg -->
<!-- <img style="float: left; width: 50%;;" src="https://sansiddhjain.github.io/graph5.svg"> -->
</p>

My work here focused on developing a computer vision pipeline for estimating volume of an object given a set of images. This was for determining whether a newborn baby is low birth-weight or not using images captured on a mobile phone. India has a high incidence of neonate and child mortality due to low-birth weight - 350,000 newborns die in India before they turn 28 days old, and that accounts for roughly 50% of all neonate deaths in India ([Source](http://archive.indiaspend.com/cover-story/low-birth-weight-preterm-delivery-cause-most-newborn-deaths-in-india-45376)). A lot of these deaths are avoidable - more than 66% of neonates in India are not weighed at birth (because the proper infrastructure doesn't exist). Since India has one of the highest incidences of low-birth-weight in general (28% of babies born in India are low-birth-weight), solving this can have an impact at an enormous scale ([Data Source](https://data.unicef.org/topic/nutrition/low-birthweight/)). I worked on developing a computer vision pipeline with largely classical vision techniques. Mask-RCNN was used for image segmentation, and SfM and MVS techniques were used for 3D reconstruction to obtain the volume of object from its images.

<p>
<font size="+3"> Data-driven Legal Reforms </font>
<br>
Undergraduate Thesis
<br>
<i> Advisors - Prof. Mausam & Prof. Nomesh Bolia, IIT Delhi </i>
</p>

<img src="../images/iitd-logo.jpeg" style="float: left; width: 15%; margin: 12px" >

The objective of this project was to amass a very large dataset of court cases from Indian district courts. We scrape (still ongoing!) a dataset of more than 10 million cases at Indian district courts from [this](https://services.ecourts.gov.in/ecourtindia_v6/) website. The first part of the project focused on analysing the data to make inferences regarding the performance of various districts - which are the good/bad performing districts, good/bad performing states, are certain districts outstandingly good/egregiously bad with respect to certain casetypes, etc. For this we defined various evaluation metrics (such as mean case duration time, percentage tail bounds) for statistically analysing districts for identifying anomalies. KL Divergence was also used to create an aggregate metric.

The second part of the project focused on developing various predictive models - given information about a case, can we predict its case duration time? Various models such as Random Forest, Boosted Trees, Feedforward NNs, Mixture Density Networks etc were used. We also designed a website to demonstrate our work, which was showcased to senior SC judge Justice Madan Lokur, and NITI Aayog (link is below).

[\[demo\]](https://sansiddhjain.github.io/btp_website/home)
           

<p>
<font size="+3"> Wi-Fi Based Location Tracking </font>
<br>
<i>Advisor - Prof. Mausam, IIT Delhi </i>
</p>

<img src="../images/i2e1-logo.png" style="float: left; width: 15%; margin: 12px" >

The objective of this project was to develop algorithms which are able to triangulate the location of a user given solely the WiFi RSSI values. Wi-Fi RSSI is an indication of signal strength, which is inversely proportional to distance. The initial approaches were based on RSSI-to-distance conversion and triangulation, however, noise in RSSI led to highly erroneous predictions. Next, "Fingerprinting" (maintaining a database of RSSI and distance tuples) was tried out, however, problems of scalability rendered this technique not useful. Next, various sequence models, such as Hidden Markov Models (HMM) and Kalman Filters were extensively tried out for path prediction, and they were the models that showed most promise.

[\[repo\]](https://github.com/sansiddhjain/internal-localisation)