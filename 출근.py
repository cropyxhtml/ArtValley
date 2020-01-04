import os,datetime
working_day = datetime.datetime.now().strftime('%y%m%d_%a')
if not os.path.isdir(working_day):
    os.mkdir(working_day)
    open(working_day+'/readme.txt','w',encoding='utf-8')
