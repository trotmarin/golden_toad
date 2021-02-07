import csv
import os 
from maindata.models import TestTable

def run():
    file = open('/Users/trotmarin/Downloads/1_month_records.csv', encoding='euc-kr')
    read_file=csv.reader(file)

    TestTable.objects.all().delete()

    count=1

    for record in read_file:
        if count==1:
            pass
        else:
            print(record)
            TestTable.objects.create(apt_name=record[4],sgmt=record[5],cnt_year_month=record[6],cnt_day=record[7],cnt_amt=record[8],level=record[9])
        count=count+1