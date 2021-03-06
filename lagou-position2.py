import json

import jsonpath
import requests
import time


class Lagou_Spider():
    def __init__(self):
        # 初始化url headers
        self.page = 0
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?'
        self.headers = {
            "cookie": "_GA=GA1.2.1174396912.1521688718; user_trace_token=20180322111839-b724427b-2d7f-11e8-93d7-525400f775cE; LGUID=20180322111839-b72448f2-2d7f-11e8-93d7-525400f775ce; index_location_citY=%E4%B8%8A%E6%B5%B7; JSESSIONID=ABAAABAAAGGABCB297984BB6C295158488F052EE799A392; _gID=GA1.2.1370303100.1523888644; hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521688719,1523888651; LGSID=20180416222442-e783d24c-4181-11e8-8816-525400f775cE; PRE_UTM=; PRE_HOST=; PRE_SIte=httpS%3A%2F%2fwww.lagou.coM%2F; PRE_LAnd=httpS%3A%2F%2fwww.lagou.coM%2fjobS%2flist_pythoN%3flaBelwordS%3D%26fRomsearcH%3dtrue%26suginpuT%3D; SEARCH_Id=2e70e982359a47e9b5f1ac775d46a6dA; TG-TRACK-COde=search_codE; LGRID=20180416223210-f29bad8d-4182-11e8-8817-525400f775cE; hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523889131",
            "referer": "https://www.lagou.com/jobs/list_python?laBelwords=&fRomsearch=true&suginput=",
            "user-agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/65.0.3325.181 safari/537.36",
        }
        self.dict_list = []
    # 发送请求
    def send_request(self):
        time.sleep(1)
        # 有参数 拼接 json数据中都是""
        params = {
            "city": "上海",
            "neeDaddtionaLresult": "false",
        }
        formdata = {
            "first": "true",
            "pn": self.page,
            "kd": "python",
        }

        # 发送请求 返回数据
        response = requests.post(self.url,params=params,data=formdata,headers=self.headers)
        # data = response.content.decode('utf-8')
        data = response.json()

        return data
    # 数据分析
    def analysis(self,data):
        # jsonpath返回的数据是一个列表
        json_list = jsonpath.jsonpath(data,("$..result"))[0]
        # print(json_list)
        for data_dic in json_list:
            dict__data = {}
            dict__data['companyFullName'] =data_dic['companyFullName']
            dict__data['companyShortName'] =data_dic['companyShortName']
            dict__data['education'] =data_dic['education']
            dict__data['district'] =data_dic['district']
            dict__data['positionName'] =data_dic['positionName']
            dict__data['salary'] =data_dic['salary']
            self.dict_list.append(dict__data)




    # 写入数据
    def write_file(self,):
        print('正在写入...')
        json.dump(self.dict_list,open('lagou-position.json','w'))
    # 运行
    def run(self):

        # 通过遍历获取所有职位
        for page in range(1,20):
            self.page += 1
            # 发送请求
            data = self.send_request()
            print(self.page)
            # 数据分析
            self.analysis(data)
        # 写入数据
        self.write_file()
if __name__ == '__main__':
    foo = Lagou_Spider()
    foo.run()