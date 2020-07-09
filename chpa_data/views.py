from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy import create_engine
import pandas as pd

ENGINE = create_engine('mysql://root:root@127.0.0.1:3306/CHPA_1806')  # 创建数据库连接引擎


def index(request):
    sql = "Select * from data"  # 标准sql语句，此处为测试返回数据库data表的数据条目n，之后可以用python处理字符串的方式动态扩展
    df = pd.read_sql_query(sql, ENGINE)  # 将sql语句结果读取至Pandas Dataframe
    return HttpResponse(df.to_html())  # 渲染，这里暂时渲染为最简单的HttpResponse，以后可以扩展
