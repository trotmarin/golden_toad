# python3 manage.py runscript load2

import csv
import os 
from maindata.models import Table2

def run():
    file = open('/Users/trotmarin/Downloads/table2.csv')
    read_file=csv.reader(file)

    Table2.objects.all().delete()

    count=1

    for record in read_file:
        if count==1:
            pass
        else:
            if record[0] == "서울특별시":
                print(record)
                Table2.objects.create(apt_code = record[4], apt_name=record[5],apt_addr=record[7],apt_born=record[10], apt_indvs=record[12])
            else:
                pass
        count=count+1