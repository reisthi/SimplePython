#!/usr/bin/python3

import xlrd
import openpyxl

file = xlrd.open_workbook('csv_files/leave_codes.xlsx')
sheet = file.sheet_by_index(0)

table = list()
record = list()

for x in range(sheet.nrows):
    for y in range(sheet.ncols):
        record.append(sheet.cell(x, y).value)
        table.append(record)
        # record = []

print(table)


water = openpyxl.load_workbook('csv_files/Waterbodies.xlsx')
sheet = water.active
cells = sheet['A1': 'C1772']
d = dict()
a = 0
for c1, c2, c3 in cells:
        d[a] = c1.value, c2.value, c3.value
        a += 1

################################################################################
# Create Genus
# un = Family.objects.get(name__icontains="UNK")
# for a in d.values():
#     if not Genus.objects.filter(name__icontains=a[2]):
#         Genus.objects.create(name=a[2], family=un)
# ################################################################################


###############################################################
# from datetime import datetime, timedelta
# yes = datetime.today() - timedelta(days=1)
# Species.objects.filter(created__gte=yes).delete()
###############################################################


##################################################################
# fish = Class.objects.get(name='Fish')
# tt = 0
# for a in d.values():
#     try:
#         g = Genus.objects.get(name__icontains=a[2].rstrip())
#     except Genus.MultipleObjectsReturned:
#         print("exception")
#         g = Genus.objects.get(name=a[2].rstrip())
#     if Species.objects.filter(common_name=a[0]):
#         Species.objects.filter(common_name=a[0]).update(scientific_name=a[1], genus=g, classification=fish)
#     else:
#         Species.objects.get_or_create(common_name=a[0], scientific_name=a[1], genus=g, classification=fish)
#     print(g)
#     tt += 1

##################################################################
