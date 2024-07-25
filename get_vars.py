from website import db
from website.models import PDM

cities = []
zip = []

for i in PDM.query.all():
    if str(i.zip) in zip:
        continue
    else:
        zip.append(str(i.zip))

for i in PDM.query.all():
    if i.city in cities:
        continue
    else:
        cities.append(i.city)

print(cities)
print(zip)
