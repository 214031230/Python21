#!/usr/bin/env python3
disk_info = {
    '#1': {'factory': 'x1', 'model': 'x2', 'size': 600},
    '#2': {'factory': 'x1', 'model': 'x2', 'size': 500},
    '#3': {'factory': 'x1', 'model': 'x2', 'size': 600},
    '#4': {'factory': 'x1', 'model': 'x2', 'size': 900},
}

disk_queryset = [
    {'slot': '#1', 'factory': 'x1', 'model': 'x2', "size": 600},
    {'slot': '#2', 'factory': 'x1', 'model': 'x2', "size": 100},
    {'slot': '#6', 'factory': 'x1', 'model': 'x2', "size": 300},
    ]

s1 = set(disk_info.keys())
s2 = set([i.get('slot') for i in disk_queryset])
print(s1 - s2)
print(s2 - s1)
print(s2 & s1)