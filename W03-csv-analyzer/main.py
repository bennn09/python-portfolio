# with open("students.csv", "r", encoding="utf-8") as file:
#   print(file.read())

import csv
with open("students.csv", "r", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  students = list(reader)
  print(students)

for s in students:
  chinese = int(s["chinese"])
  english = int(s["english"])
  math = int(s["math"])
  average = (chinese + english + math) / 3
  print(s["name"], average)

for s in students:
  chinese = int(s["chinese"])
  english = int(s["english"])
  math = int(s["math"])
  average = (chinese + english + math) / 3
  print(s["name"], average)
for s in students:
  print(s["name"])
for s in students:
  chinese = int(s["chinese"])
  english = int(s["english"])
  math = int(s["math"])
  average = (chinese + english + math) / 3
  print("最高平均",max(average))