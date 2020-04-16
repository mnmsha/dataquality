
def availability_def(hostname):
    import requests
    r = requests.get(hostname)
    if r.status_code != 200:
        return 0
    else:
        return 1

def authority_def(hostname):
    from bs4 import BeautifulSoup
    import requests
    try:
        r=requests.get("https://news.yandex.ru/yandsearch?text="+hostname+"&rpt=nnews2&grhow=clutop")
        soup=BeautifulSoup(r.text)
        number=soup.find('span', 'filters__counters').get_text()
    except AttributeError:
        number=0
    return int(number)


def machinereadability_def(file):
    machine_readable_formats=[".json", ".xml", ".csv", ".xls", ".xlsx"]
    import os
    import pathlib
    from pathlib import Path
    from os.path import abspath
    filename, file_extension = os.path.splitext(file.name)
    if file_extension in machine_readable_formats:
        result=1
    else:
        result=0
    return result

def class_dict_def(file):
    INN_10_dict={}
    INN_12_dict={}
    OGRN_13_dict={}
    OGRN_15_dict={}
    import pandas as pd
    import os
    filename, file_extension = os.path.splitext(file.name)
    if file_extension == ".csv":
        df = pd.read_csv(file, encoding = "utf-8", sep=',', error_bad_lines=False)
        for i in list(df):
            for index, row in df.iterrows():
                r=list(str(row[i]))
                if len(r)==10:
                    try:
                        csum=(2*int(r[0])+4*int(r[1])+10*int(r[2])+3*int(r[3])+5*int(r[4])+9*int(r[5])+4*int(r[6])+6*int(r[7])+8*int(r[8]))%11
                        if csum>9:
                            csum=csum%10
                        if csum==int(r[9]):
                            df = df.rename(columns={i: 'INN_10'})
                    except ValueError:
                        pass
                elif len(r)==12:
                    try:
                        csum=(7*int(r[0])+2*int(r[1])+4*int(r[2])+10*int(r[3])+3*int(r[4])+5*int(r[5])+9*int(r[6])+4*int(r[7])+6*int(r[8])+8*int(r[9]))%11
                        if csum>9:
                            csum==csum%10
                        if csum==int(r[10]):
                            df = df.rename(columns={i: 'INN_12'})
                    except ValueError:
                        pass
                elif len(r)==13:
                    try:
                        csum=(int(r[0]+r[1]+r[2]+r[3]+r[4]+r[5]+r[6]+r[7]+r[8]+r[9]+r[10]+r[11])) % 11 % 10
                        if csum==int(r[12]):
                            df = df.rename(columns={i: 'OGRN_13'})
                    except ValueError:
                        pass
                elif len(r)==15:
                    try:
                        csum=(int(r[0]+r[1]+r[2]+r[3]+r[4]+r[5]+r[6]+r[7]+r[8]+r[9]+r[10]+r[11]+r[12]+r[13])) % 13 % 10
                        if csum==int(r[14]):
                            df = df.rename(columns={i: 'OGRN_15'})
                    except ValueError:
                        pass
        for index, row in df.iterrows():
            if "INN_10" in list(df):
                r=list(str(row["INN_10"]))
                try:
                    csum=(2*int(r[0])+4*int(r[1])+10*int(r[2])+3*int(r[3])+5*int(r[4])+9*int(r[5])+4*int(r[6])+6*int(r[7])+8*int(r[8]))%11
                    if csum>9:
                        csum=csum%10
                    if csum==int(r[9]):
                        INN_10_dict[row["INN_10"]]="ok"
                    else:
                        INN_10_dict[row["INN_10"]]="not ok"
                except ValueError:
                    INN_10_dict[row["INN_10"]]="not ok"
            if "INN_12" in list(df):
                r=list(str(row["INN_12"]))
                try:
                    csum=(7*int(r[0])+2*int(r[1])+4*int(r[2])+10*int(r[3])+3*int(r[4])+5*int(r[5])+9*int(r[6])+4*int(r[7])+6*int(r[8])+8*int(r[9]))%11
                    if csum>9:
                        csum=csum%10
                    if csum==int(r[9]):
                        INN_12_dict[row["INN_12"]]="ok"
                    else:
                        INN_12_dict[row["INN_12"]]="not ok"
                except ValueError:
                    INN_12_dict[row["INN_12"]]="ok"
            if "OGRN_13" in list(df):
                r=list(str(row["OGRN_13"]))
                try:
                    csum=(int(r[0]+r[1]+r[2]+r[3]+r[4]+r[5]+r[6]+r[7]+r[8]+r[9]+r[10]+r[11])) % 11 % 10
                    if csum==int(r[12]):
                        OGRN_13_dict[row["OGRN_13"]]="ok"
                    else:
                        OGRN_13_dict[row["OGRN_13"]]="not ok"
                except ValueError:
                    OGRN_13_dict[row["OGRN_13"]]="not ok"
                except IndexError:
                    OGRN_13_dict[row["OGRN_13"]]="not ok"
            if "OGRN_15" in list(df):
                r=list(str(row["OGRN_15"]))
                try:
                    csum=(int(r[0]+r[1]+r[2]+r[3]+r[4]+r[5]+r[6]+r[7]+r[8]+r[9]+r[10]+r[11]+r[12]+r[13])) % 13 % 10
                    if csum==int(r[14]):
                        OGRN_15_dict[row["OGRN_15"]]="ok"
                    else:
                        OGRN_15_dict[row["OGRN_15"]]="not ok"
                except ValueError:
                    OGRN_15_dict[row["OGRN_15"]]="not ok"
                except IndexError:
                    OGRN_15_dict[row["OGRN_13"]]="not ok"
        all_dict = dict(list(INN_10_dict.items()) + list(INN_12_dict.items()) + list(OGRN_13_dict.items()) + list(OGRN_15_dict.items()))
    else:
        all_dict = 0
    return all_dict

