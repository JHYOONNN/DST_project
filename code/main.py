'''
main 에서는 각각의 file의 function을 이용해 data를 가공해 받아오고
최종적으로 routes.py로 보내줌
'''
import numpy as np
import datetime as dt

import cal_people_sum as cps
import cal_time
import tps_algo

def cal_best_route():
    node_data = np.genfromtxt('./csv/made_data.csv', encoding="utf8", dtype = None, delimiter = ',', usecols = range(0,2))
    range_data = np.genfromtxt('./csv/made_data.csv', encoding="utf8", dtype = None, delimiter = ',', usecols = range(2,6))

    my_time = dt.time(12, 00, 00)
    print("--------------------------\n안덕면\n--------------------------")
    for i in range(0,13):
        print(i,"      ", node_data[i][0])
    print("--------------------------\n대정읍\n--------------------------")
    for i in range(13,18):
        print(i,"      ", node_data[i][0])
    print("--------------------------\n한경면\n--------------------------")
    for i in range(18,30):
        print(i,"      ", node_data[i][0])
    print("--------------------------\n한림읍\n--------------------------")
    for i in range(30,39):
        print(i,"      ", node_data[i][0])
    print("--------------------------\n애월읍\n--------------------------")
    for i in range(39,50):
        print(i,"      ", node_data[i][0])
    print("choose all node (first should be start): ")
    all_node = list(map(int, input().split()))
    ft = np.zeros((len(all_node), len(all_node)))
    
    using_time = []
    node_info_need = []
    
    range_info_need = np.zeros((len(all_node), 24))

    for i in range(0, len(all_node)):
        node_info_need.append(node_data[all_node[i]][1])
        range_info_need[i] = cps.cal_people_sum_def(range_data[all_node[i]])

    fp = cps.cal_people_all(range_info_need)
    ft = cal_time.GET_INFO(node_info_need)

    routes = []
    print("finding path using data...")
    tps_algo.find_path(all_node, all_node[0], [], 0, 0,my_time, ft, fp, routes)
    choice = tps_algo.best_choice(routes)
    print("finding path using data is done")
    print(choice)
    for i in range(0, len(choice) -1):
        using_time.append(ft[all_node.index(choice[i])][all_node.index(choice[i+1])])
    return (choice, using_time)