import csv;

with open('../../training.csv', 'r') as InFile, open("../../../TrainingDataAfterDiscretization.csv", "w") as OutFile:
  writer = csv.writer(OutFile);
  file = [];
  for row in csv.reader(InFile):
    file.append(row);
  
  for  i in range(len(file)):
    for j in range(len(file[i])):
      if(j == 0):
        if(int(file[i][j]) >= 25):
          file[i][j] = "True";
        else:
          file[i][j] = "False";
      
      elif(j == 17):
        if(float(file[i][j]) >= 2.75):
          file[i][j] = "True";
        else:
          file[i][j] = "False";
      
      elif(j == 19):
        if(float(file[i][j]) >= 1.5):
          file[i][j] = "True";
        else:
          file[i][j] = "False";
          




min = float(input("Minimum: "));
max = float(input("Maximum: "));
diff = max - min;
print("The mid value of", min, "<= x <=", max, "is:", ((diff/2) + min));

