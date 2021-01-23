import xlwt

workbook = xlwt.Workbook(encoding="utf-8")   # xlwt.Workbool(解码标准)  创建excel对象
worksheet = workbook.add_sheet("sheet1")   # 创建一个单元sheet1
# worksheet.write(行,列,内容)
for i in range(0,9):
    for j in range(0, i+1):
            worksheet.write(i, j, "%d*%d=%d" % (i+1, j+1, (i+1)*(j+1)))
workbook.save('九九乘法表.xls')

