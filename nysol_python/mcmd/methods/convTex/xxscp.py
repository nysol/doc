#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nysol.mcmd as nm

with open('dat1.csv','w') as f:
  f.write(
'''items
b a  c
c c
e a   b
''')

with open('dat2.csv','w') as f:
  f.write(
'''items
b.a..c
.c.c
e.a...b.
''')

import nysol.mcmd as nm

nm.mvdelnull(vf="items:new", A=True, i="dat1.csv", o="rsl4.csv").run()
