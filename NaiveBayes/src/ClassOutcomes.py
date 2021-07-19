########### Importing Modules ###########
import numpy as np;
###################################

class classOutcome():
  def __init__(self):
    self.means = [0, 0, 0, 0, 0, 0]; #age, tsh, t3, tt4, t4u
    self.variances = [0, 0, 0, 0, 0, 0]; #age, tsh, t3, tt4, t4u
    self.pMaleClass, self.pFemaleClass = 0, 0;
  
  def findMean(self, index, atts):
    mean = 0;
    for i in range(len(atts[index])):
      try: 
        mean += int(atts[index][i]);

      except Exception as e: print(e);
    
    mean /= len(atts[index]);
    return mean;
  
  def findVariance(self, index, atts, mean):
    squares = np.square(atts[index]);
    MeanOfSquares = 0;
    for i in range(len(squares)):
      MeanOfSquares += squares[i];
    
    MeanOfSquares /= len(squares);

    return MeanOfSquares - (mean*mean);
  
  def pSexGivenClass(self, atts, outcomes, WhichClass):
    sexes = atts[1];
    TotalMales, TotalFemales, TotalOutcome = 0, 0, 0;
    for i in range(len(sexes)):
      if(sexes[i] == "M"): TotalMales += 1;
      elif(sexes[i] == "F"): TotalFemales += 1;
      if(outcomes[i] == WhichClass): TotalOutcome += 1
    return [TotalMales/TotalOutcome, TotalFemales/TotalOutcome]; #[p(Male|Outcome), p(Female|Outcome)]
  
  def AttGivenClass(self, mean, variance):
    return (1/(2*np.pi*variance))*np.exp((-(np.square(6 - mean)))/(2*np.square(variance)));
  
  def findingAttsGivenClasses(self):
    results = {
      
    };
    results["age"] = self.AttGivenClass(self.means[0], self.variances[0]);
    results["tsh"] = self.AttGivenClass(self.means[1], self.variances[1]); 
    results["t3"] = self.AttGivenClass(self.means[2], self.variances[2]);
    results["tt4"] = self.AttGivenClass(self.means[3], self.variances[3]);
    results["t4u"] = self.AttGivenClass(self.means[4], self.variances[4]);
    results["fti"] = self.AttGivenClass(self.means[5], self.variances[5]);

    return results;

