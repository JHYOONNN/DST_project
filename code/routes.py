'''
Flask를 이용해 local server를 구동하고 index.html로 계산된 값들을 보내주는 부분
지도를 띄우고 경로를 출력해주는 것은 index.html 코드에 들어있음

디버깅이 완료되면 local server를 통해 http://127.0.0.1:5000 에서 출력을 확인할 수 있음
'''

from flask import Flask, render_template
import json
import numpy as np
import main
import geo_coding

(final_path, final_time) = main.cal_best_route()

for i in range(0, len(final_time)):
    final_time[i] = round(final_time[i])
    
final_path = np.asarray(final_path)
final_time = np.asarray(final_time)
print("getting geo code using address...")
geo_addr = geo_coding.cal_node_geo_addr(final_path)
print("getting geo code using address is done")
length = len(geo_addr)

geo = geo_addr.tolist()
geo = json.dumps(geo)
finaltime = final_time.tolist()
finaltime = json.dumps(finaltime)
finalpath = final_path.tolist()
finalpath = json.dumps(finalpath)
app = Flask(__name__)

@app.route('/')

def render_static():
    return render_template('index.html',geo = geo, length = length, finaltime = finaltime, finalpath = finalpath)

if __name__ == '__main__':
    app.run()