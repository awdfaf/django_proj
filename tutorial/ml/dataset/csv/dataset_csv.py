import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

class Dataset_Csv:
    # 클래스 생성자
    # anscom 데이터 셋 로드
    def __init__(self):
        # 클래스가 생성될 때 엠스콤 데이터셋 로드하기
        # self로 지정된 변수들은 모두 전역변수로 사용가능
        self.df = sns.load_dataset('anscombe')
        
    # 앤스콤 데이터 조회
    def getAnscombeData(self):
        return self.df
    
    
    # html에 넘겨주기 위한 데이터형태로 조회
    def getColumn_List(self):
        columns = self.df.columns

        # 행렬 자동조회
        df_list = [{columns[0] : d,
                    columns[1] : x,
                    columns[2] : y} for d,x,y in zip(self.df["dataset"], self.df["x"], self.df["y"])]
        return columns, df_list
    
    # 앤스콤 시각화 이미지 저장하기
    def initVisualization(self):
        # ans 데이터 원본을 이용해 
        # dataset 컬럼의 데이터 중 I 값만 추출
        data1 = self.df[self.df["dataset"] == "I"]
        # dataset 다른 데이터에 대해서도 필터링 후 그래프 그리기
        data2 = self.df[self.df["dataset"] == "II"]
        data3 = self.df[self.df["dataset"] == "III"]
        data4 = self.df[self.df["dataset"] == "IV"]

        # 그래프 그리기 위한 객체 받아오기
        fig = plt.figure()

        # 4개 각각의 그래프를 그리기 위한 공간만들기
        # subplot
        # 첫번째 값 : 행
        # 두번째 값 : 열
        # 세번째 값 : 행렬 중 어느 위치에 들어갈지 순서 지정
        ax1 = fig.add_subplot(2,2,1)
        ax2 = fig.add_subplot(2,2,2)
        ax3 = fig.add_subplot(2,2,3)
        ax4 = fig.add_subplot(2,2,4)

        # subplot에 제목넣기
        ax1.set_title("data1")
        ax2.set_title("data2")
        ax3.set_title("data3")
        ax4.set_title("data4")



        # 데이터 넣어서 그래프 그리기 : 점으로 표시
        ax1.plot(data1["x"],data1["y"], "o",c="r")
        ax2.plot(data2["x"],data2["y"], "o",c="g")
        ax3.plot(data3["x"],data3["y"], "o",c="b")
        ax4.plot(data4["x"],data4["y"], "o",c="y")

        # 전체 그래프 제목
        fig.suptitle("Anscombe Data")

        # 그래프 간 간격 조절
        # tight_layout()
        fig.tight_layout()

        # 완료된 시각화 그래프 이미지 저장
        # 저장위치 : images
        # 파일명 : anscombe_data.png
        plt.savefig('C:/pknu_web/tutorial/ml/static/ml/images/anscombe_data.png')
