#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import hashlib
import time
import base64
import urllib.parse as urlparse
from urllib.parse import urlencode

class LianJiaUtil:
    app_id = '20161001_android' # 重要
    app_secret = '7df91ff794c67caee14c3dacd5549b35' #重要
    scheme = 'https' # api scheme
    host = 'app.api.lianjia.com' #host

    cookies = {
    }

    headers = {        
    }

    def get_token(self, params):
        '''
            生成链家api请求token
        '''
        data = list(params.items())
        data.sort()

        token = self.app_secret

        for entry in data:
            token += '{}={}'.format(*entry)

        token = hashlib.sha1(token.encode()).hexdigest()
        token = '{}:{}'.format(self.app_id, token)
        token = base64.b64encode(token.encode()).decode()

        return token

    def build_request(self, path, payload, headers=None, cookies=None):
        '''
            组装完整的url
            生成参数签名
            @param path 资源路径
            @param payload 参数
            @param headers 请求头（可选）
            @param cookies cookie信息（可选）
            ret: {
                'headers' : {...}, 
                'url' : '...',
                'cookies' : {...},
                'payload' ： {...}
            }
        '''

        headers = dict((headers or {}), **self.headers)
        cookies = dict((cookies or {}), **self.cookies)
        payload = dict((payload or {}), **(payload or {}))

        payload['request_ts'] = int(time.time())
        headers['Authorization'] = self.get_token(payload)

        url_parts = (
            self.scheme, #scheme
            self.host, #netloc
            path, #path
            '', #params
            urlencode(payload), #query
            '' #fragment
        )

        return {
            'url': urlparse.urlunparse(url_parts),
            'headers': headers,
            'cookies': cookies,
            'payload': payload
        }
        

if __name__ == '__main__':
    path = '/house/chengjiao/search'
    payload = {
        'city_id': '440300',
        'community_id':'2411052382585',
        'limit_count': 20,
        'limit_offset': 0
    }
    headers = {
        "User-Agent": "HomeLink 8.2.0;iPhone9,1;iOS 11.0.3;"
    }
    cookies = {
        "lianjia_uuid": "71151113-EC04-4033-90C0-C6CBA891272D",
        "lianjia_ssid": "230AAEEE-B109-4751-90A2-573435B2FD8F"
    }

    utils = LianJiaUtil()

    rqs = utils.build_request(path, payload, headers, cookies)
    import pprint
    pprint.pprint(rqs)


