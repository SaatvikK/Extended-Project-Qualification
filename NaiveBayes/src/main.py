########### Random Info ###########
# Naive Bayes Classifier EPQ
# Saatvik Kambhampati
# 14/07/2021 - 
###################################

########### Importing Modules ###########
import csv;
import numpy as np;
from ClassOutcomes import classOutcome;
#########################################


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
      atts[0].append(float(data[i][0]));
      atts[1].append(str(data[i][1]));
      atts[2].append(float(data[i][2]));
      atts[3].append(float(data[i][3]));
      atts[4].append(float(data[i][4]));
      atts[5].append(float(data[i][5]));
      atts[6].append(float(data[i][6]));
      ClassOutcomes.append(str(data[i][7]));
    return [atts, ClassOutcomes];


  def readCSV(self):
    with open('../../training.csv', 'r') as file:
      data = [];
      for row in csv.reader(file):
        if("Age" not in row):
          data.append(row);
      
      return data;
  
  
  
  def generalProbabilities(self, outcomes):
    hypo.generalProbabilityClass(outcomes, "hypothyroid");
    hyper.generalProbabilityClass(outcomes, "hyperthyroid");
    no.generalProbabilityClass(outcomes, "no");
    #print("h1", hypo.GeneralProbability)
    #print("h2", hyper.GeneralProbability)
    #print("h3", no.GeneralProbability)

  def main(self):
    data = self.readCSV();
    res = self.getAtts(data);
    atts, classes = res[0], res[1];

    ########################
    TempAtts = atts;
    del TempAtts[1];

    self.generalProbabilities(classes)
    hypo.findingAttsGivenClasses(TempAtts, classes, "hypothyroid");
    hypo.pSexGivenClass(self.getAtts(data)[0], classes, "hypothyroid");
    hyper.findingAttsGivenClasses(TempAtts, classes, "hyperthyroid");
    hyper.pSexGivenClass(self.getAtts(data)[0], classes, "hyperthyroid");
    no.findingAttsGivenClasses(TempAtts, classes, "no");
    no.pSexGivenClass(self.getAtts(data)[0], classes, "no");

    
    print("hypo", hypo.CondProbAtts)
    print("hyper", hyper.CondProbAtts)
    print("no", no.CondProbAtts)
    
    evidence = (
      (
        hypo.GeneralProbability*
        hypo.CondProbAtts["age"]*hypo.CondProbAtts["tsh"]*hypo.CondProbAtts["t3"]*
        hypo.CondProbAtts["tt4"]*hypo.CondProbAtts["t4u"]*hypo.CondProbAtts["fti"]*
        hypo.CondProbAtts["sexes"]["males"]*hypo.CondProbAtts["sexes"]["females"]
      ) + (
        hyper.GeneralProbability*
        hyper.CondProbAtts["age"]*hyper.CondProbAtts["tsh"]*hyper.CondProbAtts["t3"]*
        hyper.CondProbAtts["tt4"]*hyper.CondProbAtts["t4u"]*hyper.CondProbAtts["fti"]*
        hyper.CondProbAtts["sexes"]["males"]*hyper.CondProbAtts["sexes"]["females"]
      ) + (
        no.GeneralProbability*
        no.CondProbAtts["age"]*no.CondProbAtts["tsh"]*no.CondProbAtts["t3"]*
        no.CondProbAtts["tt4"]*no.CondProbAtts["t4u"]*no.CondProbAtts["fti"]*
        no.CondProbAtts["sexes"]["males"]*no.CondProbAtts["sexes"]["females"]
      )
    )

    ###################################
    print("'Hypothyroid' predicted cases:", hypo.SpecificProb(evidence));
    print("'Hyperthyroid' predicted cases:", hyper.SpecificProb(evidence));
    print("'No' predicted cases:", no.SpecificProb(evidence));
    

hypo, hyper, no = classOutcome(), classOutcome(), classOutcome();
obj = main();
obj.main();