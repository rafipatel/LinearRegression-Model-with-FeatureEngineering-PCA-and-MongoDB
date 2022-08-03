# -*- coding: utf-8 -*-
"""Script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NbQYO-P-5-hgVrQBgz9q9ydA4RxfbAlS
"""

import pandas as pd
import pickle

def predict(data,model):
  model = pickle.load(open(model, 'rb'))
  data = pd.read_csv(data)
  data['Total Heat Recovery System Header Mass Flow'] = data['Heat Recovery System Header Mass Flow'] + data['Heat Recovery System Header Mass Flow.1']
  data['Pump Suction Pressure'] = data['Pump Suction Pressure 1'] + data['Pump Suction Pressure 2']
  data = data.drop(['Heat Recovery System Header Mass Flow','Heat Recovery System Header Mass Flow.1',
              'Motor Input Power', 'Motor Power Factor','Pump Radial Bearing Vibration'],axis =1)
  prediction = model.predict(data) 
  
  return prediction


