import json

if __name__ == '__main__':
    data = [{
        'a':1,
        'b':2,
        'c':3,
        'd':True,
        'e':False,
        'f':None
    }]
    json_data = json.dumps(data)
    print(json_data)
    jsonData = '''[{"a": 1, "b": 2, "c": 3, "d": true, "e": false, "f": null}]
    '''
    data1 = json.loads(jsonData)
    print(data1)
