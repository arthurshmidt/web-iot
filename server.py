import time
import json

global data 
global stpt

# Read in stpt from stpt.json and load them into stpt_json variable.  
def read_stpt(stpt_json):
    
    with open('data/stpt.json','r') as openfile:
        stpt_json = json.load(openfile)
    print("startstop value: "+ str(stpt_json["startstop"]))
    return stpt_json

# Write data to data.json file.
def write_data(data_json):
    # Testing: increment value by 1.
    counter = data_json["value"] 
    data_json["value"] = data_json["value"] + 1
    print("update_data(): " + str(data_json["value"]))

    # Write data_json to file.  
    json_object = json.dumps(data_json,indent=4)
    with open('data/data.json','w') as openfile:
        openfile.write(json_object)

    return data_json

if __name__ == "__main__":

    # Set initial values
    data = {
        "value": 0
    }

    stpt = {
        "startstop": 0
    }

    # Test loop
    while True:
        stpt = read_stpt(stpt)
        data = write_data(data)
        time.sleep(1)
