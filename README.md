# Extended Project Qualification
 EPQ Repo.


*22/07/2021:*
L39 - 47 of `ClassOutcomes.py`. Branch: 20/07/2021
```
  def pSexGivenClass(self, atts, outcomes, WhichClass):
    sexes = atts[1];
    TotalOutcome = 0;
    for i in range(len(sexes)):
      if(sexes[i] == "M"): self.TotalMales += 1;
      elif(sexes[i] == "F"): self.TotalFemales += 1;
      if(outcomes[i] == WhichClass): TotalOutcome += 1
    self.CondProbAtts["sexes"]["males"] = self.TotalMales/TotalOutcome
    self.CondProbAtts["sexes"]["females"] = self.TotalFemales/TotalOutcome;
```

Realised this was wrong. To calculate Sex|Class or Sex and Class, you do:
p = (Total Num of Sex with Class)/(Total Num of Patients)


**NEW CODE**
```
  def pSexGivenClass(self, atts, outcomes, WhichClass):
    sexes = atts[1];
    TotalMalesAndClass, TotalFemalesAndClass = 0, 0;
    for i in range(len(sexes)):
      if((outcomes[i] == WhichClass) and sexes[i] == "M"): 
        TotalMalesAndClass += 1;
        self.TotalMales += 1
      elif((outcomes[i] == WhichClass) and sexes[i] == "F"): 
        TotalFemalesAndClass += 1;
        self.TotalFemales += 1;
      
    self.CondProbAtts["sexes"]["males"] = TotalMalesAndClass/len(sexes);
    self.CondProbAtts["sexes"]["females"] = TotalFemalesAndClass/len(sexes);
```


L30 to 37 of `ClassOutcomes.py`:
```
  def findVariance(self, index, atts, mean):
    squares = np.square(atts[index]);
    MeanOfSquares = 0;
    for i in range(len(squares)):
      MeanOfSquares += squares[i];
    
    MeanOfSquares /= len(squares);
    return np.absolute(MeanOfSquares - (mean*mean));
```
This is wrong, on the first line I am squaring every instance of the attribute (reguardless of the classification). I *should actually* be only squaring the instances of the attribute that have the classification of a certain class (eg for hypothyroid and ages, only square the ages for which hypothyroid is true).

**NEW CODE**

