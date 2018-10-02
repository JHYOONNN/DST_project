import numpy as np
import datetime as dt

my_data = np.genfromtxt('jeju_people_data_all.csv', encoding="utf8", dtype = np.float64)
my_time = dt.time(12, 23, 32)

#해당 여행지 전체 그리드의 유동인구 합을 구해주는 함수
def cal_people_sum(final_people, x_range_min, x_range_max, y_range_min, y_range_max):
    people_temp =np.zeros((20,24))
    temp = 0
    add_all = 0
    
    for i in range(1,14927):
        if my_data[i][0] >= y_range_min and my_data[i][0] <= y_range_max and my_data[i][1] >= x_range_min and  my_data[i][1] <= x_range_max:
            for j in range(2,26):
                people_temp[temp][j-2] = my_data[i][j]
            temp += 1
            
    for i in range(0,temp):
        for j in range(0,24):
            final_people[j] += people_temp[i][j]
    
    for i in range(0,24):
        add_all += final_people[i]
    
    for i in range(0,24):
        final_people[i] = final_people[i] * 100 / add_all        
            
fa = np.zeros((100,24))
cal_people_sum(fa[0], 913250, 914000, 1472750, 1473250)

for i in range(0,24):
    print(fa[0][i])
    
print(my_time)

'''
final_array 정보
--------------------------
행       여행지
--------------------------
0       정방폭포
'''