
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sktime.classification.interval_based import TimeSeriesForestClassifier
from sklearn import svm
import wfdb
import os
import numpy as np


def getGBMScores(x, y, testSize):

    # Declare the classifier
    classifier = GradientBoostingClassifier()

    trainAcc, testAcc = [], []

    # Split the data into training and testing sets
    XTrain, XTest, yTrain, yTest = train_test_split(x, y, test_size = testSize, random_state=42)

    # Train Classifier using classifier.fit method
    classifier.fit(XTrain, yTrain)

    # Predict XTest and record testing accuracy
    yPredTest = classifier.predict(XTest)
    testAccuracy = accuracy_score(yTest, yPredTest)
    testAcc.append(testAccuracy)

    # Predict XTrain and record training accuracy
    yPredTrain = classifier.predict(XTrain)
    trainAccuracy = accuracy_score(yTrain, yPredTrain)
    trainAcc.append(trainAccuracy)

    return trainAcc, testAcc

def getSVMScores(x, y, testSize):

    # Declare the classifier
    classifier = svm.SVC()

    trainAcc, testAcc = [], []

    # Split the data into training and testing sets
    XTrain, XTest, yTrain, yTest = train_test_split(x, y, test_size = testSize, random_state=42)

    # Train Classifier using classifier.fit method
    classifier.fit(XTrain, yTrain)

    # Predict XTest and record testing accuracy
    yPredTest = classifier.predict(XTest)
    testAccuracy = accuracy_score(yTest, yPredTest)
    testAcc.append(testAccuracy)

    # Predict XTrain and record training accuracy
    yPredTrain = classifier.predict(XTrain)
    trainAccuracy = accuracy_score(yTrain, yPredTrain)
    trainAcc.append(trainAccuracy)

    return trainAcc, testAcc

def getTSFScores(x, y, numberEstimators, testSize):

    # Declare the classifier
    classifier = TimeSeriesForestClassifier(n_estimators=numberEstimators)
    trainAcc, testAcc = [], []

    # Split the data into training and testing sets
    XTrain, XTest, yTrain, yTest = train_test_split(x, y, test_size=testSize, random_state=42)

    # Train Classifier using classifier.fit method
    classifier.fit(XTrain, yTrain)

    # Predict X_test and record testing accuracy
    yPredTest = classifier.predict(XTest)
    testAccuracy = accuracy_score(yTest, yPredTest)
    testAcc.append(testAccuracy)

    # Predict X_train and record training accuracy
    yPredTrain = classifier.predict(XTrain)
    trainAccuracy = accuracy_score(yTrain, yPredTrain)
    trainAcc.append(trainAccuracy)

    return trainAcc, testAcc


def getApgar1(fields):
  #apgar retreaval
  metaData = fields['comments']
  apgar1String = metaData[6]

  # Split the string into parts based on spaces
  parts = apgar1String.split()

  # The last part should be the number
  apgar1 = int(parts[-1])

  if apgar1 in range(0, 4):
      return "concerning"
  elif apgar1 in range(4, 7):
      return "abnormal"
  elif apgar1 in range(7, 11):
      return "normal"
  else:
      return "Invalid Apgar1 score"
  
def XYArrayMakeLocal():
    x, y = [], []
    for filename in os.listdir('data'):
        # Check if the file is a .dat file and its name is between '1001' and '2046'
        if filename.endswith('.dat') and '1001' <= filename[:-4] <= '2046':
            # Use 'rdsamp' to read the .dat file
            signals, fields = wfdb.rdsamp('data/' + filename[:-4])

            # Get the first two signals
            signal_0 = signals[:, 0]
            signal_1 = signals[:, 1]

            # Truncate the signals to a length of 14400 from the end
            signal_0 = signal_0[-14400:]
            signal_1 = signal_1[-14400:]

            # Concatenate the two signals into a single long signal
            xData = np.concatenate((signal_0, signal_1))

            # Append the data to the 'x' list
            x.append(xData)

            # Append the apgar1 urgency class ["Concerning", "Abnormal", "Normal"]
            apgar1 = getApgar1(fields)
            y.append(apgar1)

    # Convert the list to a numpy array
    y = np.array(y)
    x = np.array(x)
    print('X first/last 3 values', x[:3], " ... ", x[:-4])
    print('Y first/last 3 values', y[:3], " ... ", y[:-4])
    print('X matryx shape :', x.shape)
    print('Y matryx shape :', y.shape)
    return x, y



