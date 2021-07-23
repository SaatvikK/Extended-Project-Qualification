# Extended Project Qualification
 EPQ Repo.


*23/07/2021:*
- Saving general probabilities to json file
- Doing first run on test.csv

1) L80 - 94 of `ClassOutcomes.py`, branch: 22/07/2021:
  ```
    def findingAttsGivenClasses(self, atts, outcomes, WhichClass):
    for i in range(len(atts)):
      self.means[i] = self.findMean(i, atts, WhichClass, outcomes);
      self.variances[i] = self.findVariance(i, atts, self.means[i], outcomes, WhichClass);
    
    # exit()

    self.CondProbAtts["age"] = self.attGivenClass(self.means[0], self.variances[0], "b");
    print(self.CondProbAtts["age"]);
    
    self.CondProbAtts["tsh"] = self.attGivenClass(self.means[1], self.variances[1]); 
    self.CondProbAtts["t3"] = self.attGivenClass(self.means[2], self.variances[2]);
    self.CondProbAtts["tt4"] = self.attGivenClass(self.means[3], self.variances[3]);
    self.CondProbAtts["t4u"] = self.attGivenClass(self.means[4], self.variances[4]);
    self.CondProbAtts["fti"] = self.attGivenClass(self.means[5], self.variances[5]);
  ```

  Shouldn't be finding the conditional probabilities of atts|classes for each attribute. 

2) L64 - 66 of `ClassOutcomes.py`, branch: 22/07/2021:
  ```
    def attGivenClass(self, mean, variance, t):
    thing = (1/(np.sqrt(2*np.pi*variance)))*np.exp(((-(np.square(6 - mean)))/(2*variance)));
    return thing;
  ```
  the `6` should not be a constant. This `6` should be the value of the patient of the attribute calculation.
  Eg: if the current patient's age is 42, that `6` should be 42 instead.


**CORRECT CODE**
1)
```
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
```

2) 
```
  def attGivenClass(self, mean, variance, val):
    thing = (1/(np.sqrt(2*np.pi*variance)))*np.exp(((-(np.square(float(val) - mean)))/(2*variance)));
    return thing;
```


ALSO ADDED CONFUSION MATRIX