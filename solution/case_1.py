from sum_of_digits import sum_digits
from prep_dataframe import prep_df
from cleanup import cleanup

def case_1(n_customers):
    df = prep_df(n_customers)		#prep the dataframe
    for i in range(n_customers):	#for n customers starting with 0
        j = sum_digits(i)			#find their group id
        df[j] = df[j] + 1			#add one customer to their group
    df = cleanup(df)				#clean up
    return(df)						#and we're done