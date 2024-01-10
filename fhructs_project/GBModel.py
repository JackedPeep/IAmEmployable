from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import warnings
import matplotlib.pyplot as plt
import wfdb
import os

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def getGBMScores(testSize):

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

def getApgar1():
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

x, y = [], []

# Iterate through all files in the 'data' directory
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
        apgar1 = getApgar1()
        y.append(apgar1)

# Convert the list to a numpy array
y = np.array(y)
x = np.array(x)
print('X first/last 3 values', x[:3], " ... ", x[-3:])
print('Y first/last 3 values', y[:3], " ... ", y[-3:])
print('X matryx shape :', x.shape)
print('Y matryx shape :', y.shape)



# Specify the test size for train_test_split
testSize = 0.2

# Train a SVM classifier and return the mean train and test accuracies
trainAccuracies, testAccuracies = getGBMScores(testSize)

print("The training accuracy is :")
print(trainAccuracies)

print("The testing accuracy is :")
print(testAccuracies)

meanTest, meanTrain = [], []
testSizes = np.linspace(0.1, 0.9, 9)  # or any other range of test sizes you want to use

for testSize in testSizes:
    # Call getGBMScores function with correct test size
    trainAcc, testAcc = getGBMScores(testSize)

    # Find and record the mean training and testing accuracies
    meanTrain.append(np.mean(trainAcc))
    meanTest.append(np.mean(testAcc))

# Plot mean training accuracies
plt.plot(testSizes, meanTrain, label='Training accuracy')

# Plot mean testing accuracies
plt.plot(testSizes, meanTest, label='Testing accuracy')

# Add title and labels
plt.title('Learning Curves')
plt.xlabel('Test Size')
plt.ylabel('Accuracy')

# Add a legend
plt.legend()

# Set the y-axis limits
plt.ylim(0, 1.1)

# Display the plot
plt.show()