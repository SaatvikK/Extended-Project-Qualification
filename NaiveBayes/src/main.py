########### Random Info ###########
# Naive Bayes Classifier EPQ
# Saatvik Kambhampati
# 14/07/2021 - 
###################################

########### Importing Modules ###########
import csv;
import numpy as np;
from ClassOutcomes import classOutcome;
###################################


class main():
  def __init__(self):
    return;
  
  def getAtts(self, data):
    atts = [
            [], #age
            [], #sex
            [], #tsh
            [], #t3
            [], #tt4
            [], #t4u
            [] #fti
           ];
    
    ClassOutcomes = [] #hypo, hyper, negative/no.

    for i in range(len(data)):
      atts[0].append(int(data[0]));
      atts[1].append(str(data[1]));
      atts[2].append(float(data[2]));
      atts[3].append(float(data[3]));
      atts[4].append(float(data[4]));
      atts[5].append(float(data[5]));
      atts[6].append(int(data[6]));
      ClassOutcomes.apppend(str(data[7]));
    return [atts, ClassOutcomes];

  def readCSV(self):
    with open('../../training.csv', 'r') as file:
      data = [];
      for row in csv.reader(file):
        if("Age" not in row):
          data.append(row);
      
      return data;

  
  def main(self):
    data = self.readCSV();
    res = getAtts(data);
    atts, classes = res[0], res[1];
    
hypo, hyper, no = classOutcome(), classOutcome(), classOutcome();
obj = main();
obj.main();