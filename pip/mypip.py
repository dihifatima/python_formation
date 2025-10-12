# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 23:37:59 2025

@author: Admin
"""

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

