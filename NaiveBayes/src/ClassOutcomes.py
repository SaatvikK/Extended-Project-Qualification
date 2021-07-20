########### Importing Modules ###########
import numpy as np;
###################################

class classOutcome():
  def __init__(self):
    self.means = [0, 0, 0, 0, 0, 0]; #age, tsh, t3, tt4, t4u, fti
    self.variances = [0, 0, 0, 0, 0, 0]; #age, tsh, t3, tt4, t4u, fti
    self.pMaleClass, self.pFemaleClass = 0, 0;
    self.GeneralProbability = 0;
    self.CondProbAtts = {
      "sexes": {}
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
  
  def findVariance(self, index, atts, mean):
    squares = np.square(atts[index]);
    MeanOfSquares = 0;
    for i in range(len(squares)):
      MeanOfSquares += squares[i];
    
    MeanOfSquares /= len(squares);
    return np.absolute(MeanOfSquares - (mean*mean));
  
  def pSexGivenClass(self, atts, outcomes, WhichClass):
    sexes = atts[1];
    TotalMales, TotalFemales, TotalOutcome = 0, 0, 0;
    for i in range(len(sexes)):
      if(sexes[i] == "M"): TotalMales += 1;
      elif(sexes[i] == "F"): TotalFemales += 1;
      if(outcomes[i] == WhichClass): TotalOutcome += 1
    self.CondProbAtts["sexes"]["males"] = TotalMales/TotalOutcome
    self.CondProbAtts["sexes"]["females"] = TotalFemales/TotalOutcome;
  
  def attGivenClass(self, mean, variance, t):
    """
    (1/(np.sqrt(2*np.pi*variance)))
    ((-(np.square(6 - mean)))/(2*variance))
    """
    thing = (1/(np.sqrt(2*np.pi*variance)))*np.exp(((-(np.square(6 - mean)))/(2*variance)));
    return thing;

  def generalProbabilityClass(self, outcomes, WhichClass):
    ThisClass = 0;
    for i in range(len(outcomes)):
      if(outcomes[i] == WhichClass): ThisClass += 1;
    
    self.GeneralProbability = ThisClass/len(outcomes);

  def findingAttsGivenClasses(self, atts, outcomes, WhichClass):
    for i in range(len(atts)):
      self.means[i] = self.findMean(i, atts, WhichClass, outcomes);
      self.variances[i] = self.findVariance(i, atts, self.means[i]);
    
    # exit()

    self.CondProbAtts["age"] = self.attGivenClass(self.means[0], self.variances[0], "b");
    print(self.CondProbAtts["age"]);
    
    self.CondProbAtts["tsh"] = self.attGivenClass(self.means[1], self.variances[1], "n"); 
    self.CondProbAtts["t3"] = self.attGivenClass(self.means[2], self.variances[2], "n");
    self.CondProbAtts["tt4"] = self.attGivenClass(self.means[3], self.variances[3], "n");
    self.CondProbAtts["t4u"] = self.attGivenClass(self.means[4], self.variances[4], "y");
    self.CondProbAtts["fti"] = self.attGivenClass(self.means[5], self.variances[5], "n");
  
  def SpecificProb(self, evidence):
    return ((float(self.GeneralProbability)*
        float(self.CondProbAtts["age"])*float(self.CondProbAtts["tsh"])*float(self.CondProbAtts["t3"])*
        float(self.CondProbAtts["tt4"])*float(self.CondProbAtts["t4u"])*float(self.CondProbAtts["fti"])*
        float(self.CondProbAtts["sexes"]["males"])*float(self.CondProbAtts["sexes"]["females"])/float(evidence)));
    
    

