########### Random Info ###########
# Naive Bayes Classifier EPQ
# Saatvik Kambhampati
# 14/07/2021 - 
###################################

########### Importing Modules ###########
import csv;
import json;
import numpy as np;
import pandas as pd;
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


  def readCSV(self, FileName):
    with open('../' + FileName + '.csv', 'r') as file:
      data = [];
      for row in csv.reader(file):
        if("Age" not in row):
          data.append(row);
      
      return data;
  
  
  
  def generalProbabilities(self, outcomes, load):
    hypo.generalProbabilityClass(outcomes, "hypothyroid", load);
    hyper.generalProbabilityClass(outcomes, "hyperthyroid", load);
    no.generalProbabilityClass(outcomes, "no", load);


  def printShit(self):
    return "";


  def saveGeneralProbs(self):
    try:
      dict = {
        "hypothyroid": hypo.GeneralProbability,
        "hyperthyroid": hyper.GeneralProbability,
        "no": no.GeneralProbability
      };

      with open("../../NaiveBayes/GenProbs.json", "w") as file:
        json.dump(dict, file);
      
      return True;
    
    except Exception as e: return False;
  
  def evidence(self, i):
      return (
        (
          hypo.GeneralProbability*
          hypo.CondProbAtts["age"][i]*hypo.CondProbAtts["tsh"][i]*hypo.CondProbAtts["t3"][i]*
          hypo.CondProbAtts["tt4"][i]*hypo.CondProbAtts["t4u"][i]*hypo.CondProbAtts["fti"][i]*
          hypo.CondProbAtts["sexes"]["males"]*hypo.CondProbAtts["sexes"]["females"]
        ) + (
          hyper.GeneralProbability*
          hyper.CondProbAtts["age"][i]*hyper.CondProbAtts["tsh"][i]*hyper.CondProbAtts["t3"][i]*
          hyper.CondProbAtts["tt4"][i]*hyper.CondProbAtts["t4u"][i]*hyper.CondProbAtts["fti"][i]*
          hyper.CondProbAtts["sexes"]["males"]*hyper.CondProbAtts["sexes"]["females"]
        ) + (
          no.GeneralProbability*
          no.CondProbAtts["age"][i]*no.CondProbAtts["tsh"][i]*no.CondProbAtts["t3"][i]*
          no.CondProbAtts["tt4"][i]*no.CondProbAtts["t4u"][i]*no.CondProbAtts["fti"][i]*
          no.CondProbAtts["sexes"]["males"]*no.CondProbAtts["sexes"]["females"]
        )
      );

  def results(self, actual, predicted):
      # CONFUSION MATRIX
      PDactual = pd.Series(actual, name = "Actual");
      PDpredicted = pd.Series(predicted, name = "Predicted")
      print(pd.crosstab(PDactual, PDpredicted, rownames = ["Actual"], colnames = ["Predicted"], margins = True));

      # % Correct
      TotalCorrect, CorrectHypo, CorrectHyper, CorrectNo = 0, 0, 0, 0;
      PredictedHypo, PredictedNo, PredictedHyper = 0, 0, 0;
  
      for i in range(len(actual)):
        if(actual[i] == predicted[i]): 
          TotalCorrect += 1
          if(predicted[i] == "hypothyroid"): CorrectHypo += 1;
          elif(predicted[i] == "hyperthyroid"): CorrectHyper += 1;
          else: CorrectNo += 1;

        if(predicted[i] == "hypothyroid"): PredictedHypo += 1;
        elif(predicted[i] == "hyperthyroid"): PredictedHyper += 1;
        else: PredictedNo += 1;


      PercentCorrect = round((TotalCorrect/len(actual))*100, 2);
      print("Total correctly predicted: " + str(PercentCorrect) + "%");
      print("Total incorrectly predicted: " + str(round(100 - PercentCorrect, 2)) + "%");
      print("Out of all patients that were predicted 'hypothyroid', correct % predictions were: " + str(round((CorrectHypo/PredictedHypo)*100, 2)) + "%");
      print("Out of all patients that were predicted 'hyperthyroid', correct % predictions were: " + str(round((CorrectHyper/PredictedHyper)*100, 2)) + "%");
      print("Out of all patients that were predicted 'no', correct % predictions were: " + str(round((CorrectNo/PredictedNo)*100, 2)) + "%");

  def main(self):
    which = int(input("Testing [1] or training [2]? "));
    if(which == 1):
      data = self.readCSV("test");
      res = self.getAtts(data);
      atts, classes = res[0], res[1];
      ########################
      TempAtts = atts;
      del TempAtts[1];

      self.generalProbabilities(classes, True)
      hypo.findingAttsGivenClasses(TempAtts, classes, "hypothyroid", data);
      hypo.pSexGivenClass(self.getAtts(data)[0], classes, "hypothyroid");
      hyper.findingAttsGivenClasses(TempAtts, classes, "hyperthyroid", data);
      hyper.pSexGivenClass(self.getAtts(data)[0], classes, "hyperthyroid");
      no.findingAttsGivenClasses(TempAtts, classes, "no", data);
      no.pSexGivenClass(self.getAtts(data)[0], classes, "no");


      predicted, actual = [], [];
      for i in range(len(hypo.CondProbAtts["age"])):
        evidence = self.evidence(i);
        ProbHypo, ProbHyper, ProbNo = hypo.SpecificProb(evidence, i), hyper.SpecificProb(evidence, i), no.SpecificProb(evidence, i);
        print("COUNT:", i)
        if((ProbHypo > ProbHyper) and (ProbHypo > ProbNo)):
          print("================");
          print("Prediction: hypothyroid");
          print("Actual:", classes[i]);
          print("================");
          predicted.append("hypothyroid");
          actual.append(classes[i]);

        elif((ProbHyper > ProbHypo) and (ProbHyper > ProbNo)):
          print("================");
          print("Prediction: hyperthyroid");
          print("Actual:", classes[i]);
          print("================");
          predicted.append("hyperthyroid");
          actual.append(classes[i]);

        else:
          print("================");
          print("Prediction: no");
          print("Actual:", classes[i]);
          print("================");
          predicted.append("no");
          actual.append(classes[i]);
      
      self.results(actual, predicted);

    else:
      data = self.readCSV("training");
      res = self.getAtts(data);
      atts, classes = res[0], res[1];
      self.generalProbabilities(classes, False);
      self.saveGeneralProbs();

hypo, hyper, no = classOutcome(), classOutcome(), classOutcome();
obj = main();
obj.main();
