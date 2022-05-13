#!/usr/bin/env python3
from datetime import datetime
import time
import requests
import json
import os.path
import matplotlib.pyplot as plt


def get_current_day():  # Problem 1
    date = time.time()
    dt_object = datetime.fromtimestamp(date)
    return dt_object.strftime('%Y-%m-%d')  # %H:%M:%S


data_cache = []  # Problem 2


def query_carbon(date=get_current_day(), use_cache=True):

    headers = {'Accept': 'application/json'}
    url = 'https://api.carbonintensity.org.uk/intensity/date/' + str(date)

    if use_cache:

        if os.path.exists(f"data/carbon_{date}.json"):
            with open(f"data/carbon_{date}.json", 'r') as f:
                data = f.read()
                data = json.loads(data)
            print('data found on os')

        else:
            r = requests.get(url, params={}, headers=headers)
            if r.status_code == 200:
                data = json.loads(r.content.decode('utf-8'))
                print('data loaded from api')
                with open(f'data/carbon_{date}.json', 'w') as f:
                    json.dump(data, f)

            else:
                return 'error: ' + str(r.status_code)

    else:
        r = requests.get(url, params={}, headers=headers)
        if r.status_code == 200:
            data = json.loads(r.content.decode('utf-8'))
            with open(f'data/carbon_{date}.json', 'w') as f:
                json.dump(data, f)
        print('use_cache turned off, pulled data from api')
    return data


def plot_carbon(date=get_current_day()):  # Problem 3 (incomplete)
    data = query_carbon(date, True)
    print(data)
    # intensity = []
    # forecast_carbon = []
    # actual_carbon = []
    # data_time = []

    forecast_carbon = data.get('forecast', 0)
    actual_carbon = data.get('actual', 0)
    data_time = data.get("from", 0)

    # for i in data["data"]:
    #     intensity.append(i["intensity"])
    #
    # for j in intensity:
    #     forecast_carbon.append(j["forecast"])

    # for k in intensity:
    #     actual_carbon.append(k["actual"])

    # for m in data["data"]:
    #     data_time.append(m["from"])

    # data_time_stripped =

    # for n in data_time:
    #     n.strip(str(date))

    print(forecast_carbon, actual_carbon, data_time)
    return forecast_carbon, actual_carbon, data_time


if __name__ == '__main__':
    forecast, actual, time = plot_carbon()
    # = query_carbon(get_current_day())
    # Problem 3 unfinished so plotting not complete
    plt.plot(time, forecast)
    plt.plot(time, actual)
