import time
import json

global data 
global stpt

def read_stpt(stpt_json):
    
    with open('data/stpt.json','r') as openfile:
        stpt_json = json.load(openfile)
    print("startstop value: "+ str(stpt_json["startstop"]))
    return stpt_json

def update_data(data_json):
    counter = data_json["value"] 
    data_json["value"] = data_json["value"] + 1
    print("update_data(): " + str(data_json["value"]))

    json_object = json.dumps(data_json,indent=4)
    with open('data/data.json','w') as openfile:
        openfile.write(json_object)

    return data_json

if __name__ == "__main__":

    # counter
    data = {
        "value": 0
    }

    stpt = {
        "startstop": 0
    }

    while True:
        stpt = read_stpt(stpt)
        data = update_data(data)
        time.sleep(1)
