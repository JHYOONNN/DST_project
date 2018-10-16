import numpy as np

my_data = np.genfromtxt('./csv/temp.csv', encoding="utf8", dtype = np.float64) # 유동인구 정보

#해당 여행지 전체 그리드의 유동인구 합을 구해주는 함수
def cal_people_sum_def(range_info):
    people_hap = np.zeros((24))
    for i in range(1,14927):
        if my_data[i][0] >= range_info[2] and my_data[i][0] <= range_info[3] and my_data[i][1] >= range_info[0] and  my_data[i][1] <= range_info[1]:
            for j in range(2,26):
                people_hap[j-2] += my_data[i][j]
    return people_hap

def cal_people_all(nodes_range_info):
    hap = 0
    for i in range(0, len(nodes_range_info)):
        for j in range(0,24):
            hap += nodes_range_info[i][j]
        for j in range(0,24):
            nodes_range_info[i][j] = nodes_range_info[i][j] / hap * 100
        hap = 0
    return nodes_range_info