#!/usr/bin/env python
# -*- coding: utf-8 -*-


def remove_duplicates(lst):
	lst_final = []
	for i in lst:
		if i not in lst_final:
			lst_final.append(i)

	return lst_final

print remove_duplicates([1, 2, 3, 5, 6, 6, 7, 4, 6])
