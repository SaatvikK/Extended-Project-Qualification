########### Random Info ###########
# Naive Bayes Classifier EPQ
# Saatvik Kambhampati
# 14/07/2021 - 
###################################

########### Importing Modules ###########
import csv;
###################################


class main():
  def __init__(self):
    return;
  
  def getAtts(self, data):
    atts = {
      "Age": [], 
      "Sex": [],
      "OnThyroxine": [],
      "QueryOnThyroxine": [], 
      "OnAntiThyroidMeds": [], 
      "Sick": [], 
      "Pregnant": [], 
      "ThyroidSurgery": [], 
      "I131Treatment": [], 
      "QueryHypo": [], 
      "QueryHyper": [], 
      "Lithium": [], 
      "hyperthyroid": [], 
      "Tumor": [], 
      "Hypopituitary": [], 
      "Psych": [], 
      "TSHMeasured": [], 
      "TSH": [], 
      "T3Measured": [], 
      "T3": [], 
      "TT4Measured": [], 
      "TT4": [], 
      "T4UMeasured": [], 
      "T4U": [], 
      "FTIMeasured": [], 
      "FTI": [], 
      "TBGMeasured": []
    };

    for i in range(len(data)):
      atts["Age"].append(int(data[0]));
      atts["Sex"].append(str(data[1]));
      atts["OnThyroxine"].append(bool(data[2]));
      atts["QueryOnThyroxine"].append(bool(data[3]));
      atts["OnAntiThyroidMeds"].append(bool(data[4]));
      atts["Sick"].append(bool(data[5]));
      atts["Pregnant"].append(bool(data[6]));
      atts["ThyroidSurgery"].append(bool(data[7]));
      atts["I131Treatment"].append(bool(data[8]));
      atts["QueryHypo"].append(bool(data[9]));
      atts["QueryHyper"].append(bool(data[10]));
      atts["Lithium"].append(bool(data[11]));
      atts["hyperthyroid"].append(bool(data[12]));
      atts["Tumor"].append(bool(data[13]));
      atts["Hypopituitary"].append(bool(data[14]));
      atts["Psych"].append(bool(data[15]));
      atts["TSHMeasured"].append(bool(data[16]));
      atts["TSH"].append(float(data[17]));
      atts["T3Measured"].append(bool(data[18]));
      atts["T3"].append(float(data[19]));
      atts["TT4Measured"].append(bool(data[20]));
      atts["TT4"].append(float(data[21]));
      atts["T4UMeasured"].append(bool(data[22]));
      atts["T4U"].append(float(data[23]));
      atts["FTIMeasured"].append(bool(data[24]));
      atts["FTI"].append(int(data[25]));
      atts["TBGMeasured"].append(bool(data[26]));
  
    return atts;

  def readCSV(self):
    with open('../../training.csv', 'r') as file:
      data = [];
      for row in csv.reader(file):
        if("Age" not in row):
          data.append(row);
      
      return data;

  def main(self):
    data = self.readCSV();
    atts = getAtts(data);
    

main().main();