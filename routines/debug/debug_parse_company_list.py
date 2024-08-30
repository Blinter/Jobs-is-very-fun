# -*- coding: utf-8 -*-
from routines.auto.top_company_list import company_list
from routines.parsing.company import clean_company_str

new_list = []
for i in company_list:
    new_list.append(clean_company_str(i))

for i in new_list:
    print(i)
