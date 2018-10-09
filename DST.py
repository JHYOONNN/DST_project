import numpy as np
import datetime as dt

my_data1 = np.genfromtxt('temp.csv', encoding="utf8", dtype = np.float64) # 유동인구 정보
my_data2 = np.genfromtxt('jeju_time.csv', encoding="utf8", dtype = np.int64, delimiter = ',', filling_values = '0') # 이동시간 정보
my_time = dt.time(12, 00, 00)
fa = np.zeros((100,24)) #필요 유동인구 정보
ft = np.zeros((100,100)) #필요 이동시간 정보



#해당 여행지 전체 그리드의 유동인구 합을 구해주는 함수
def cal_people_sum(final_people, x_range_min, x_range_max, y_range_min, y_range_max):
    people_temp =np.zeros((20,24))
    temp = 0
    add_all = 0
    
    for i in range(1,14927):
        if my_data1[i][0] >= y_range_min and my_data1[i][0] <= y_range_max and my_data1[i][1] >= x_range_min and  my_data1[i][1] <= x_range_max:
            for j in range(2,26):
                people_temp[temp][j-2] = my_data1[i][j]
            temp += 1
            
    for i in range(0,temp):
        for j in range(0,24):
            final_people[j] += people_temp[i][j]
    
    for i in range(0,24):
        add_all += final_people[i]
    
    for i in range(0,24):
        final_people[i] = final_people[i] * 100 / add_all
        
        
        
        
#여행지 그리드 통합 유동인구 계산
cal_people_sum(fa[0], 894250, 895000, 1477750, 1478500)
cal_people_sum(fa[1], 886750, 887750, 1479500, 1480250)
cal_people_sum(fa[2], 891750, 892250, 1474000, 1474500)
cal_people_sum(fa[3], 889250, 889750, 1471750, 1472250)
cal_people_sum(fa[4], 890000, 891000, 1478000, 1478500)
cal_people_sum(fa[5], 890000, 890500, 1474000, 1474750)
cal_people_sum(fa[6], 887500, 888000, 1479750, 1480250)
cal_people_sum(fa[7], 891000, 891500, 1475250, 1475750)
cal_people_sum(fa[8], 892500, 893250, 1477250, 1477750)
cal_people_sum(fa[9], 892750, 893250, 1478000, 1478500)
cal_people_sum(fa[10], 894000, 894500, 1477500, 1478000)
cal_people_sum(fa[11], 888250, 889000, 1471000, 1471750)
cal_people_sum(fa[12], 888500, 888750, 1471250, 1471500)
cal_people_sum(fa[13], 886750, 887750, 1467750, 1468750)
cal_people_sum(fa[14], 886750, 887250, 1477250, 1477750)
cal_people_sum(fa[15], 883250, 883750, 1470000, 1470500)
cal_people_sum(fa[16], 885500, 886000, 1470250, 1470750)
cal_people_sum(fa[17], 884000, 884500, 1469500, 1469750)




#이동시간 정리
ftTemp = np.zeros((100,100))
ftTemp = my_data2
for i in range (0,18):
    for j in range (0,18):
        ft[i][j] = ftTemp[i+1][j+1]




# 필요시간은 00 - 01 과 같은 1시간 단위이므로 이를 찾아주는 함수
def time_array(clock):
    for i in range(0,23):
        if(clock >= dt.time(0+i,0,0) and clock < dt.time(1+i, 0, 0)):
            
            return 0+i




# 경로별 점수 합산(TSP 완전탐색)    
routes = []

def find_path(all_node, node, path, td, pd, clock):
    path.append(node)
    if len(path) > 1:
        delta = dt.timedelta(minutes = ft[path[-2]][node] + 60)
        clock = ((dt.datetime.combine(dt.date(1,1,1),clock) + delta).time())
        print(clock)
        td += (ft[path[-2]][node])
        pd += fa[node][time_array(clock)]
    if(len(all_node) == len(path)):
        global routes
        routes.append([td, pd, path])
        return
    
    for city in all_node:
        if(city not in path):
            find_path(all_node, city, list(path), td, pd, clock)
                
                
                
                

def best_choice(arr):
    all_time = 0
    all_people = 0
    best_node = []
    best_point = 1000
    for i in arr:
        all_time += i[0]
        all_people += i[1]
    for i in arr:
        if(best_point > (i[0] / all_time) + (i[1] / all_people)):
            best_point = (i[0] / all_time) + (i[1] / all_people)
            best_node = i[2]
        print((i[0] / all_time) + (i[1] / all_people), i[2])
    return best_node



#main
print("all node : ")

all_node = list(map(int, input().split()))
now_node = all_node[0]

find_path(all_node, now_node, [], 0, 0,my_time)
for i in routes:
    print(i)
choice = best_choice(routes)
print(choice)



'''
final_array 정보
--------------------------
행       여행지
--------------------------
안덕면
--------------------------
0       카멜리아힐
1       오설록 티뮤지엄
2       안덕 계곡
3       용머리 해안변
4       소인국테마파크
5       포레스트 판타지아
6       항공 우주 박물관
7       화순곶자왈생태탐방숲길
8       세계자동차제주박물관
9       헬로키티 아일랜드
10      귤밭 76번지
11      사계해변
12      마라도 잠수함
---------------------------
대정읍
---------------------------
13      송악산
14      노리매 공원
15      모슬포항
16      알뜨르 비행장
17      운진항, 케이제주씨워킹
'''