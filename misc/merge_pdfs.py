#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyPDF2
import sys
import time


def add_pages(pdf_reader, pdf_writer):
	for page_num in range(pdf_reader.numPages):
		page_obj = pdf_reader.getPage(page_num)
		pdf_writer.addPage(page_obj)

if __name__ == '__main__':
	get_pdfs = [sys.argv[1:]]

	# first pdf file
	pdf_writer = PyPDF2.PdfFileWriter()
	for pdf in get_pdfs:
		with open(pdf, 'rb') as pdf_file:
			add_pages(PyPDF2.PdfFileReader(pdf_file), pdf_writer)

	merged_pdf_filename = str(time.time()) + '.pdf'

	with open(merged_pdf_filename, 'wb') as output:
		pdf_writer.write(merged_pdf_filename)
