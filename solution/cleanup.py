def cleanup(df):
    df = df.loc[:, (df != 0).any(axis=0)]	#Find columns without zeroes, and keep only those
    return df								#and we're done