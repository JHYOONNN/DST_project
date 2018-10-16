import requests as r
import json
import numpy as np

http_header = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'x-requested-with': 'XMLHttpRequest'
}

session = r.Session()
session.headers.update(http_header)

search_distance_url_base = 'https://m.map.naver.com/spirra/findCarRoute.nhn?route=route3&output=json&result=web3&coord_type=latlng&search=2&car=0&mileage=12.4'

def SEARCH_DISTANCE_URL(start_point, end_point):
    return search_distance_url_base+'&start={}&destination={}'.format(start_point, end_point)

def SEARCH_POINT_URL(q):
    return 'https://m.map.naver.com/apis/search/poi?query={}&page=1'.format(q)

def GET_END_POINT(q):
    res = session.get(SEARCH_POINT_URL(q)).text
    res_dict = json.loads(res)
    x = res_dict['result']['address']['list'][0]['x']
    y = res_dict['result']['address']['list'][0]['y']
    name = res_dict['result']['address']['list'][0]['name']
    return '{},{},{}'.format(x, y, name)

def GET_INFO(array_input):
    print("Getting time information from NAVER MAP....")
    ret_array = np.zeros((len(array_input),len(array_input)))
    for i in range (0, len(array_input)):
        for j in range(i, len(array_input)):
            if(i != j):
                start_point = GET_END_POINT(array_input[i])
                end_point = GET_END_POINT(array_input[j])
                res = session.get(SEARCH_DISTANCE_URL(start_point, end_point)).text
                res_dict = json.loads(res)
                target = res_dict['routes'][0]['summary']
                sec = target['duration']
                ret_array[i][j] = sec/60
    for i in range(0, len(array_input)):
        for j in range(0, i):
            ret_array[i][j] = ret_array[j][i]
    print("Getting time information from NAVER MAP is done")
    return ret_array
