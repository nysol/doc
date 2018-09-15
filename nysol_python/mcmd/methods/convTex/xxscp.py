#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nysol.mcmd as nm

with open('dat1.xml','w') as f:
  f.write(
'''<a att="aa">
<b att="bb1">
<c p="pp1" q="qq1"/>
<d>text1</d>
</b>
<b att="bb2">
<c q="qq2"></c>
<d>text2</d>
</b>
<b>
<c p="pp3"/>
<d>text3</d>
</b>
</a>
''')

import nysol.mcmd as nm

nm.mxml2csv(k="/a", f="/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a", i="dat1.xml", o="rsl3.csv").run()
