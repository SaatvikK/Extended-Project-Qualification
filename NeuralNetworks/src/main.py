########### Random Info ###########
# Neural Networks Classifier EPQ
# Saatvik Kambhampati
# 14/07/2021 - 
###################################

########### Importing Modules ###########
import csv;
import json;
import numpy as np;
import pandas as pd;
import tensorflow as tf;
import matplotlib as plt;
import tensorflow.compat.v2.feature_column as fc;
#########################################

# Attributes
attributes = ["Age", "Sex", "TSH", "T3", "TT4", "T4U", "FTI"]; #Sex: male: 1, female: 0
classifications = ["hypothyroid", "hyperthyroid", "no"];

# Read CSV
train = pd.read_csv("/content/training.csv");
test = pd.read_csv("/content/test.csv");
TrainLabels = train.pop('Class'); #No: 0, Hypo: 1, Hyper: 2
TestLabels = test.pop('Class');
print(train)

# Input Function
def inputFunc(atts, labels, training = True, batch = 256):
  dataset = tf.data.Dataset.from_tensor_slices((dict(atts), labels));

  if (training):
    dataset = dataset.shuffle(1000).repeat();
  
  return dataset.batch(batch);

# Feature columns to describe how to use the input.
FeatureColumns = [];
for i in train.keys():
  FeatureColumns.append(tf.feature_column.numeric_column(key = i));

print(FeatureColumns);


# Creating neural network model, 2 hidden layers, with 39 and 10 hidden node each.
model = tf.estimator.DNNClassifier(
  feature_columns = FeatureColumns,
  hidden_units = [30, 10],
  n_classes = 4  
);

# Training the model
model.train(
  input_fn = lambda: inputFunc(train, TrainLabels, training = True),
  steps = 5000
);

# Testing the model
res = model.evaluate(
    input_fn = lambda: inputFunc(test, TestLabels, training = False)
);

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**res))

#List of prediction labels

predictions = list(model.predict(input_fn = lambda: inputFunc(test, TestLabels, training = False)));


PredictionLabels = [];
for i in range(len(predictions)):
  PredictionLabels.append(np.argmax(predictions[i]["probabilities"]));

PDactual = pd.Series(TestLabels, name = "Actual");
PDpredicted = pd.Series(PredictionLabels, name = "Predicted");
print(pd.crosstab(PDactual, PDpredicted, rownames = ["Actual"], colnames = ["Predicted"], margins = True));