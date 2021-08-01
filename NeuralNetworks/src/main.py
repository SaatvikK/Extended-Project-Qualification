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
import tensorflow as tf;
import matplotlib as plt;
import tensorflow.compat.v2.feature_column as fc;
#########################################

# Attributes
attributes = ["Age", "Sex", "TSH", "T3", "TT4", "T4U", "FTI"]; #Sex: male: 1, female: 0
classifications = ["hypothyroid", "hyperthyroid", "no"];

# Read CSV
train = pd.read_csv("../training.csv");
test = pd.read_csv("../test.csv");
TrainSpecies = train.pop('Class'); #Hypo: 1, Hyper: 2, No: 3
TestSpecies = test.pop('Class');
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
  input_fn = lambda: inputFunc(train, TrainSpecies, training = True),
  steps = 5000
);

# Testing the model
res = model.evaluate(
    input_fn = lambda: inputFunc(test, TestSpecies, training = False)
);

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**res))