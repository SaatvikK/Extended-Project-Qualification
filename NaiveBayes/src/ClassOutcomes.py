########### Importing Modules ###########
import numpy as np;
import json;
###################################

class classOutcome():
  def __init__(self):
    self.means = [0, 0, 0, 0, 0, 0]; #age, tsh, t3, tt4, t4u, fti
    self.variances = [0, 0, 0, 0, 0, 0]; #age, tsh, t3, tt4, t4u, fti
    self.pMaleClass, self.pFemaleClass = 0, 0;
    self.TotalMales, self.TotalFemales = 0, 0;
    self.GeneralProbability = 0;
    self.CondProbAtts = {
      "sexes": {},
      "age": [],
      "tsh": [],
      "t3": [],
      "tt4": [],
      "t4u": [],
      "fti": []
    };
  
  def findMean(self, index, atts, WhichClass, outcomes):
    mean = 0;
    NumOfAges = 0;
    for i in range(len(atts[index])):
      try: 
        if(outcomes[i] == WhichClass): 
          mean += float(atts[index][i]);
          NumOfAges += 1;

      except Exception as e: print(e);

    mean /= NumOfAges;
    return mean;
  
  def findVariance(self, index, atts, mean, outcomes, WhichClass):
    MeanOfSquares, length = 0, 0;
    squares = []
    for i in range(len(atts[index])):
      try:
        if(outcomes[i] == WhichClass):
          MeanOfSquares += (np.square(atts[index][i]));
          squares.append(np.square(atts[index][i]))
          length += 1;
               
      except Exception as e: print(e);
    
    MeanOfSquares /= length;
    return np.absolute(MeanOfSquares - (mean*mean));
  
  def pSexGivenClass(self, atts, outcomes, WhichClass):
    sexes = atts[1];
    
    for i in range(len(sexes)):
      if((outcomes[i] == WhichClass) and sexes[i] == "M"): 
        self.TotalMales += 1
      elif((outcomes[i] == WhichClass) and sexes[i] == "F"): 
        self.TotalFemales += 1;
      
    self.CondProbAtts["sexes"]["males"] = self.TotalMales/len(sexes);
    self.CondProbAtts["sexes"]["females"] = self.TotalFemales/len(sexes);
  
  def attGivenClass(self, mean, variance, val):
    thing = (1/(np.sqrt(2*np.pi*variance)))*np.exp(((-(np.square(float(val) - mean)))/(2*variance)));
    return thing;

  def generalProbabilityClass(self, outcomes, WhichClass, load):
    if(load == False): #used for training
      ThisClass = 0;
      for i in range(len(outcomes)):
        if(outcomes[i] == WhichClass): ThisClass += 1;
    
      self.GeneralProbability = ThisClass/len(outcomes);
    else: #used for tesing
      with open("../../GenProbs.json") as file:
        data = json.load(file);
        self.GeneralProbability = data[WhichClass];

  def findingAttsGivenClasses(self, atts, outcomes, WhichClass, data):
    for i in range(len(atts)):
      self.means[i] = self.findMean(i, atts, WhichClass, outcomes);
      self.variances[i] = self.findVariance(i, atts, self.means[i], outcomes, WhichClass);
    
    # exit()

    for i in range(len(data)):
      for j in range(len(data[i])):
        if("Age" in data[i]): break;
        if(j == 0):
          self.CondProbAtts["age"].append(self.attGivenClass(self.means[0], self.variances[0], data[i][j]));
        elif(j == 2):
          self.CondProbAtts["tsh"].append(self.attGivenClass(self.means[1], self.variances[1], data[i][j]));
        elif(j == 3):
          self.CondProbAtts["t3"].append(self.attGivenClass(self.means[2], self.variances[2], data[i][j]));
        elif(j == 4):
          self.CondProbAtts["tt4"].append(self.attGivenClass(self.means[3], self.variances[3], data[i][j]));
        elif(j == 5):
          self.CondProbAtts["t4u"].append(self.attGivenClass(self.means[4], self.variances[4], data[i][j]));
        elif(j == 6):
          self.CondProbAtts["fti"].append(self.attGivenClass(self.means[5], self.variances[5], data[i][j]));
  
  def SpecificProb(self, evidence, i):
    return ((float(self.GeneralProbability)*
        float(self.CondProbAtts["age"][i])*float(self.CondProbAtts["tsh"][i])*float(self.CondProbAtts["t3"][i])*
        float(self.CondProbAtts["tt4"][i])*float(self.CondProbAtts["t4u"][i])*float(self.CondProbAtts["fti"][i])*
        float(self.CondProbAtts["sexes"]["males"])*float(self.CondProbAtts["sexes"]["females"])/float(evidence)));
    
    

