#!/usr/bin/env python
# Author:Wang Xueming

import json
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'files/population_json.json'

with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        # print(country_name + ": " + str(population))
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop


wm_style = RS('#456789', base_style=LCS)

# 看看每组分别包含多少个国家
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2016, by Country'

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
