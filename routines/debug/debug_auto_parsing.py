# -*- coding: utf-8 -*-
from routines.auto.top_job_list import top_job_titles
from routines.auto.top_locations_list import top_location_list

new_list = {}
for i in top_job_titles:
    new_list[i] = []
for j in top_location_list.keys():
    for k in top_location_list[j]:
        for i in top_job_titles:
            new_list[i].append(k)

counter = 1
for i in new_list.keys():
    for j in range(len(new_list[i])):
        print("#" + str(counter) +
              " Job Title:" + str(i) +
              " Location:" + str(new_list[i][j]))
        counter += 1
