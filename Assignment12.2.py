'''2.â€‹ Problem Statement

In this assignment students have to make ARIMA model over shampoo sales data and
check the MSE between predicted and actual value.
Student can download data in .csv format from the following link:
https://datamarket.com/data/set/22r0/sales-of-shampoo-over-a-three-year-period#!ds
=22r0&display=line
Hint:

Following is the command import packages and data
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
def parser(x):
return datetime.strptime('190'+x, '%Y-%m')
series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0],'''

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error


#Date parser
def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')



try:
    #Get the dataset
    series = read_csv(r'sales-of-shampoo-over-a-three-ye.csv', 
                      header=0, parse_dates=[0], index_col=0, 
                      squeeze=True, date_parser=parser)
    X = series.values
    
    #Separates train and test data
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    
    
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        #Model creation and training
    	model = ARIMA(history, order=(5,1,0))
    	model_fit = model.fit(disp=0)
        
        #Model forecasting
    	output = model_fit.forecast()
    	yhat = output[0]
    	predictions.append(yhat)
    	obs = test[t]
    	history.append(obs)
    	print('predicted=%f, expected=%f' % (yhat, obs))
    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)
    # plot
    pyplot.plot(test,label='Actual')
    pyplot.plot(predictions, color='red',label='Predicted')
    pyplot.legend()
    pyplot.show()
except Exception as e:
    print("Error Occured")
