# tableformat.py

class TableFormatter:
	def headings(self, headers):
		'''
		Emit the table headings
		'''
		raise NotImplementedError()
	def row(self, rowdata):
		'''
		Emit a single row of table data
		'''
		raise NotImplementedError()

class TextTableFormatter(TableFormatter):
	'''
	Emit a table in plain-text format
	'''
	def headings(self, headers):
		for h in headers:
			print(f'{h:>10s}', end=' ')
		print()
		print(('-'*10 + ' ') * len(headers))

	def row(self, rowdata):
		for d in rowdata:
			print(f'{d:>10s}', end=' ')
		print()

class CSVTableFormatter(TableFormatter):
	'''
	Output portfolio data in CSV format
	'''
	def headings(self, headers):
		print(','.join(headers))

	def row(self, rowdata):
		print(','.join(rowdata))

def create_formatter(fmt):
	if fmt == 'txt':
		return TextTableFormatter()
	elif fmt == 'csv':
		return CSVTableFormatter()
	else:
		raise RuntimeError(f'Unknown format {fmt}')

def print_table(data, attributes, formatter):
	'''
	Print a table showing user-specified attributes of a list of arbitrary objects
	'''
	formatter.headings(attributes)
	for instance in data:
		rowdata = [str(getattr(instance, attribute)) for attribute in attributes]
		formatter.row(rowdata)