# Time-Series-projects
## 1.Time-Series Analysis usnig FB-Prophet

**Goal:**
> Predictions for April, May, June, July, August, September 2021.
## 2. Time Series Forecasting - Autoregression (AR)

**Goal**
> Forecast time series with the Autoregression (AR) Approach. 1) JetRail Commuter, 2) Air Passengers, 3) Function Autoregression with Air Passengers, and 5) Function Autoregression with Wine Sales.

## 3.Time series forecasting using ARIMA models

In this project, you are requested to demonstrate Auto Regressive Integrated Moving Average (ARIMA) model and use it to forecast a time series. Perform the following:

> 1.	Provide brief description of ARIMA model and explain how it is used. Describe its parameters.
> 2.	Select a stochastic time series of that describes a phenomenon. 
> 3. Using COVID-19 infections in Saudi Arabia Dataset. 

## 4. ARIMA with Fourier terms

> The goal of this notebook is to show how to tune ARIMA model with additional regressors. We will add some Fourier terms to capture multiple seasonality and compare the best      model with TBATS model.

> Dataset use  Web Traffic Time Series Forecasting from kaggle

## Finding Best Distribution that Fits Data using Fitter

> Finding the Best Distribution that Fits Your Data using Python’s  `Fitter` Library
> Also finding the Z score and precentile for lognoramal form. 


# Forecasting Best Practices

Time series forecasting is one of the most important topics in data science. Almost every business needs to predict the future in order to make better decisions and allocate resources more effectively.

This repository provides examples and best practice guidelines for building forecasting solutions. The goal of this repository is to build a comprehensive set of tools and examples that leverage recent advances in forecasting algorithms to build solutions and operationalize them. Rather than creating implementations from scratch, we draw from existing state-of-the-art libraries and build additional utilities around processing and featurizing the data, optimizing and evaluating models, and scaling up to the cloud.

The examples and best practices are provided as [Python Jupyter notebooks and R markdown files](examples) and [a library of utility functions](fclib). We hope that these examples and utilities can significantly reduce the “time to market” by simplifying the experience from defining the business problem to the development of solutions by orders of magnitude. In addition, the example notebooks would serve as guidelines and showcase best practices and usage of the tools in a wide variety of languages.

## Cleanup notice (2020-06-23)

> We've carried out a cleanup of large obsolete files to reduce the size of this repo. If you had cloned or forked it previously, please delete and clone/fork it again to avoid any potential merge conflicts.

## Content

