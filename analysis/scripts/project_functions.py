import pandas as pd

def load_and_process(directory):
    
    df1 = (pd.read_csv(directory)
          .drop(['Final Weight', 'Education-Num'], axis = 1)
          .dropna()
          )
    return df1