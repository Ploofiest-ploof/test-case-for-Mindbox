from sum_of_digits import sum_digits
from prep_dataframe import prep_df
from cleanup import cleanup

def case_2(n_customers, n_first_id):
    df = prep_df(n_customers)								#prep the dataframe
    for i in range(n_first_id, n_customers + n_first_id):	#for n customers, starting with n_first_id)
        j = sum_digits(i) 									#find the group ID
        df[j] = df[j] + 1									#and add one customer to the corresponding group
    df = cleanup(df)										#clean up
    return(df)												#and we're done