def reliability_def(all_dict):
    if all_dict == 0:
        result=0
    else:
        all_values=list(all_dict.values())
        if (all_values.count("ok")+all_values.count("not ok")) == 0:
            result = 0
        else:
            result=all_values.count("ok")/(all_values.count("ok")+all_values.count("not ok"))
    return result

def relevance_def(file):
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    for i in file.keys():
        try:
            driver = webdriver.Chrome("/Users/Misha/Downloads/chromedriver")
            driver.get("https://www.rusprofile.ru")
            time.sleep(0)
            element = driver.find_element_by_class_name("index-search-input")
            element.send_keys(str(i))
            element.submit()
            time.sleep(3)
            element_1 = driver.find_element_by_xpath('//*[@id="anketa"]/div[1]/div[1]/div[2]')
            if element_1.text == "Действующая организация":
                file[i]="ok"
            else:
                file[i]="not ok"
            driver.quit()
        except NoSuchElementException:
            file[i]="not ok"
            driver.quit()
    return file







def fullness_def(list_class, file):
    list_class_ok=[]
    if 2 in list_class:
        list_class.append("INN")
        list_class.remove(2)
    if 1 in list_class:
        list_class.append("OGRN")
        list_class.remove(1)
    count_nan =[]
    INN_dict={}
    OGRN_dict={}
    import pandas as pd
    import os
    filename, file_extension = os.path.splitext(file.name)
    if file_extension == ".csv":
        df = pd.read_csv(file, encoding = "utf-8", sep=',', error_bad_lines=False)
        for i in list(df):
            for index, row in df.iterrows():
                r=list(str(row[i]))
                if len(r)==10:
                    try:
                        csum=(2*int(r[0])+4*int(r[1])+10*int(r[2])+3*int(r[3])+5*int(r[4])+9*int(r[5])+4*int(r[6])+6*int(r[7])+8*int(r[8]))%11
                        if csum>9:
                            csum=csum%10
                        if csum==int(r[9]):
                            df = df.rename(columns={i: 'INN'})
                    except ValueError:
                        pass
                elif len(r)==12:
                    try:
                        csum=(7*int(r[0])+2*int(r[1])+4*int(r[2])+10*int(r[3])+3*int(r[4])+5*int(r[5])+9*int(r[6])+4*int(r[7])+6*int(r[8])+8*int(r[9]))%11
                        if csum>9:
                            csum==csum%10
                        if csum==int(r[10]):
                            df = df.rename(columns={i: 'INN'})
                    except ValueError:
                        pass
                elif len(r)==13:
                    try:
                        csum=(int(r[0]+r[1]+r[2]+r[3]+r[4]+r[5]+r[6]+r[7]+r[8]+r[9]+r[10]+r[11])) % 11 % 10
                        if csum==int(r[12]):
                            df = df.rename(columns={i: 'OGRN'})
                    except ValueError:
                        pass
                elif len(r)==15:
                    try:
                        csum=(int(r[0]+r[1]+r[2]+r[3]+r[4]+r[5]+r[6]+r[7]+r[8]+r[9]+r[10]+r[11]+r[12]+r[13])) % 13 % 10
                        if csum==int(r[14]):
                            df = df.rename(columns={i: 'OGRN'})
                    except ValueError:
                        pass
        for i in list_class:
            if i in list(df):
                list_class_ok.append(i)
                count_nan.append(1 - (len(df[i]) - df[i].count())/len(df[i]))
        if len(list_class) != 0:
            if len(count_nan) != 0:
                result = (len(list_class_ok)/len(list_class))*(sum(count_nan)/len(count_nan))
            else:
                result = (len(list_class_ok)/len(list_class))
        else:
            result=0
    return result



def popularuty_def(hostname):
    f=dataquality.objects.filter(source=hostname).values("popularuty").values()/len(dataquality.objects.filter(source=hostname).values("popularuty"))
    result = sum(f.values())/len(f)
    return result
