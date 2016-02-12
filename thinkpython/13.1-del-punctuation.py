#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string


text = open('text.txt').read().lower()
escapes = string.punctuation.split() + string.whitespace.split()

text = text.translate(None, str(escapes)).split()

print text
