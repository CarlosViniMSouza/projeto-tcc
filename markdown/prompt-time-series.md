Ideias, concepts, algorithms, etc:

**Concepts**:
1. **Time Series**: A time series is a sequence of data points collected, recorded, or measured at successive, evenly-spaced time intervals⁵.
2. **Components of Time Series**: There are four main components of a time series: Trend, Seasonality, Cyclical variations, and Random or irregular variations⁵.
3. **Stationarity**: Time series data is said to be stationary if it does not exhibit trends or seasonality. That is, the mean, variance, and covariance should be the same for any segment of the series, and they should not be functions of time⁵.
4. **Univariate and Multivariate Time Series**: Univariate time series involves a single time-dependent variable. Multivariate time series involves multiple time-dependent variables¹.

**Methods & Algorithms**:
1. **Autoregression (AR)**: This method uses the dependent relationship between an observation and some number of lagged observations².
2. **Moving Average (MA)**: This method uses the dependency between an observation and a residual error from a moving average model applied to lagged observations².
3. **Autoregressive Moving Average (ARMA)**: This method combines both Autoregression (AR) and Moving Average (MA) models².
4. **Autoregressive Integrated Moving Average (ARIMA)**: This method combines both Autoregression (AR) and Moving Average (MA) models along with a differencing pre-processing step of the sequence to make the sequence stationary²¹.
5. **Seasonal Autoregressive Integrated Moving-Average (SARIMA)**: This method uses the seasonal difference of the series to remove seasonality and then fits an ARIMA model².
6. **Vector Autoregression (VAR)**: This method is used when two or more time series influence each other².
7. **Simple Exponential Smoothing (SES)**: This method is suitable for univariate time series without trend and seasonal components².
8. **Holt Winter’s Exponential Smoothing (HWES)**: This method is suitable for univariate time series with trend and/or seasonal components².
9. **Long Short-Term Memory (LSTM)**: This is a type of recurrent neural network that can learn and remember over long sequences and can achieve state-of-the-art results on challenging prediction problems[^10^].

**Python Libraries**:
1. **Statsmodels**: Provides the capability to fit statistical models such as ARIMA².
2. **TensorFlow**: Offers modules for defining and training machine learning models, and it provides a set of layers and feature columns to build models in a modular way[^10^].

**Articles & Tutorials**:
1. [11 Classical Time Series Forecasting Methods in Python (Cheat Sheet)](^2^)
2. [10 Incredibly Useful Time Series Forecasting Algorithms](^1^)
3. [Time series forecasting | TensorFlow Core](^10^)
4. [A Guide to Time Series Forecasting with ARIMA in Python 3](^12^)
5. [How to Make Predictions for Time Series Forecasting with Python](^9^)

Remember, the choice of model might depend on factors like the characteristics of your data and the requirements of your problem. It's often a good idea to try multiple approaches and see what works best for your specific use case. Good luck with your time series forecasting! If you have more questions or need further clarification, feel free to ask.

Source: Conversation with Copilot, 13/06/2024

1. Time Series Analysis and Forecasting - GeeksforGeeks. https://www.geeksforgeeks.org/time-series-analysis-and-forecasting/.
2. 10 Incredibly Useful Time Series Forecasting Algorithms. https://www.advancinganalytics.co.uk/blog/2021/06/22/10-incredibly-useful-time-series-forecasting-algorithms.
3. 11 Classical Time Series Forecasting Methods in Python (Cheat Sheet). https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/.
4. Time series forecasting | TensorFlow Core. https://www.tensorflow.org/tutorials/structured_data/time_series.
5. 11 Classical Time Series Forecasting Methods in Python (Cheat Sheet). https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/.
6. 10 Incredibly Useful Time Series Forecasting Algorithms. https://www.advancinganalytics.co.uk/blog/2021/06/22/10-incredibly-useful-time-series-forecasting-algorithms.
7. Time series forecasting | TensorFlow Core. https://www.tensorflow.org/tutorials/structured_data/time_series.
8. A Guide to Time Series Forecasting with ARIMA in Python 3. https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3.
9. How to Make Predictions for Time Series Forecasting with Python. https://machinelearningmastery.com/make-predictions-time-series-forecasting-python/.
10. Machine Learning Algorithms for Time Series Analysis and Forecasting. https://arxiv.org/abs/2211.14387.
11. Deep Learning for Time Series Forecasting - Machine Learning Mastery. https://machinelearningmastery.com/deep-learning-for-time-series-forecasting/.
12. Time Series Forecasting: Core Concepts and Definitions. https://link.springer.com/chapter/10.1007/978-3-031-27852-5_5.
13. Time Series Forecasting: Definition & Examples | Tableau. https://www.tableau.com/learn/articles/time-series-forecasting.
14. The Complete Guide to Time Series Forecasting Models. https://medium.com/@wainaina.pierre/the-complete-guide-to-time-series-forecasting-models-ef9c8cd40037.
15. Time Series Forecasting in Python: A Quick Practical Guide. https://365datascience.com/tutorials/time-series-analysis-tutorials/time-series-forecasting-python/.
16. Time Series Forecasting | Papers With Code. https://paperswithcode.com/task/time-series-forecasting.
17. Forecasting the Future: A Comprehensive Review of Time Series .... https://journal.esrgroups.org/jes/article/view/1478.
18. Time series Forecasting tutorial | DataCamp. https://www.datacamp.com/tutorial/tutorial-time-series-forecasting.
19. The Complete Guide to Time Series Models | Built In. https://builtin.com/data-science/time-series-model.
20. undefined. https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip.
