import numpy as np
import json

print(np.array([1, 2, 3]) * np.array([4, 5, 6]))

# --converts a python object into JSON
print(json.dumps({'id': '1', 'name': 'Andrew'})) 

# some JSON to python
x =  '{ "name":"John", "age":30, "city":"New York"}'
print(json.loads(x))