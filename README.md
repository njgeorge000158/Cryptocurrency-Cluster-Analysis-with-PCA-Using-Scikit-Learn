![crypto1](https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/d7a3c903-907c-410a-9c5b-89c28a0e6fec)

----

# Cryptocurrency Cluster Analysis with PCA Using Scikit-learn

----

## Overview

This Cryptocurrency Clustering project predicts if 24-hour or 7-day price changes affect 42 crytpocurrencies using unsupervised machine learning techniques, specifically, K-means and Principal Component Analysis (PCA). This endeavor showcases proficiency in data manipulation, normalization, dimensionality reduction, and clustering algorithms.

## Steps

To meet the objectives of this project, I scale all of the cryptocurrency data with scikit-learn's StandardScalar function. Next, I determine the ideal K-Means value and cluster the cryptocurrency data using four methods: WCSS Elbow, Calinski-Harabasz, Silhouette, and Davies-Bouldin.  To optimize the process, I use PCA and calculate new optimal values of K before clustering the cryptocurrencies again.

## Results

The project includes the following visualizations:

1. K-Means Methods Line Plots for the Original Data
   
<img width="979" alt="crypto2" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/9f1f582f-9c0e-4ee0-8442-a683e3a71e3f">

2. K-Means Price Change (%) Scatter Plots (2D) for the Original Data

<img width="948" alt="crypto3" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/2bf20568-1d60-427d-b3fc-198704f68324">

3. K-Means Price Change (%) Scatter Plots (3D) for the Original Data

<img width="939" alt="crypto4" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/922e02da-1275-40ce-ab52-afa09677d180">

<img width="928" alt="crypto5" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/019804c5-0f2a-4f7b-861b-f15a6c35ba5d">

<img width="919" alt="crypto6" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/e55ba3a6-4251-460f-9c43-435472082e40">

4. K-Means Methods Line Plots with PCA Data.

<img width="987" alt="crypto7" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/dbe54819-dfa2-46ac-8224-994197c51f2b">

5. K-Means Price Change (%) Scatter Plots (2D) with PCA Data.

<img width="988" alt="crypto8" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/2b1a8d83-ae1a-48f6-b171-45778697c4ff">

<img width="988" alt="crypto9" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/278df51d-5511-4480-8a19-c73907ce11dc">

<img width="967" alt="crypto10" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/943a4770-6a1b-41d1-80cb-c49efe94f21b">

6. K-Means Price Change (%) Scatter Plots (3D) with PCA Data.

<img width="935" alt="crypto11" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/cac4b894-28fd-438a-8896-8ff5bf2cfcb4">

<img width="951" alt="crypto12" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/a0207cd5-b581-4f00-852d-e28a5c0de660">

<img width="969" alt="crypto13" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/5af3b439-be80-48a0-900b-feadc7e240e0">

<img width="959" alt="crypto14" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/c0da1e44-8a0f-44c0-9c8e-54d7d34ef1c2">

7.  Comparison of K-Means Methods Line Plots

<img width="520" alt="crypto15" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/e7d3af85-0fa8-4bce-938e-0c726fa75604">

<img width="497" alt="crypto16" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/2b0e3c3d-f80f-4ce4-8798-15cbfe602132">

9.  Comparison of K-Means Price Change (%) Scatter Plots (2D)

<img width="487" alt="crypto17" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/0bb0a6d0-8a55-4347-8566-bdfe25f85d12">

<img width="502" alt="crypto18" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/b03b404f-09f7-4841-8673-7b12854afc7d">

10. Comparison of Comparison of K-Means Price Change (%) Scatter Plots (3D) for k=4

<img width="957" alt="crypto19" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/ec68f842-c838-40da-b8dc-9478360f539f">

<img width="973" alt="crypto20" src="https://github.com/njgeorge000158/Cryptocurrency-Cluster-Analysis-with-PCA-Using-Scikit-Learn/assets/137228821/4be55a34-b9e9-4b0d-ba09-7ce527c30455">

## Conclusion

I found that, with the scaled data and PCA data, that four clusters was the optimal configuration, and, after examining the cluster analysis results visually, the cluster distribution for PCA data has better performance and tighter grouping of data points within each cluster.  Using fewer features with the PCA data has had a positive impact with better-defined and separable clusters compared to using the original data. This reduction has helped to highlight patterns and reduce the impact of noise, leading to more meaningful clustering results.

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
