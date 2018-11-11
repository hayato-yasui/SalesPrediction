import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
from fbprophet import Prophet

# from Common.DB.SQLServer_Client import SQLServerClient
# from Common.DB.sql import *
# from Common.util import Util
# from Common.Setting.BicEC_PriceGapAnalysisSetting import *
# from Common.Logic.Preprocess import *
# from Common.Setting.Common.PreprocessSetting import *
# from Common.Logic.ChartClient import *


class TimeSeriesAnalysis:
    def __init__(self):
        # self.sql_cli = SQLServerClient()
        # self.util = Util()
        # self.bpg_s = BicECPriceGapAnalysisSetting()
        # self.mmt = MergeMasterTable()
        # self.mmt_s = MergeMasterTableSetting()
        # self.preproc=Preprocess
        # self.chart_cli = ChartClient()
        pass


    def execute(self):
        # read csv
        df = pd.read_csv('./Data/example_wp_log_peyton_manning.csv')

        # df['ds'] = pd.to_datetime(df['ds'])
        # df = df.set_index('ds')
        # df.plot()
        model = Prophet()
        model.fit(df)
        future_df = model.make_future_dataframe(365)
        print(future_df.tail())

        # model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
        # model.fit(df_input)
        #
        # future = model.make_future_dataframe(periods=90)
        # forecast = model.predict(future)
        # model.plot(forecast)
        # plt.ylim(2000, 7000)
        # plt.show()

    def _preprocess(self):
        pass


if __name__ == '__main__':
    tsa = TimeSeriesAnalysis()
    tsa.execute()
    print("END")
