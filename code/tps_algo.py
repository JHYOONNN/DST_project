'''
시간에 대한 유동인구와 이동시간 data를 이용해 최적의 경로를 찾아주는 tsp알고리즘 부분
'''

import datetime as dt

# 필요시간은 00 - 01 과 같은 1시간 단위이므로 이를 찾아주는 함수
def time_array(clock):
    for i in range(0,23):
        if(clock >= dt.time(0+i,0,0) and clock < dt.time(1+i, 0, 0)):
            
            return 0+i
        
# 경로별 점수 합산(TSP 완전탐색)    
def find_path(all_node, node, path, td, pd, clock, ta, pa, routes):
    path.append(node)
    if len(path) > 1:
        delta = dt.timedelta(minutes = ta[all_node.index(path[-2])][all_node.index(node)] + 60)
        clock = ((dt.datetime.combine(dt.date(1,1,1),clock) + delta).time())
        td += ta[all_node.index(path[-2])][all_node.index(node)]
        pd += pa[all_node.index(node)][time_array(clock)]
    if(len(all_node) == len(path)):
        routes.append([td, pd, path])
        return
    
    for city in all_node:
        if(city not in path):
            find_path(all_node, city, list(path), td, pd, clock, ta, pa, routes)
    
def best_choice(arr):
    all_time = 0
    all_people = 0
    best_node = []
    best_point = 1000
    car_point = 0
    people_point = 0
    for i in arr:
        all_time += i[0]
        all_people += i[1]
    for i in arr:
        if(best_point > (i[1] / all_people) + (i[0] / all_time)):
            best_point = (i[1] / all_people) + (i[0] / all_time)
            car_point = i[0]
            people_point = i[1]
            best_node = i[2]
    print("최종 이동 시간 : ", car_point)
    print("최종 유동인구 점수 : ",people_point)
    return best_node
    