---
title: "Projects"
--- 

## Tracking Social Development From Satellite Data 
## Aaditeshwar Seth, IIT Delhi
### Master's Thesis

· Working on developing models for estimating social development indicators (employment, literacy, etc) from satellite images and nightlight data with Census 2011 data serving as ground truth
· Trained different deep learning models via transfer learning (developing on Oshri et al (KDD 2018)) to predict labels (extracted from Census 2011) given an input of a satellite image
· Clustered spatial variation of village labels from district hotspots to assign different labels to districts
· Implemented 2-Step Floating Catchment Analysis (2SFCA) to obtain accessibility metric for every
village in dataset of 2 Lakh villages

[\[repo-1\]](https://github.com/sansiddhjain/MTP-spatial-clustering) [\[repo-2\]](https://github.com/sansiddhjain/MTP-accessibility)

## Neonate Weight Estimation From Images 
## Wadhwani AI, Mumbai

<p>
<!-- <img style="float: left; width: 50%;" src="https://sansiddhjain.github.io/graph4.svg"> -->
<img src="images/wadhwai-ai-logo.jpg" style="width: 10%;" >
<!-- <img style="float: left; width: 50%;;" src="https://sansiddhjain.github.io/graph5.svg"> -->
</p>

· Developed a computer vision pipeline for estimating volume of an object given a set of images
· Designed for determining whether newborn baby is low birth-weight or not using a mobile phone
· Used Mask R-CNN trained on MS COCO dataset to segment out object from background in image
· Applied Structure-from-Motion (SfM) on segmented images to generate sparse 3D point cloud of object
· Applied Multi-view Stereo (MVS) depth map fusion on above resultant to generate dense point cloud
· Implemented ”Touch-Expand” graph-cut algorithm to generate closed surface for volume calculation
· Also advised student team working on estimating soyabean yield from satellite images in Maharashtra


# Data-driven Legal Reforms  
## Advisors - Prof. Mausam & Prof. Nomesh Bolia, IIT Delhi 
### Undergraduate Thesis

· Scraped large dataset (> 15TB) of court cases summaries from Indian district courts. 420+/594 dis- tricts (∼ 71%) scraped. Analysed districts across several metrics to identify good and bad anomalies
· Used KL divergence to come up with aggregate measure encompassing performance across all metrics
· Implemented lexical cosine distance clustering to obtain a standardised list of casetypes across courts
· Trained several random forest, gradient boosted trees, and MLP models to predict case duration time
· Trained mixture density networks to output probability distribution over case duration time instead
· Modeled case (sequence of hearings) as a Markov Reward Process with reward being case duration
· Website designed to showcase project work. Presented to senior SC judge Justice Madan Lokur, and NITI Aayog

[\[demo\]](https://sansiddhjain.github.io/btp_website/home)
           
# Wi-Fi Based Location Tracking 
### Jan 2018 - May 2018 
## Advisor - Prof. Mausam, IIT Delhi 
### In collaboration with i2e1

· Developed algorithm to estimate indoor location of multiple devices using solely Wi-Fi RSSI values
· Necessary for algorithm to be scalable, energy efficient, for deployment in several indoor environments
· Initial approaches included triangulation heuristics, and data agnostic signal propagation models
· Experimented with fingerprinting models; supervised nature inhibited scalability
· Trained unsupervised multinomial Hidden Markov Model (HMM) and unsupervised Gaussian HMM
· Developed 2 Kalman Filter models - one before RSSI to distance conversion, one after

[\[repo\]](https://github.com/sansiddhjain/internal-localisation)