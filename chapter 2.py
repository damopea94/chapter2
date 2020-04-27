import csv
import mysql.connector
import xlwt
from xlwt import Workbook


rows = []
def get_connection():
	connection = mysql.connector.connect(host='localhost', user='root',passwd='root',db='mydb')
	return connection


def read_csv_file(name):
	with open(name, 'r') as file:
		csv_data = csv.reader(file)
		print("read the file")
		fields = next(csv_data)

		for row in csv_data:
			rows.append(row)
		return fields


def create_table():
	fields = read_csv_file("assign11-1-ch02-data.csv")
	print(str(fields))

	connection = get_connection()
	cursor = connection.cursor()
	cursor.execute("drop table  IF exists ch02_data")

	table = "create table ch02_data (" + fields[0] + " varchar(255)," + fields[1]+" int (11))"
	print("table" , table)
	cursor.execute(table)
	connection.commit()


def insert_values():
	connection = get_connection()
	cursor = connection.cursor()
	print(len(rows))
	for row in rows :

		print(row[0])
		table = "insert into ch02_data values ('" + row[0] + "' ," + row[1] + ")"
		cursor.execute(table)
		connection.commit()
		print(str(row))
def sum_dates():
	connection = get_connection()
	cursor = connection.cursor()
	cursor.execute("select dates ,sum(numbers) from ch02_data group by dates")
	result = cursor.fetchall()
	return result


def save_sum():
	work_book = Workbook()
	sheet = work_book.add_sheet('results')
	column=0
	row=1;
	sql_results=sum_dates()
	sheet.write(0,0,"date ");
	sheet.write(0,1,"sum")
	for x in sql_results:
		sheet.write(row, column, x[0])
		sheet.write(row, (column+1), x[1])
		row = row+1
	work_book.save("Results.xls")


def main():
	# create_table()
	# insert_values()
	save_sum()


main()




