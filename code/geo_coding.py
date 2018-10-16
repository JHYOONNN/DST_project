import googlemaps
import numpy as np

addr_data = np.genfromtxt('./csv/made_data.csv', encoding="utf8", dtype = None, delimiter = ',', usecols = range(1,2))

gmaps_key = 'AIzaSyAtlj9g55jQTeaDIC6Zzki97I5mbVJmCAE'
gmaps = googlemaps.Client(key = gmaps_key)


def cal_node_geo_addr(node_nums):
    geo_data = np.zeros((len(node_nums), 2))
    for i in range(0, len(node_nums)):
        tmp = gmaps.geocode(addr_data[node_nums[i]], language = 'ko')
        geo_data[i][0] = tmp[0]['geometry']['location']['lat']
        geo_data[i][1] = tmp[0]['geometry']['location']['lng']
    return geo_data

