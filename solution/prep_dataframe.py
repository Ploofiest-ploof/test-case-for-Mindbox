import pandas as pd
import numpy as np
from math import ceil, log

def prep_df(n_customers):				#create the dataframe
    l = ceil(log(n_customers, 10)) * 10	#find out how long it has to be
    a = np.zeros((1,l))					#create a numpy array of zeroes
    df = pd.DataFrame(a)				#turn it into a dataframe
    return df							#and we're done
    