#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan

old_dict = {                                                         ###旧数据,类型为字典
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}

new_dict = {                                                         ###新数据,类型为字典
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 }
}

old_set = set(old_dict.keys())                                       ###把字典的k转化为集合类型
new_set = set(new_dict.keys())

update_list = old_set.intersection(new_set)                          ###新旧取交集,并集为需要更新的数据
delete_list = old_set.symmetric_difference(update_list)              ###旧数据与更新数据取差集,得出需要删去的数据
add_list = new_set.symmetric_difference(update_list)                 ###新数据与更新数据取差集,得出需要添加的数据
print("需要更新:",update_list)
print("需要删除:",delete_list)
print("需要添加:",add_list)


a = old_set | new_set                                                ###union()新旧的并集(合并)
b = old_set & new_set                                                ###intersection()新旧的交集
c = new_set - old_set                                                ###difference(),求差集(在new,但不在old中)
d = new_set ^ old_set                                                ###symmetric_difference,对称差集(在new或者old,中,但不会同时出现在二着中
print(a)
print(b)
print(c)
print(d)