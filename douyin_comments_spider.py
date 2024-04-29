# -*- coding: utf-8 -*-
import csv
import time
import random
import requests
from fake_useragent import UserAgent


params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'aweme_id': '7289816712139115811',
    'cursor': '0',
    'count': '20',
    'item_type': '0',
    'insert_ids': '',
    'whale_cut_token': '',
    'cut_version': '1',
    'rcFT': '',
    'pc_client_type': '1',
    'version_code': '170400',
    'version_name': '17.4.0',
    'cookie_enabled': 'true',
    'screen_width': '1628',
    'screen_height': '916',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Edge',
    'browser_version': '120.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '120.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '8',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '2.6',
    'effective_type': '4g',
    'round_trip_time': '50',
    'webid': '7200000880502146617',
    'msToken': 'bx4i0yVHohdNpCxCkxXOiZb4Qa17c3_nsDejp7alpv3E',
    'X-Bogus': 'DFSzswVuux0ANJOFtiAKJ/D4OFXQ'
}


page = 1
comments_count = 0
comments_count = 0
userlink = "http://www.douyin.com/user/"
url = 'http://www.douyin.com/aweme/v1/web/comment/list/'

while True:   
    headers = {
        'authority': 'www.douyin.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'n_mh=OMAzXd-mej2O3xI1fZXqBUDp8c6IV423yZ_tf4ONcQc; LOGIN_STATUS=1; store-region=cn-hb; store-region-src=uid; ttwid=1%7CiOElc6KM8Bk9VXP18nNdvsmDXdQboUv-sxK5sL2J8Hk%7C1714317682%7Cdf3147517c2664801d780c5ccab93adb910cfd8e8b0fc0cf41cdc616733c9564; dy_swidth=1143; dy_sheight=715; csrf_session_id=63888c99ea9016e722edbf12b275ca87; passport_csrf_token=16cdca93e270bfd0142184f6310f0b9a; passport_csrf_token_default=16cdca93e270bfd0142184f6310f0b9a; bd_ticket_guard',
        'referer': 'https://www.douyin.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user_agent.random ,
    }

    response = requests.get(url,params,headers=headers)

    comments = json_data('comments')
    for data in comments:
        cid = data['cid']       
        create_time = data['create_time']
        digg_count = data['digg_count']
        ip_label = data['ip_label']
        text = data['text']
        nickname = data['nickname']
        print(page,cid,create_time,digg_count,ip_label,text,nickname)
        comments_count += 1
        
    print(headers['user-agent'])
    sleep_time = random.uniform(0, 3)
    print("sleep time:", sleep_time)
    print("爬取评论数量:", comments_count)
    print("======================")
    time.sleep(sleep_time)
    page+=1

