import os
from datetime import datetime


os.path.exists(r"D:\\Python")
os.getcwd()

date_1 = datetime.strptime('2020-05-03','%Y-%m-%d')
date_1
datetime.now()
datetime.now().strftime('%Y%m%d_%H%M%S')
result_dir = os.path.join(os.getcwd(), 'test_save_csv', datetime.now().strftime('%Y%m%d_%H%M%S'))
result_dir
os.mkdir(result_dir)
os.makedirs(result_dir)
os.path.exists(result_dir)
os.listdir()