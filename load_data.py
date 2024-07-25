import pandas as pd
import numpy as np
from website import db

df = pd.read_excel(r'C:\Users\matha\OneDrive\Desktop\insurnce_projecty\website\data.xlsx').dropna()

db.drop_all()

from website.models import PDM

db.create_all()

for ikey in df.T:
    attribute_list = []
    try:
        for attribute in df.iloc[ikey]:
            attribute_list.append(str(attribute))
        #print(attribute_list[9])
        facility = PDM(city=attribute_list[0], address=attribute_list[1], zip=attribute_list[2], facility_name=attribute_list[3], phone=attribute_list[4], services=attribute_list[5], facility_type=attribute_list[6], dental=attribute_list[7], mental=attribute_list[8], primary=str(attribute_list[9]))
        #print(facility.primary)
        db.session.add(facility)
    except:
        continue

db.session.commit()

