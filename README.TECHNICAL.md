# **Cryptocurrency K-Means Cluster Analysis with PCA**

----

### **Installation:**

----

This project only requires running the Google Colab Notebook, crypto_clustering_colab.ipynb.

----

### **Usage:**

----

The Google Colab Notebook, crypto_clustering_colab.ipynb, requires the following Python scripts with it in the same folder:

kmeans_analysisx.py

logx.py

pandasx.py

timex.py

If the folders, logs and images, are not present, the Google Colab Notebook will create them.  The Google Colab Notebook, crypto_clustering_colab.ipynb, needs the csv file, crypto_market_data.csv, in the folder, resources, to execute. To place the Google Colab Notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Log Mode, the notebook writes information to the log file in the folder, logs. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG and HTML files in the folder, images.

----

### **Resource Summary:**

----

#### Source code

crypto_clustering.ipynb, kmeans_analysisx.py, logx.py, pandasx.py, timex.py

#### Input files

crypto_market_data.csv

#### Output files

n/a

#### SQL script

n/a

#### Software

Matplotlib, Numpy, Pandas, Python 3.11.4, Plotly, scikit-learn

![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./crypto_clustering_colab.ipynb](./crypto_clustering_colab_colab.ipynb)

|&rarr; [./kmeans_analysisx.py](./kmeans_analysisx.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/crypto_clustering_colab221KMeansMethodsLinePlots.png](./images/crypto_clustering_colab221KMeansMethodsLinePlots.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colab331KMeansPriceChangeScatterPlots.png](./images/crypto_clustering_colab331KMeansPriceChangeScatterPlots.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab341CryptocurrencyPriceChange3DScatterPlotk4.png](./images/crypto_clustering_colab341CryptocurrencyPriceChange3DScatterPlotk4.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab343CryptocurrencyPriceChange3DScatterPlotk3.png](./images/crypto_clustering_colab343CryptocurrencyPriceChange3DScatterPlotk3.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab344CryptocurrencyPriceChange3DScatterPlotk2.png](./images/crypto_clustering_colab344CryptocurrencyPriceChange3DScatterPlotk2.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab521KMeansMethodswithPCADataLinePlots.png](./images/crypto_clustering_colab521KMeansMethodswithPCADataLinePlots.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab631KMeansScatterPlotsPCA1vsPCA2.png](./images/crypto_clustering_colab631KMeansScatterPlotsPCA1vsPCA2.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colab632KMeansScatterPlotsPCA1vsPCA3.png](./images/crypto_clustering_colab632KMeansScatterPlotsPCA1vsPCA3.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colab633KMeansScatterPlotsPCA2vsPCA3.png](./images/crypto_clustering_colab633KMeansScatterPlotsPCA2vsPCA3.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colab641CryptocurrencyDataUsingPCA3DScatterPlotk2.png](./images/crypto_clustering_colab641CryptocurrencyDataUsingPCA3DScatterPlotk2.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab641CryptocurrencyDataUsingPCA3DScatterPlotk4.png](./images/crypto_clustering_colab641CryptocurrencyDataUsingPCA3DScatterPlotk4.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab642CryptocurrencyDataUsingPCA3DScatterPlotk10.png](./images/crypto_clustering_colab642CryptocurrencyDataUsingPCA3DScatterPlotk10.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab643CryptocurrencyDataUsingPCA3DScatterPlotk3.png](./images/crypto_clustering_colab643CryptocurrencyDataUsingPCA3DScatterPlotk3.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab711KMeansWCSSElbowMethodOriginal.png](./images/crypto_clustering_colab711KMeansWCSSElbowMethodOriginal.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab712KMeansWCSSElbowMethodPCA.png](./images/crypto_clustering_colab712KMeansWCSSElbowMethodPCA.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colab721KMeansPriceChangeOriginal.png](./images/crypto_clustering_colab721KMeansPriceChangeOriginal.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab722KMeansPriceChangePCA.png](./images/crypto_clustering_colab722KMeansPriceChangePCA.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colab731CryptocurrencyData3DScatterPlotK4.png](./images/crypto_clustering_colab731CryptocurrencyData3DScatterPlotK4.png)

  &emsp; |&rarr; [./images/crypto_clustering_colab731CryptocurrencyDatawithPCA3DScatterPlotK4.png](./images/crypto_clustering_colab731CryptocurrencyDatawithPCA3DScatterPlotK4.png)

  &emsp; |&rarr; [./images/crypto_clustering_colabTable121CryptocurrenciesDataFrameTable.png](./images/crypto_clustering_colabTable121CryptocurrenciesDataFrameTable.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colabTable122CryptocurrenciesDataFrameSummaryStatistics.png](./images/crypto_clustering_colabTable122CryptocurrenciesDataFrameSummaryStatistics.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colabTable131NormalizedCryptocurrencyDataFrameTable.png](./images/crypto_clustering_colabTable131NormalizedCryptocurrencyDataFrameTable.png)

  &emsp; |&rarr; [./images/crypto_clustering_colabTable132NormalizedCryptocurrencyDataFrameSummaryStatistics.png](./images/crypto_clustering_colabTable132NormalizedCryptocurrencyDataFrameSummaryStatistics.png)
  
  &emsp; |&rarr; 
[./images/crypto_clustering_colabTable321NormalizedCryptocurrencywithPredictionsDataFrameTable.png](./images/crypto_clustering_colabTable321NormalizedCryptocurrencywithPredictionsDataFrameTable.png)

  &emsp; |&rarr; [./images/crypto_clustering_colabTable421CryptocurrenciesPCADataFrameTable.png](./images/crypto_clustering_colabTable421CryptocurrenciesPCADataFrameTable.png)
  
  &emsp; |&rarr; [./images/crypto_clustering_colabTable621CryptocurrencywithPredictionsUsingPCADataTable.png](./images/crypto_clustering_colabTable621CryptocurrencywithPredictionsUsingPCADataTable.png)
  
  &emsp; |&rarr; [./images/README.md](./images/README.md)

|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240429crypto_clustering_colab_log.txt](./logs/20240429crypto_clustering_colab_log.txt)

  &emsp; |&rarr; [./logs/README.md](./logs/README.md)

|&rarr; [./resources/](./resources/)

  &emsp; |&rarr; [./resources/crypto_market_data.csv](./resources/crypto_market_data.csv)

  &emsp; |&rarr; [./resources/README.md](./resources/README.md)

----

### **References:**

----

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

[Plotly Documentation](https://plotly.com/python/getting-started/)

[scikit-learn Documentation](https://scikit-learn.org/stable/)

----

### **Authors and Acknowledgment:**

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
