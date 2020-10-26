import pandas as pd


class TestData:
    def __init__(self, datfr):
        df.columns = map(str.upper, df.columns)
        dx = df['SUB_ENTITY'].unique()

        for i in dx:
            dy = df[df['SUB_ENTITY'].str.contains(i)]
            dy.to_csv(i + '.csv', index=False) 
            print("Writing " + format(len(dy))+ " amount of data to " + i + '.csv')


df = pd.read_csv("example-file.csv")
TestData(df)