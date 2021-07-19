########### Importing Modules ###########
import numpy as np;
###################################

class hypothyroid():
  def __init__(self):
    self.means = [0, 0, 0, 0, 0]; #age, tsh, t3, tt4, t4u
    self.variances = [0, 0, 0, 0, 0]; #age, tsh, t3, tt4, t4u
    self.sexes = []; #males, females
  
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

  def thing(self, atts):
    for i in range(len(self.means)):
      self.means[i] = self.findMean(i, atts);
      self.variances[i] = self.findVariance(i, atts, self.means[i]);

