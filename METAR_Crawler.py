import time
import urllib
from urllib import request
import os

try:
    os.mkdir('J:\\METAR\\')
except Exception as e:
    pass#Nothing
os.chdir('J:\\METAR\\')


#your data storage address

def downloading(month,day,filename):
    #download url and save to file
    url='https://zh.weatherspark.com/h/d/149123/2019/'+str(month)+'/'+str(day)+'/2019%E5%B9%B47%E6%9C%881%E6%97%A5%E6%98%9F%E6%9C%9F%E4%B8%80-%E4%B8%AD%E5%9B%BD%E3%80%81%E6%88%90%E9%83%BD%E5%8F%8C%E6%B5%81%E5%9B%BD%E9%99%85%E6%9C%BA%E5%9C%BA-%E7%9A%84%E5%8E%86%E5%8F%B2%E5%A4%A9%E6%B0%94#Sections-ObservedWeather'
    print("URL=",url)
    print("Downloading...")
    data=urllib.request.urlopen(url)
    dataF=data.read()
    data.close()
    with open(filename,'wb') as f:
            print("FileName=",filename)
            print("Writing...")
            f.write(dataF)
    return url

def get_filename(month,day):
    filename='2019_'+str(month)+'_'+str(day)+'.html'
    return filename

if __name__=="__main__":
    for m in range(1,13):
        if m in (1,3,5,7,8,10,12):
            for d in range(1,32):
                filename=get_filename(m,d)
                downloading(m,d,filename)
                time.sleep(10)
        elif m in (4,6,9,11):
            for d in range(1,31):
                filename=get_filename(m,d)
                downloading(m,d,filename)
                time.sleep(10)
        else:
            for d in range(1,29):
                #2019 is NOT the leap year
                filename=get_filename(m,d)
                downloading(m,d,filename)
                time.sleep(10)
