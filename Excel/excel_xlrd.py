__author__ = 'jinfeng'

import xlrd
from tempfile import TemporaryFile
from xlwt import Workbook

def excel_read():
    fname = "sample.xls"
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in %s named Sheet1" % fname
        return None
    nrows = sh.nrows
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows, ncols)

    row_list = []
    for i in range(0, nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)
    print 'all rows: ', row_list

    col_list = []
    for i in range(0, ncols):
        col_data = sh.col_values(i)
        col_list.append(col_data)
    print 'all columns: ', col_list

    cell_value = sh.cell_value(0, 0)
    print 'cell(3,2): ', cell_value


def excel_write():
    book = Workbook()
    sheet1 = book.add_sheet('Sheet1')
    book.add_sheet('Sheet2')
    sheet1.write(0, 0, 'A1')
    sheet1.write(0, 1, 'B1')
    row1 = sheet1.row(1)
    row1.write(0, 'A2')
    row1.write(1, 'B2')
    sheet1.col(0).width = 10000
    sheet2 = book.get_sheet(1)
    sheet2.row(0).write(0, 'Sheet 2 A1')
    sheet2.row(0).write(1, 'Sheet 2 B1')
    sheet2.flush_row_data()
    sheet2.write(1, 0, 'Sheet 2 A3')
    sheet2.col(0).width = 5000
    sheet2.col(0).hidden = True
    book.save('sample.xls')
    book.save(TemporaryFile())

if __name__ == '__main__':
    excel_read()
    #excel_write()
