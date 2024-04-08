# **Cryptocurrency Cluster Analysis with PCA Using Scikit-learn**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, plotly, sklearn.

Here are the requisite Terminal commands for the installation of these peripheral modules:

pip3 install -U holoviews

pip3 install -U hvplot

pip3 install -U geoviews

pip3 install -U geopy

pip3 install -U aspose-words

pip3 install -U dataframe-image

pip3 install -U scikit-learn

pip3 install -U plotly

----

### **Usage:**

----

The IPython notebook, crypto_clustering.ipynb, requires the following Python scripts with it in the same folder:

kmeans_analysis_functions.py

log_constants.py

log_functions.py

log_subroutines.py

pandas_process_functions.py

If the folders, logs and images, are not present, the IPython notebook will create them.  The IPython notebook, crypto_clustering.ipynb, needs the csv file, crypto_market_data.csv, in the folder, resources, to execute. To place the IPython notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. If the program is in Log Mode, it writes information to the log file. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG and HTML files in the folder, images.

----

### **Resource Summary:**

----

#### Source code

crypto_clustering.ipynb, kmeans_analysis_functions.py, log_constants.py, log_functions.py, log_subroutines.py, pandas_process_functions.py

#### Input files

crypto_market_data.csv

#### Output files

n/a

#### SQL script

n/a

#### Software

Jupyter Notebook, Matplotlib, Numpy, Pandas, Python 3.11.4, Plotly, scikit-learn

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./crypto_clustering.ipynb](./crypto_clustering.ipynb)

|&rarr; [./kmeans_analysis_functions.py](./kmeans_analysis_functions.py)

|&rarr; [./log_constants.py](./log_constants.py)

|&rarr; [./log_functions.py](./log_functions.py)

|&rarr; [./log_subroutines.py](./log_subroutines.py)

