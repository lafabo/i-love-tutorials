#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lutz_study.makedb import loadDbase, storeDbase

db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
