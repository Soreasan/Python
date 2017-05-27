#!/usr/bin/env python
import pandas as pd
def test_run():
    df = pd.read_csv('data.csv')
    print(df) #Print entire dataframe
if __name__ == "__main__":
    test_run()