|&rarr; [./pandas_process_functions.py](./pandas_process_functions.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/crypto_clustering221KMeansMethodsLinePlots.png](./images/crypto_clustering221KMeansMethodsLinePlots.png)
  
  &emsp; |&rarr; [./images/crypto_clustering331KMeansPriceChangeScatterPlots.png](./images/crypto_clustering331KMeansPriceChangeScatterPlots.png)

  &emsp; |&rarr; [./images/crypto_clustering341CryptocurrencyPriceChange3DScatterPlotk4.png](./images/crypto_clustering341CryptocurrencyPriceChange3DScatterPlotk4.png)

  &emsp; |&rarr; [./images/crypto_clustering343CryptocurrencyPriceChange3DScatterPlotk3.png](./images/crypto_clustering343CryptocurrencyPriceChange3DScatterPlotk3.png)

  &emsp; |&rarr; [./images/crypto_clustering344CryptocurrencyPriceChange3DScatterPlotk2.png](./images/crypto_clustering344CryptocurrencyPriceChange3DScatterPlotk2.png)

  &emsp; |&rarr; [./images/crypto_clustering521KMeansMethodswithPCADataLinePlots.png](./images/crypto_clustering521KMeansMethodswithPCADataLinePlots.png)

  &emsp; |&rarr; [./images/crypto_clustering631KMeansScatterPlotsPCA1vsPCA2.png](./images/crypto_clustering631KMeansScatterPlotsPCA1vsPCA2.png)
  
  &emsp; |&rarr; [./images/crypto_clustering632KMeansScatterPlotsPCA1vsPCA3.png](./images/crypto_clustering632KMeansScatterPlotsPCA1vsPCA3.png)
  
  &emsp; |&rarr; [./images/crypto_clustering633KMeansScatterPlotsPCA2vsPCA3.png](./images/crypto_clustering633KMeansScatterPlotsPCA2vsPCA3.png)
  
  &emsp; |&rarr; [./images/crypto_clustering641CryptocurrencyDataUsingPCA3DScatterPlotk2.png](./images/crypto_clustering641CryptocurrencyDataUsingPCA3DScatterPlotk2.png)

  &emsp; |&rarr; [./images/crypto_clustering641CryptocurrencyDataUsingPCA3DScatterPlotk4.png](./images/crypto_clustering641CryptocurrencyDataUsingPCA3DScatterPlotk4.png)

  &emsp; |&rarr; [./images/crypto_clustering642CryptocurrencyDataUsingPCA3DScatterPlotk10.png](./images/crypto_clustering642CryptocurrencyDataUsingPCA3DScatterPlotk10.png)

  &emsp; |&rarr; [./images/crypto_clustering643CryptocurrencyDataUsingPCA3DScatterPlotk3.png](./images/crypto_clustering643CryptocurrencyDataUsingPCA3DScatterPlotk3.png)

  &emsp; |&rarr; [./images/crypto_clustering711KMeansWCSSElbowMethodOriginal.png](./images/crypto_clustering711KMeansWCSSElbowMethodOriginal.png)

  &emsp; |&rarr; [./images/crypto_clustering712KMeansWCSSElbowMethodPCA.png](./images/crypto_clustering712KMeansWCSSElbowMethodPCA.png)
  
  &emsp; |&rarr; [./images/crypto_clustering721KMeansPriceChangeOriginal.png](./images/crypto_clustering721KMeansPriceChangeOriginal.png)

  &emsp; |&rarr; [./images/crypto_clustering722KMeansPriceChangePCA.png](./images/crypto_clustering722KMeansPriceChangePCA.png)
  
  &emsp; |&rarr; [./images/crypto_clustering731CryptocurrencyData3DScatterPlotK4.png](./images/crypto_clustering731CryptocurrencyData3DScatterPlotK4.png)

  &emsp; |&rarr; [./images/crypto_clustering731CryptocurrencyDatawithPCA3DScatterPlotK4.png](./images/crypto_clustering731CryptocurrencyDatawithPCA3DScatterPlotK4.png)

  &emsp; |&rarr; [./images/crypto_clusteringTable121CryptocurrenciesDataFrameTable.png](./images/crypto_clusteringTable121CryptocurrenciesDataFrameTable.png)
  
  &emsp; |&rarr; [./images/crypto_clusteringTable122CryptocurrenciesDataFrameSummaryStatistics.png](./images/crypto_clusteringTable122CryptocurrenciesDataFrameSummaryStatistics.png)
  
  &emsp; |&rarr; [./images/crypto_clusteringTable131NormalizedCryptocurrencyDataFrameTable.png](./images/crypto_clusteringTable131NormalizedCryptocurrencyDataFrameTable.png)

  &emsp; |&rarr; [./images/crypto_clusteringTable132NormalizedCryptocurrencyDataFrameSummaryStatistics.png](./images/crypto_clusteringTable132NormalizedCryptocurrencyDataFrameSummaryStatistics.png)
  
  &emsp; |&rarr; 
[./images/crypto_clusteringTable321NormalizedCryptocurrencywithPredictionsDataFrameTable.png](./images/crypto_clusteringTable321NormalizedCryptocurrencywithPredictionsDataFrameTable.png)

  &emsp; |&rarr; [./images/crypto_clusteringTable421CryptocurrenciesPCADataFrameTable.png](./images/crypto_clusteringTable421CryptocurrenciesPCADataFrameTable.png)
  
  &emsp; |&rarr; [./images/crypto_clusteringTable621CryptocurrencywithPredictionsUsingPCADataTable.png](./images/crypto_clusteringTable621CryptocurrencywithPredictionsUsingPCADataTable.png)
  
  &emsp; |&rarr; [./images/README.md](./images/README.md)

|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240407crypto_clustering_log.txt](./logs/20240407crypto_clustering_log.txt)

  &emsp; |&rarr; [./logs/README.md](./logs/README.md)

|&rarr; [./resources/](./resources/)

  &emsp; |&rarr; [./resources/crypto_market_data.csv](./resources/crypto_market_data.csv)

  &emsp; |&rarr; [./resources/README.md](./resources/README.md)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

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
