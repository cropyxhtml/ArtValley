import os,datetime,re
working_day = datetime.datetime.now().strftime('%y%m%d_%a')
if not os.path.isdir(working_day):
    os.mkdir(working_day)
    open(working_day+'/readme.txt','w',encoding='utf-8')

a = os.listdir();print(a)
년월일 = re.compile('\d{8}',re.VERBOSE)
print(년월일.search(a));input('wait')
