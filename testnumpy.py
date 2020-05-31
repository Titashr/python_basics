import numpy as np
import json

a = np.array([1, 2, 3]) * np.array([4, 5, 6])
b = np.array([1, 2, 3, 4, 5], ndmin=4)
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a)
print(b)
print(c)
print(d)
# print(type(a))
print(a.ndim) 
print(b.ndim) 
print(c.ndim) 
print(d.ndim) 

# # --converts a python object into JSON
# print(json.dumps({'id': '1', 'name': 'Andrew'})) 

# # some JSON to python
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# print(json.loads(x))