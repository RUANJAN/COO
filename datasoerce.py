import requests
import csv
from io import StringIO
# 涓涓增加
import pandas as pd
import matplotlib.pyplot as plt


class CarbonFootPrint():

    @classmethod
    def download_aqi(cls) -> list:
        response = requests.get(
            'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')

        if response.ok:
            file = StringIO(response.text, newline="")
            csvReader = csv.reader(file)
            next(csvReader)

            #for item in csvReader:
                #print(item[0], item[1], item[3], item[7], item[19],
                    #item[37], item[43], item[47], item[70])
                # item[0]=country,item[1]=year,item[3]=population,item[7]=co2,item[19]=co2_per_gdp,item[37]=flaring_co2,item[43],item[47],item[70]
        else:
            raise Exception("下載失敗")

# --涓涓--------按鈕連接到曲線圖----------------


def draw_oil_co2():
    # 從CSV檔案讀取DataFrame物件
    df = pd.read_csv('oil_co2.csv')
    # 從DataFrame中提取gas_co2、co2、oil_co2和coal_co2列
    gas_co2 = df['gas_co2']
    co2 = df['co2']
    oil_co2 = df['oil_co2']
    coal_co2 = df['coal_co2']
    coal_co2 = df['coal_co2']
    # 繪製折線圖
    plt.plot(gas_co2, label='gas_co2')
    plt.plot(co2, label='co2')
    plt.plot(oil_co2, label='oil_co2')
    plt.plot(coal_co2, label='coal_co2')

    # 添加標籤和圖例
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.legend()

    # 顯示圖表
    plt.show()
    # 顯示圖表
    plt.show()


def main():
    draw_oil_co2()


if __name__ == '__main__':
    main()