The following is a summary of models and methods for developing forecasting solutions covered in this repository. The [examples](examples) are organized according to use cases. Currently, we focus on a retail sales forecasting use case as it is widely used in [assortment planning](https://repository.upenn.edu/cgi/viewcontent.cgi?article=1569&context=edissertations), [inventory optimization](https://en.wikipedia.org/wiki/Inventory_optimization), and [price optimization](https://en.wikipedia.org/wiki/Price_optimization). To enable high-throughput forecasting scenarios, we have included examples for forecasting multiple time series with distributed training techniques such as Ray in Python, parallel package in R, and multi-threading in LightGBM. Note that html links are provided next to R examples for best viewing experience when reading this document on our [`github.io`](https://microsoft.github.io/forecasting/) page.

| Model                                                                                             | Language | Description                                                                                                 |
|---------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------|
| [Auto ARIMA](examples/grocery_sales/python/00_quick_start/autoarima_single_round.ipynb)           | Python   | Auto Regressive Integrated Moving Average (ARIMA) model that is automatically selected                      |
| [Linear Regression](examples/grocery_sales/python/00_quick_start/azure_automl_single_round.ipynb) | Python   | Linear regression model trained on lagged features of the target variable and external features             |
| [LightGBM](examples/grocery_sales/python/00_quick_start/lightgbm_single_round.ipynb)              | Python   | Gradient boosting decision tree implemented with LightGBM package for high accuracy and fast speed          |
| [DilatedCNN](examples/grocery_sales/python/02_model/dilatedcnn_multi_round.ipynb)                 | Python   | Dilated Convolutional Neural Network that captures long-range temporal flow with dilated causal connections |
| [Mean Forecast](examples/grocery_sales/R/02_basic_models.Rmd) [(.html)](examples/grocery_sales/R/02_basic_models.nb.html)                                | R        | Simple forecasting method based on historical mean                                                          |
| [ARIMA](examples/grocery_sales/R/02a_reg_models.Rmd) [(.html)](examples/grocery_sales/R/02a_reg_models.nb.html)                                              | R        | ARIMA model without or with external features                                                               |
| [ETS](examples/grocery_sales/R/02_basic_models.Rmd) [(.html)](examples/grocery_sales/R/02_basic_models.nb.html)                                              | R        | Exponential Smoothing algorithm with additive errors                                                        |
| [Prophet](examples/grocery_sales/R/02b_prophet_models.Rmd) [(.html)](examples/grocery_sales/R/02b_prophet_models.nb.html)                                       | R        | Automated forecasting procedure based on an additive model with non-linear trends                           |

The repository also comes with AzureML-themed notebooks and best practices recipes to accelerate the development of scalable, production-grade forecasting solutions on Azure. In particular, we have the following examples for forecasting with Azure AutoML as well as tuning and deploying a forecasting model on Azure.

| Method                                                                                                    | Language | Description                                                                                                |
|-----------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------|
| [Azure AutoML](examples/grocery_sales/python/00_quick_start/azure_automl_single_round.ipynb)              | Python   | AzureML service that automates model development process and identifies the best machine learning pipeline |
| [HyperDrive](examples/grocery_sales/python/03_model_tune_deploy/azure_hyperdrive_lightgbm.ipynb)          | Python   | AzureML service for tuning hyperparameters of machine learning models in parallel on cloud                 |
| [AzureML Web Service](examples/grocery_sales/python/03_model_tune_deploy/azure_hyperdrive_lightgbm.ipynb) | Python   | AzureML service for deploying a model as a web service on Azure Container Instances                        |

## Getting Started in Python

To quickly get started with the repository on your local machine, use the following commands.

1. Install Anaconda with Python >= 3.6. [Miniconda](https://conda.io/miniconda.html) is a quick way to get started.

2. Clone the repository

    ```
    git clone https://github.com/microsoft/forecasting
    cd forecasting/
    ```

3. Run setup scripts to create conda environment. Please execute one of the following commands from the root of Forecasting repo based on your operating system.

    - Linux

    ```
    ./tools/environment_setup.sh
    ```

    - Windows

    ```
    tools\environment_setup.bat
    ```

    Note that for Windows you need to run the batch script from Anaconda Prompt. The script creates a conda environment `forecasting_env` and installs the forecasting utility library `fclib`.

4. Start the Jupyter notebook server

    ```
    jupyter notebook
    ```

5. Run the [LightGBM single-round](examples/grocery_sales/python/00_quick_start/lightgbm_single_round.ipynb) notebook under the `00_quick_start` folder. Make sure that the selected Jupyter kernel is `forecasting_env`.

If you have any issues with the above setup, or want to find more detailed instructions on how to set up your environment and run examples provided in the repository, on local or a remote machine, please navigate to the [Setup Guide](./docs/SETUP.md).

## Getting Started in R

We assume you already have R installed on your machine. If not, simply follow the [instructions on CRAN](https://cloud.r-project.org/) to download and install R.

The recommended editor is [RStudio](https://rstudio.com), which supports interactive editing and previewing of R notebooks. However, you can use any editor or IDE that supports RMarkdown. In particular, [Visual Studio Code](https://code.visualstudio.com) with the [R extension](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r) can be used to edit and render the notebook files. The rendered `.nb.html` files can be viewed in any modern web browser.

The examples use the [Tidyverts](https://tidyverts.org) family of packages, which is a modern framework for time series analysis that builds on the widely-used [Tidyverse](https://tidyverse.org) family. The Tidyverts framework is still under active development, so it's recommended that you update your packages regularly to get the latest bug fixes and features.

## Target Audience

Our target audience for this repository includes data scientists and machine learning engineers with varying levels of knowledge in forecasting as our content is source-only and targets custom machine learning modelling. The utilities and examples provided are intended to be solution accelerators for real-world forecasting problems.

## Contributing

We hope that the open source community would contribute to the content and bring in the latest SOTA algorithm. This project welcomes contributions and suggestions. Before contributing, please see our [Contributing Guide](CONTRIBUTING.md).

## Reference

The following is a list of related repositories that you may find helpful.

|                                                                                                            |                                                                                                 |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [Deep Learning for Time Series Forecasting](https://github.com/Azure/DeepLearningForTimeSeriesForecasting) | A collection of examples for using deep neural networks for time series forecasting with Keras. |
| [Microsoft AI Github](https://github.com/microsoft/ai)                                                     | Find other Best Practice projects, and Azure AI designed patterns in our central repository.    |

## Build Status

| Build         | Branch  | Status  |
| -  | -  | - |
| **Linux CPU** | master  | [![Build Status](https://dev.azure.com/best-practices/forecasting/_apis/build/status/cpu_unit_tests_linux?branchName=master)](https://dev.azure.com/best-practices/forecasting/_build/latest?definitionId=128&branchName=master)   |
| **Linux CPU** | staging | [![Build Status](https://dev.azure.com/best-practices/forecasting/_apis/build/status/cpu_unit_tests_linux?branchName=staging)](https://dev.azure.com/best-practices/forecasting/_build/latest?definitionId=128&branchName=staging) |


List of state of the art papers, code, and other resources focus on time series forecasting.

## [Table of Contents]()

- [M4 competition](#M4-competition)
- [Kaggle time series competition](#Kaggle-time-series-competition)
- [Papers](#Papers)
- [Conferences](#Conferences)
- [Theory-Resource](#Theory-Resource)
- [Code Resource](#Code-Resource)
- [Datasets](#Datasets)

## M4-competition

[M4](https://github.com/Mcompetitions/M4-methods)

#### papers

- [The M4 Competition: 100,000 time series and 61 forecasting methods](https://www.sciencedirect.com/science/article/pii/S0169207019301128)
- [A hybrid method of exponential smoothing and recurrent neural networks for time series forecasting](https://www.sciencedirect.com/science/article/pii/S0169207019301153)
- [Weighted ensemble of statistical models](https://www.sciencedirect.com/science/article/pii/S0169207019301190#b5)
- [FFORMA: Feature-based forecast model averaging](https://www.sciencedirect.com/science/article/pii/S0169207019300895)

## Kaggle-time-series-competition

- [Walmart Store Sales Forecasting (2014)](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)
- [Walmart Sales in Stormy Weather (2015)](https://www.kaggle.com/c/walmart-recruiting-sales-in-stormy-weather)
- [Rossmann Store Sales (2015)](https://www.kaggle.com/c/rossmann-store-sales)
- [Wikipedia Web Traffic Forecasting (2017)](https://www.kaggle.com/c/web-traffic-time-series-forecasting)
- [Corporación Favorita Grocery Sales Forecasting (2018)](https://www.kaggle.com/c/favorita-grocery-sales-forecasting)
- [Recruit Restaurant Visitor Forecasting (2018)](https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting)
- [COVID19 Global Forecasting (2020)](https://www.kaggle.com/c/covid19-global-forecasting-week-5)
- [Jane Street Future Market Prediction(2021)](https://www.kaggle.com/c/jane-street-market-prediction/)

## Papers

### 2022

- [Transformers in Time Series: A Survey](https://arxiv.org/pdf/2202.07125) `review`
  - Wen, et al.
  - [Code](https://github.com/qingsongedu/time-series-transformers-review)

- [Pyraformer: Low-Complexity Pyramidal Attention for Long-Range Time Series Modeling and Forecasting](https://arxiv.org/pdf/2202.07125) `ICLR 2022 oral`
  - Liu, et al.

### 2021

- [A machine learning approach for forecasting hierarchical time series](https://www.sciencedirect.com/science/article/pii/S0957417421005431)
  - Mancuso, et al.

- [Probabilistic Transformer For Time Series Analysis](https://openreview.net/forum?id=HfpNVDg3ExA) `NeuIPS 2021`
  - Tang, et al.

- [Autoformer: Decomposition transformers with auto-correlation for long-term series forecasting](https://papers.nips.cc/paper/2021/file/bcc0d400288793e8bdcd7c19a8ac0c2b-Paper.pdf) `NeuIPS 2021`
  - Wu, et al.

- [CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation](https://openreview.net/forum?id=VzuIzbRDrum) `NeuIPS 2021`
  - Yusuke, et al.

- [Variational Inference for Continuous-Time Switching Dynamical Systems](https://openreview.net/forum?id=ake1XpIrDKN) `NeuIPS 2021`
  - Lukas, et al.

- [MixSeq: Connecting Macroscopic Time Series Forecasting with Microscopic Time Series Data](https://openreview.net/forum?id=VeZQA9KdjMK) `NeuIPS 2021`
  - Zhu, et al.

- [Coresets for Time Series Clustering](https://openreview.net/forum?id=jar9C-V8GH) `NeuIPS 2021`
  - Zhou, et al.

- [Online false discovery rate control for anomaly detection in time series](https://openreview.net/forum?id=NvN_B_ZEY5c) `NeuIPS 2021`
  - Quentin, et al.

- [Adjusting for Autocorrelated Errors in Neural Networks for Time Series](https://openreview.net/forum?id=tJ_CO8orSI) `NeuIPS 2021`
  - Sun, et al.

- [Deep Explicit Duration Switching Models for Time Series](https://openreview.net/forum?id=jar9C-V8GH) `NeuIPS 2021`
  - Zhou, et al.

- [Deep Learning for Time Series Forecasting: A Survey](https://www.liebertpub.com/doi/pdfplus/10.1089/big.2020.0159) `survey`
  - Torres, et al.

- [Whittle Networks: A Deep Likelihood Model for Time Series](https://www.ml.informatik.tu-darmstadt.de/papers/yu2021icml_wspn.pdf) `ICML 2021`
  - Yu, et al.
  - [Code](https://github.com/ml-research/WhittleNetworks)

- [Z-GCNETs: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting](https://arxiv.org/abs/2105.04100) `ICML 2021`
  - Chen, et al.
  - [Code](https://github.com/Z-GCNETs/Z-GCNETs)

- [Long Horizon Forecasting With Temporal Point Processes](https://arxiv.org/abs/2101.02815) `WSDM 2021`
  - Deshpande, et al.
  - [Code](https://github.com/pratham16cse/DualTPP)

- [Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting](https://arxiv.org/abs/2012.07436) `AAAI 2021 best paper`
  - Zhou, et al.
  - [Code](https://github.com/zhouhaoyi/Informer2020)

- [Coupled Layer-wise Graph Convolution for Transportation Demand Prediction](https://arxiv.org/pdf/2012.08080.pdf) `AAAI 2021`
  - Ye, et al.
  - [Code](https://github.com/Essaim/CGCDemandPrediction)

### 2020

- [Block Hankel Tensor ARIMA for Multiple Short Time Series Forecasting](https://ojs.aaai.org/index.php/AAAI/article/download/6032/5888) `AAAI 2020`
  - Shi, et al.
  - [Code](https://github.com/huawei-noah/BHT-ARIMA)

- [Adversarial Sparse Transformer for Time Series Forecasting](https://proceedings.neurips.cc/paper/2020/file/c6b8c8d762da15fa8dbbdfb6baf9e260-Paper.pdf) `NeurIPS 2020`
  - Wu, et al.
  - Code not yet

- [Benchmarking Deep Learning Interpretability in Time Series Predictions](https://arxiv.org/pdf/2010.13924) `NeurIPS 2020`
  - Ismail, et al.
  - [[Code](https://github.com/ayaabdelsalam91/TS-Interpretability-Benchmark)]

- [Deep reconstruction of strange attractors from time series](https://proceedings.neurips.cc/paper/2020/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html) `NeurIPS 2020`
  - Gilpin, et al.
  - [[Code](https://github.com/williamgilpin/fnn)]

- [Rethinking 1D-CNN for Time Series Classification: A Stronger Baseline]( https://arxiv.org/abs/2002.10061) `classification`
  - Tang, et al.
  - [[Code](https://github.com/Wensi-Tang/OS-CNN/)]

- [Active Model Selection for Positive Unlabeled Time Series Classification](https://www.researchgate.net/profile/Shen_Liang7/publication/341691181_Active_Model_Selection_for_Positive_Unlabeled_Time_Series_Classification/links/5ed4ef09458515294527ad45/Active-Model-Selection-for-Positive-Unlabeled-Time-Series-Classification.pdf)
  - Liang, et al.
  - [[Code](https://github.com/sliang11/Active-Model-Selection-for-PUTSC)]

- [Unsupervised Phase Learning and Extraction from Quasiperiodic Multidimensional Time-series Data](https://authors.elsevier.com/a/1b54P5aecShD%7EW)
  - Prayook, et al.
  - [[Code](https://github.com/koonyook/unsupervised-phase-supplementary)]

- [Connecting the Dots: Multivariate Time Series Forecasting withGraph Neural Networks](https://128.84.21.199/pdf/2005.11650.pdf)
  - Wu, et al.
  - [[Code](https://github.com/nnzhan/MTGNN)]

- [Forecasting with sktime: Designing sktime's New Forecasting API and Applying It to Replicate and Extend the M4 Study](https://arxiv.org/pdf/2005.08067.pdf)
  - Löning, et al.
  - Code not yet

- [RobustTAD: Robust Time Series Anomaly Detection viaDecomposition and Convolutional Neural Networks](https://arxiv.org/pdf/2002.09545v1.pdf)
  - Gao, et al.
  - Code not yet

- [Neural Controlled Differential Equations forIrregular Time Series](https://arxiv.org/pdf/2005.08926.pdf)

  - Patrick Kidger, et al.
  - `University of Oxford`
  - [[Code](https://github.com/patrick-kidger/NeuralCDE)]

- [Time Series Forecasting With Deep Learning: A Survey](https://arxiv.org/pdf/2004.13408.pdf)
  - Lim, et al.
  - Code not yet
  
- [Neural forecasting: Introduction and literature overview](https://arxiv.org/pdf/2004.10240.pdf)
  - Benidis, et al.
  - `Amazon Research`
  - Code not yet.

- [Time Series Data Augmentation for Deep Learning: A Survey](https://arxiv.org/pdf/2002.12478.pdf)
  - Wen, et al.
  - Code not yet

- [Modeling time series when some observations are zero](https://www.researchgate.net/profile/Andrew_Harvey5/publication/335035033_Modeling_time_series_when_some_observations_are_zero/links/5d5ea1d5a6fdcc55e81ff273/Modeling-time-series-when-some-observations-are-zero.pdf)```Journal of Econometrics 2020```
  - Andrew Harveyand Ryoko Ito.
  - Code not yet

- [Meta-learning framework with applications to zero-shot time-series forecasting](https://arxiv.org/pdf/2002.02887.pdf)
  - Oreshkin, et al.
  - Code not yet.

- [Harmonic Recurrent Process for Time Series Forecasting](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/ecai20hr.pdf)
  - Shao-Qun Zhang and Zhi-Hua Zhou.
  - Code not yet.

- [Block Hankel Tensor ARIMA for Multiple Short Time Series Forecasting](https://github.com/huawei-noah/BHT-ARIMA)```AAAI 2020```
  - QIQUAN SHI, et al.
  - Code not yet

- [Learnings from Kaggle's Forecasting Competitions](https://www.researchgate.net/publication/339362837_Learnings_from_Kaggle's_Forecasting_Competitions)

  - Casper Solheim Bojer, et al.
  - Code not yet.
  
- [An Industry Case of Large-Scale Demand Forecasting of Hierarchical Components](https://ieeexplore.ieee.org/abstract/document/8999262)

  - Rodrigo Rivera-Castro, et al.
  - Code not yet.
  
- [Multi-variate Probabilistic Time Series Forecasting via Conditioned Normalizing Flows](https://arxiv.org/pdf/2002.06103.pdf)

  - Kashif Rasul, et al.
  - Code not yet.
  
- [ForecastNet: A Time-Variant Deep Feed-Forward Neural Network Architecture for Multi-Step-Ahead Time-Series Forecasting](https://arxiv.org/pdf/2002.04155.pdf)

  - Joel Janek Dabrowski, et al.
  - Code not yet.
  
- [Anomaly detection for Cybersecurity: time series forecasting and deep learning](https://pdfs.semanticscholar.org/810b/dfa0f63f03473be79556b90dc79a88a1f769.pdf)`Good review about forecasting`

  - Giordano Colò.
  - Code not yet.
  
- [Event-Driven Continuous Time Bayesian Networks](https://krvarshney.github.io/pubs/BhattacharjyaSGMVS_aaai2020.pdf)

  - Debarun Bhattacharjya, et al.
  - `Research AI, IBM`
  - Code not yet.

## Conferences

- [ICLR](https://iclr.cc/)
- [AAAI](https://www.aaai.org/)
- [IJCAI](https://www.ijcai.org/)
- [ISF](https://isf.forecasters.org/)
- [NeurIPS](https://nips.cc/)
- [ICML](https://icml.cc/)
- [M5 Competition](https://mofc.unic.ac.cy/m5-competition/)

## Theory-Resource

- [Time Series Analysis, MIT](https://ocw.mit.edu/courses/economics/14-384-time-series-analysis-fall-2013/)

- [Time Series Forecasting, Udacity](https://www.udacity.com/course/time-series-forecasting--ud980)

- [Practical Time Series Analysis, Cousera](https://www.coursera.org/learn/practical-time-series-analysis)

- [Sequences, Time Series and Prediction](https://www.coursera.org/learn/tensorflow-sequences-time-series-and-prediction)

- [Intro to Time Series Analysis in R, Cousera](https://www.coursera.org/projects/intro-time-series-analysis-in-r)

- [Anomaly Detection in Time Series Data with Keras, Corsera](https://www.coursera.org/projects/anomaly-detection-time-series-keras)

- [Applying Data Analytics in Finance, Coursera](https://www.coursera.org/learn/applying-data-analytics-business-in-finance)

- [Time Series Forecasting using Python](https://courses.analyticsvidhya.com/courses/creating-time-series-forecast-using-python)

- [STAT 510: Applied Time Series Analysis, PSU](https://online.stat.psu.edu/statprogram/stat510)

- [Policy Analysis Using Interrupted Time Series, edx](https://www.edx.org/course/policy-analysis-using-interrupted-time-series)

- [Time Series Forecasting in Python](https://www.manning.com/books/time-series-forecasting-in-python-book)

## Code-Resource

- [FOST from microsoft](https://github.com/microsoft/FOST)

- [pyWATTS: Python Workflow Automation Tool for Time-Series](https://github.com/KIT-IAI/pyWATTS)

- [Seglearn: A Python Package for Learning Sequences and Time Series](https://dmbee.github.io/seglearn/)

- [cesium: Open-Source Platform for Time Series Inference](https://github.com/cesium-ml/cesium)

- [PyTorch Forecasting: A Python Package for time series forecasting with PyTorch](https://github.com/jdb78/pytorch-forecasting)

- [A collection of time series prediction methods: rnn, seq2seq, cnn, wavenet, transformer, unet, n-beats, gan, kalman-filter](https://github.com/LongxingTan/Time-series-prediction)

- [Implementation of Transformer model (originally from Attention is All You Need) applied to Time Series](https://github.com/maxjcohen/transformer)

- [Predicting/hypothesizing the findings of the M4 Competition](https://www.sciencedirect.com/science/article/pii/S0169207019301098)

- [PyFlux](https://github.com/RJT1990/pyflux)

- [Time Series Forecasting Best Practices & Examples](https://github.com/microsoft/forecasting)

- [List of tools & datasets for anomaly detection on time-series data](https://github.com/rob-med/awesome-TS-anomaly-detection)

- [python packages for time series analysis](https://github.com/MaxBenChrist/awesome_time_series_in_python)

- [A scikit-learn compatible Python toolbox for machine learning with time series](https://github.com/alan-turing-institute/sktime)

- [time series visualization tools](https://github.com/facontidavide/PlotJuggler)

- [A statistical library designed to fill the void in Python's time series analysis capabilities](https://github.com/alkaline-ml/pmdarima)

- [RNN based Time-series Anomaly detector model implemented in Pytorch](https://github.com/chickenbestlover/RNN-Time-series-Anomaly-Detection)

- [ARCH models in Python](https://github.com/bashtage/arch)

- [A Python toolkit for rule-based/unsupervised anomaly detection in time series](https://github.com/arundo/adtk)

- [A curated list of awesome time series databases, benchmarks and papers](https://github.com/xephonhq/awesome-time-series-database)

- [Matrix Profile analysis methods in Python for clustering, pattern mining, and anomaly detection](https://github.com/matrix-profile-foundation/matrixprofile)

## Datasets

- [SkyCam: A Dataset of Sky Images and their Irradiance values](https://github.com/vglsd/SkyCam)

- [U.S. Air Pollution Data](https://data.world/data-society/us-air-pollution-data)

- [U.S. Chronic Disease Data](https://data.world/data-society/us-chronic-disease-data)

- [Air quality from UCI](http://archive.ics.uci.edu/ml/datasets/Air+Quality)

- [Seattle freeway traffic speed](https://github.com/zhiyongc/Seattle-Loop-Data)

- [Youth Tobacco Survey Data](https://data.world/data-society/youth-tobacco-survey-data)

- [Singapore Population](https://data.world/hxchua/populationsg)

- [Airlines Delay](https://data.world/data-society/airlines-delay)

- [Airplane Crashes](https://data.world/data-society/airplane-crashes)

- [Electricity dataset from UCI](https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014)

- [Traffic dataset from UCI](https://archive.ics.uci.edu/ml/datasets/PEMS-SF)

- [City of Baltimore Crime Data](https://data.world/data-society/city-of-baltimore-crime-data)

- [Discover The Menu](https://data.world/data-society/discover-the-menu)

- [Global Climate Change Data](https://data.world/data-society/global-climate-change-data)

- [Global Health Nutrition Data](https://data.world/data-society/global-health-nutrition-data)

- [Beijing PM2.5 Data Set](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pollution.csv)

- [Airline Passengers dataset](https://github.com/jbrownlee/Datasets/blob/master/airline-passengers.csv)

- [Government Finance Statistics](https://data.world/data-society/government-finance-statistics)

- [Historical Public Debt Data](https://data.world/data-society/historical-public-debt-data)

- [Kansas City Crime Data](https://data.world/data-society/kansas-city-crime-data)

- [NYC Crime Data](https://data.world/data-society/nyc-crime-data)

- [Kaggle-Web Traffic Time Series Forecasting](https://www.kaggle.com/c/web-traffic-time-series-forecasting)
