#!/bin/python
ages = { 'kevin' : 30, 'bob':29, 'keith' : 45}
print(ages)
ages['kala'] = 60
print(ages)
print(ages.keys())
print(ages.values())
ages['bob'] = 100
print(ages)
print(ages.pop('keith'))
print(ages)
del ages['kala']
print(ages)
colors = { [ ('muthu', 46), ('alli', 30)]}
print(colors)
