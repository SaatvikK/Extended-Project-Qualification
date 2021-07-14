########### Random Info ###########
# Attributes: Age, Sex, OnThyroxine, QueryOnThyroxine, OnAntiThyroidMeds, Sick, Pregnant, ThyroidSurgery, I131Treatment, QueryHypo, QueryHyper, Lithium, hyperthyroid, Tumor, Hypopituitary, Psych, TSHMeasured, TSH, T3Measured, T3, TT4Measured, TT4, T4UMeasured, T4U, FTIMeasured, FTI, TBGMeasured

#############################

class person:
  def __init__(self):
    return;
  
  def means(self, ages):
    """
    self.MeanAge, self.MeanSex, self.MeanOnThyroxine, self.MeanQueryOnThyroxine, self.MeanOnAntiThyroidMeds, self.MeanSick, self.MeanPregnant, 
    self.MeanThyroidSurgery, self.MeanI131Treatment, self.MeanQueryHypo, self.MeanQueryHyper, self.MeanLithium, self.Meanhyperthyroid, self.MeanTumor, 
    self.MeanHypopituitary, self.MeanPsych, self.MeanTSHMeasured, self.MeanTSH, self.MeanT3Measured, self.MeanTT4, self.MeanT4UMeasured, self.MeanT4U, 
    self.MeanFTIMeasured, self.MeanFTI, self.MeanTBGMeasured += 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
    """
    for i in range(len(ages)):
      self.MeanAge += ages[i];
    
    self.MeanAge /= len(ages);

    return True;


































































    """
    def age(self):
    def sex(self):
    def onThyroxine(self):
    def queryOnThyroxine(self):
    def sick(self):
    def pregnant(self):
    def thyroidSurgery(self):
    def I131Treatment(self):
    def queryHypo(self):
    def queryHyper(self):
    def lithium(self):
    def hyperThyroid(self):
    def hypopituitary(self):
    def psych(self):
    def tshMeasured(self):
    def tsh(self):
    def T3Measured(self):
    def T3(self):
    def TT4Measured(self):
    def TT4UMeasured(self):
    def T4U(self):
    def FTIMeasured(self):
    def FTI(self):
    def TBGMeasured(self):
"""