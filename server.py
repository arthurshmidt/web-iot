import time
import json

global data 

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
    while True:
        
        data = update_data(data)
        time.sleep(1)
