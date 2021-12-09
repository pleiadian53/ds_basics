import pandas as pd
import numpy as np
# import seaborn as sns

def fraction_rows_missing(df, verbose=False, n=None):
    '''
    Return percent of rows with any missing
    data in the dataframe. 
    
    Input:
        df (dataframe): a pandas dataframe with potentially missing data
    Output:
        frac_missing (float): fraction of rows with missing data
    '''
    rows_null = df.isnull().any(axis=1)
    n_null = sum(rows_null)
    
    if verbose: # show rows with null values
        if n_null > 0: 
            print(f"(fraction_rows_missing) Rows with nulls (n={n_null}):\n{df[rows_null].head(n=n).to_string(index=False)}\n")
    
    return sum(rows_null)/df.shape[0]


def sort_items_by_count(df, condition=None, topn=None, 
                        col='Name', col_freq='Count', ascending=False): 
    # define the target (sub-)population
    df_subset = df[condition] if condition is not None else df 

    df_count = df_subset.groupby(col)[col_freq].sum()
    df_count.sort_values(ascending=ascending, inplace=True)
    
    if topn is None: 
        return df_count.reset_index()
    return df_count[:topn].reset_index()

def get_count(df, cond=None): 
    if cond is None: 
        return df['Count'].sum()
    return df[cond]['Count'].sum()

# (Min-max) normalize a given column to [0, 1]
def normalize(df, col='Total'): 
    return (df[col]-df[col].min())/(df[col].max()-df[col].min())


def test(): 
    import pandas as pd
    baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv', sep=',')

    
   
if __name__ == "__main__": 
    test()