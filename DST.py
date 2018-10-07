import numpy as np
import datetime as dt

my_data1 = np.genfromtxt('temp.csv', encoding="utf8", dtype = np.float64) # 유동인구 정보
my_data2 = np.genfromtxt('jeju_time.csv', encoding="utf8", dtype = np.int64, delimiter = ',', filling_values = '0') # 이동시간 정보
my_time = dt.time(12, 23, 00)
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
def time_array():
    for i in range(0,23):
        if(my_time >= dt.time(0+i,0,0) and my_time < dt.time(1+i, 0, 0)):
            
            return 0+i




#입력받은 여행지들중 (유동인구 + 이동시간 이용) 다음 이동지를 결정해주는 함수
def cal_choice(mv_people_array, start):
    point_max = 1000
    point = 1
    point_temp = 0
    time_hap = 0 
    people_hap = 0
    
    for i in mv_people_array:
        people_hap += fa[i][time_array()]
        time_hap += ft[start][i]
    
    print("유동인구 합 : ", people_hap, "시간 합 : ", time_hap)    
    for i in mv_people_array:
        if(ft[start][i] < 25):
            point_temp = ft[start][i] / time_hap + fa[i][time_array()] / people_hap
            print(start,"에서 ", i , "번째 노드로 이동 시 point : ", point_temp)
            print(i, " 위치의 유동인구 : ", fa[i][time_array()], "이동 시간 : ", ft[start][i])
        else:
            point_temp = (ft[start][i] / time_hap + fa[i][time_array()] / people_hap) * point_max
            
        if(point > point_temp):
            
            point = point_temp
            choose_loc = i
            time_temp = ft[start][i] + 60
            
            
    delta = dt.timedelta(minutes = time_temp)
    global my_time
    my_time = ((dt.datetime.combine(dt.date(1,1,1),my_time) + delta).time())
    mv_people_array.remove(choose_loc)
    print(choose_loc, "노드로 이동 결정 \n 이동 후 시간 : ", my_time)
    
    if(len(mv_people_array) <= 1):
        delta = dt.timedelta(minutes = ft[choose_loc][mv_people_array[0]] + 60)
        my_time = ((dt.datetime.combine(dt.date(1,1,1),my_time) + delta).time())
    return choose_loc




#main
print("all node : ")

all_node = list(map(int, input().split()))
now_node = all_node[0]
all_node.remove(now_node)
final_node = []
final_node.append(now_node)

while(len(all_node) > 1):
    print("\n남은 노드  : ", all_node)
    now_node = cal_choice(all_node, now_node)
    
    final_node.append(now_node)

final_node.append(all_node[0])
print("\n\n최종 경로 : ", final_node, "최종 도착 시간 : ", my_time)





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