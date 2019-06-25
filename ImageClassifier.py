'''
pip install tensorflow
pip install numpy
pip install scipy
pip install opencv-python
pip install pillow
pip install matplotlib
pip install h5py
pip install keras
pip3 install imageai
'''
from imageai.Prediction.Custom import ModelTraining
from imageai.Prediction.Custom import CustomImagePrediction
import os

### TRAIN MODEL FUNCTION

def TrainModel(files, Classes, Epochs, BatchSize):
    model_trainer = ModelTraining() #create an instance for de model training
    model_trainer.setModelTypeAsResNet() #set model to ResNet NN (SqueezeNet, ResNet, InceptionV3 and DenseNet)
    model_trainer.setDataDirectory(files) #folder that contains train and test sets

    '''
    train model function
    number_objects : number of clases
    num_experiments : number of iterations (epochs)
    Enhance_data (Optional) : if true, creates modified copies of the images to maximize accuracy (but more process cost)
    batch_size: number of images that the model trainer will study at once
    Show_network_summary (Optional) : if true, shows the structure of the model type
    '''
    model_trainer.trainModel(num_objects=Classes, num_experiments=Epochs, enhance_data=True, batch_size=BatchSize, show_network_summary=True)

### CLASSIFIER FUNCTION

def ImageClassifier(Image, ModelFile, JsonFile, Classes):
    execution_path = os.getcwd() #get model path
    prediction = CustomImagePrediction() #create instance for the prediction model
    prediction.setModelTypeAsResNet() #set classification model to ResNet
    prediction.setModelPath(ModelFile) #loads best model trained
    prediction.setJsonPath(JsonFile) #loads best model trained
    prediction.loadModel(num_objects=Classes) #Loads best model trained
    predictions, probabilities = prediction.predictImage(Image, result_count=3) #classify the image
    return predictions, probabilities

'''
# Train Model
Classes = 2 #number of classes
Epochs = 10 #humber of epochs
BatchSize = 30 #batch size
files = "ndty"
TrainModel(files, Classes, Epochs, BatchSize)
'''

# Classify Image
ModelFile = "/pathtomodel/model_ex-144_acc-0.827778.h5"
JsonFile = "/pathtojson/model_class.json"
Classes = 2
#Image = "image.jpg"
#result = ImageClassifier(Image, ModelFile, JsonFile, Classes)
#print(result)

from os import listdir
from os.path import isfile, join
import os
tfp = '/pat hto test images/' #Test Files Path
files = [f for f in listdir(tfp) if isfile(join(tfp, f))]

for file in files:
    result = ImageClassifier(str(tfp+file), ModelFile, JsonFile, Classes)
    print(str(file)+": "+str(result))