from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

from ml.dataset.csv import dataset_csv as dc
# Create your views here.

def sample(request):
    return HttpResponse("hihi")

# 앤스콤 데이터 조회(샘플)
def getAnscomData(request):
    df = dc.Dataset_Csv()
    df_ans = df.getAnscombeData()
    return HttpResponse(df_ans.to_html())

# html에 넘겨줄 데이터형태로 조회
def getAns_List(request):
    df = dc.Dataset_Csv()
    # 컬럼명, 데이터리스트 조회
    columns, df_list = df.getColumn_List()
    
    # 앤스콤 시각화 이미지 저장
    df.initVisualization()
    
    return render(request,
                  "ml/anscom_list.html",
                  {"columns" : columns,
                   "df_list" : df_list})
