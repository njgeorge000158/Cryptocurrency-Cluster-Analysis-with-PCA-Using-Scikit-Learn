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
   
![CryptoClustering221KMeansMethodsLinePlots](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/14f06385-5c28-492f-914a-b27d03c6755e)

2. K-Means Price Change (%) Scatter Plots (2D) for the Original Data

![CryptoClustering331KMeansPriceChangeScatterPlots](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/59188b9a-ebae-4918-8433-9d5ec9ae84b3)

3. K-Means Price Change (%) Scatter Plots (3D) for the Original Data

![CryptoClustering341CryptocurrencyPriceChange3DScatterPlotk3](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/7f3f7745-0f88-4339-9cc6-082c00555ee6)![CryptoClustering342CryptocurrencyPriceChange3DScatterPlotk4](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/1e0ced2e-8854-4594-9334-b31ee2bb74cd)

![CryptoClustering343CryptocurrencyPriceChange3DScatterPlotk5](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/f920a1f0-e887-487a-9e61-68cecddfd593)![CryptoClustering344CryptocurrencyPriceChange3DScatterPlotk6](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/621c32b8-ffa0-40c1-8790-22b0f12651d9)

4. K-Means Methods Line Plots with PCA Data.

![CryptoClustering521KMeansMethodswithPCADataLinePlots](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/67662b8a-38a7-4a1d-bbd8-25715808eedc)

5. K-Means Price Change (%) Scatter Plots (2D) with PCA Data.

![CryptoClustering631KMeansScatterPlotsPCA1vsPCA2](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/0ee59701-5bba-49b9-8944-d48f8771a454)

![CryptoClustering632KMeansScatterPlotsPCA1vsPCA3](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/f3304661-2e62-4191-915a-91c1e5dfafd3)

![CryptoClustering633KMeansScatterPlotsPCA2vsPCA3](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/5178b52c-16bb-49f3-95d6-fcc84d2724a0)

6. K-Means Price Change (%) Scatter Plots (3D) with PCA Data.

![CryptoClustering641CryptocurrencyDataUsingPCA3DScatterPlotk3](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/61d44e8c-de31-4d82-87fd-3b9e0416442d)![CryptoClustering641CryptocurrencyDataUsingPCA3DScatterPlotk6](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/659ec468-b13f-4d35-abd1-9a2805e24231)

![CryptoClustering642CryptocurrencyDataUsingPCA3DScatterPlotk4](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/fd89825a-4470-4fd4-8e27-5d5c01f20a00)![CryptoClustering643CryptocurrencyDataUsingPCA3DScatterPlotk5](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/66687040-5e46-4c0e-bec7-08ee3e1e1272)

6.  Comparison of K-Means Methods Line Plots
   
![CryptoClustering711KMeansWCSSElbowMethodOriginal](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/55f107b9-beb5-42d1-b0bd-73e4bb842ae0)![CryptoClustering712KMeansWCSSElbowMethodPCA](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/01f6dad5-afe6-4c73-a67c-1bca0d85d881)

7.  Comparison of K-Means Price Change (%) Scatter Plots (2D)
   
![CryptoClustering721KMeansPriceChangeOriginal](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/b1c64366-045b-4065-b2b2-fb53f64e4cf9)![CryptoClustering722KMeansPriceChangePCA](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/e09a1c9b-cc66-446a-a3a1-db361781eb3b)

8. Comparison of Comparison of K-Means Price Change (%) Scatter Plots (3D) for k=4

![CryptoClustering731CryptocurrencyData3DScatterPlotK4](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/afbd0da6-0f04-44f7-87c1-4317e31e85ce)![CryptoClustering731CryptocurrencyDatawithPCA3DScatterPlotK4](https://github.com/njgeorge000158/CryptoClustering/assets/137228821/87aeafc6-be12-4f1e-a556-632a264162ce)

## Conclusion

I found that, with the scaled data and PCA data, that four clusters was the optimal configuration, and, after examining the cluster analysis results visually, the cluster distribution for PCA data has better performance and tighter grouping of data points within each cluster.  Using fewer features with the PCA data has had a positive impact with better-defined and separable clusters compared to using the original data. This reduction has helped to highlight patterns and reduce the impact of noise, leading to more meaningful clustering results.

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
