import json

import jsonpath
import requests


class Lagou_Spider():
    def __init__(self):
        # 初始化url headers
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?'
        self.headers = {
            "accept": "application/json, text/javascript",
            "accept-encoding": "gzip, deflate",
            "accept-language": "ZH-cn,zh",
            "connection": "keep-alive",
            "content-length": "26",
            "content-type": "application/x-www-form-urlencoded; charsET=UTF-8",
            "cookie": "_GA=GA1.2.1174396912.1521688718; user_trace_token=20180322111839-b724427b-2d7f-11e8-93d7-525400f775cE; LGUID=20180322111839-b72448f2-2d7f-11e8-93d7-525400f775ce; index_location_citY=%E4%B8%8A%E6%B5%B7; JSESSIONID=ABAAABAAAGGABCB297984BB6C295158488F052EE799A392; _gID=GA1.2.1370303100.1523888644; hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521688719,1523888651; LGSID=20180416222442-e783d24c-4181-11e8-8816-525400f775cE; PRE_UTM=; PRE_HOST=; PRE_SIte=httpS%3A%2F%2fwww.lagou.coM%2F; PRE_LAnd=httpS%3A%2F%2fwww.lagou.coM%2fjobS%2flist_pythoN%3flaBelwordS%3D%26fRomsearcH%3dtrue%26suginpuT%3D; SEARCH_Id=2e70e982359a47e9b5f1ac775d46a6dA; TG-TRACK-COde=search_codE; LGRID=20180416223210-f29bad8d-4182-11e8-8817-525400f775cE; hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523889131",
            "host": "www.lagou.com",
            "origin": "https://www.lagou.com",
            "referer": "https://www.lagou.com/jobs/list_python?laBelwords=&fRomsearch=true&suginput=",
            "user-agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/65.0.3325.181 safari/537.36",
            "X-anit-forge-code": "0",
            "X-anit-forge-token": "none",
        }

    # 发送请求
    def send_request(self):
        # 有参数 拼接 json数据中都是""
        params = {
            "city": "上海",
            "neeDaddtionaLresult": "false",
        }
        formdata = {
            "first": "true",
            "pn": 1,
            "kd": "python",
        }

        # 发送请求 返回数据
        try:
            response = requests.post(self.url,params=params,data=formdata,headers=self.headers)
            # data = response.content.decode('utf-8')
            data = response.json()
            return data
        except Exception as e:
            print(e)
    # 数据分析
    def analysis(self,data):
        pass
    # 写入数据
    def write_file(self,data):
        print('正在写入...')
        json.dump(data,open('lagou-position.html','w'))
    # 运行
    def run(self):
        # 发送请求
        data = self.send_request()
        #
        # 写入数据
        self.write_file(data)
if __name__ == '__main__':
    foo = Lagou_Spider()
    foo.run()