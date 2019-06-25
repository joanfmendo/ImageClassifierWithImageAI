# Image Classifier With ImageAI (Python 3)
This is a simple tutorial on how to use some neural networks to classify images. The algorithms chosen are those contained in the ImageAI package for Python 3 (SqueezeNet, ResNet, InceptionV3 and DenseNet). It is very simple to implement and very easy to understand. 

**I strongly recommend using Google Colab** to run these scripts, since neural networks require a lot of computing and memory capacity. The best thing is that GColab is free!! You can find a tutorial [here](https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d).

As you can read on  [**IMAGEAI** website](http://imageai.org/) *"ImageAI is an easy to use Computer Vision Python library that empowers developers to easily integrate state-of-the-art Artificial Intelligence features into their new and existing applications and systems. It is used by thousands of developers, students, researchers, tutors and experts in corporate organizations around the world."* It can be used for image recognition (this case), video detection and object detection.

For image recognition (or classification, it's the same) ImageAI offers these Neural Network (ANN) algorithms:
- Residual Neural Network (RESNET): read this [article](https://towardsdatascience.com/an-overview-of-resnet-and-its-variants-5281e2f56035)
- SQUEEZENET: read this [article](https://towardsdatascience.com/review-squeezenet-image-classification-e7414825581a).
- Densely Connected Convolutional Networks (DENSENET): read this [article](https://towardsdatascience.com/understanding-and-visualizing-densenets-7f688092391a).
- Inception Network (INCEPTIONV3): read this [article](https://towardsdatascience.com/a-simple-guide-to-the-versions-of-the-inception-network-7fc52b863202).

# HOW TO USE THE SCRIPTS
## 1. Format your training set
In the file **"ImageResize.py"** you can find a simple script to format and resize the images that you will use to your training. It contains 4 functions:
- `def ProportionalResize(filepath,scale_percent)`: function to resize an image based on a proportion (or percentage) of the original image
Example: `ProportionalResize(filepath="C:/mydir/miimage.jpg",scale_percent=0.6)` resizes the image to 60%
- `def CustomResize(filepath,width, height)`: Function to resize an image based on a given dimension
Example: `CustomResize(filepath="C:/mydir/miimage.jpg",width=300, height=200)` resizes the size to 300x200 pixels
- `def WidthBasedResize(filepath,width)`: function to resize an image based on is width
Example: `WidthBasedResize(filepath="C:/mydir/miimage.jpg",width=300)` resizes the image to a width of 300px while retaining its proportional height
- `def HeightBasedResize(filepath,Height)`: function to resize an image based on is height
Example: `HeightBasedResize(filepath="C:/mydir/miimage.jpg",Height=300)` resizes the image to a height of 300px while retaining its proportional width

Here is an example code to resize all images to 200x200px, given an "original files path" and a "resized files path" as output:

>`from os import listdir`
>`from os.path import isfile, join`
>`import os`
>
>`os.getcwd()`
>
>`ofp = 'original images/' #Original Files Path`
>`rfp = 'resized images/' #Resized Files Path`
>`files = [f for f in listdir(ofp) if isfile(join(ofp, f))]`
>
>`width = 200`
>`height = 200`
>`for file in files:`
>`    print(file)`
>`    resized = CustomResize(str(ofp+file), width, height)`
>`    cv2.imwrite(str(rfp+'resized_'+file), resized)`

Remember that your formated images must be stored in a sub-forder placed in the folder where you will run your python scripts (i.e: "My project/jobs"), and inside that folder (in this case, "jobs") you must place two subfolders "jobs/train" and "jobs/test". Inside both "train" and "test" folders you must separate the images by their category (in this case "test/chef", "test/judge" or "test/pilot"). [**Please use this data set to understand how the files have to be stored**](https://github.com/OlafenwaMoses/IdenProf/releases/download/v1.0/idenprof-jpg.zip).

## 2. Use a Neural Network to classify your images

If you have a very powerful computer you can use the file **"ImageClassifier.py"**. Otherwise I suggest to use the file **"image_classification.ipynb"** to be processed in **Google Colab**. Remember: there is a tutorial to use GColab [here](https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d).

Both files contains these functions:
- `def TrainModel(files, Classes, Epochs, BatchSize)`: the training function that requires these parameters:
>    `files`: path to your set of images
>    `number_objects`: number of clases of your dataset (i.e.: 10 clases of jobs)
>    `num_experiments`: number of iterations (epochs)
>    `Enhance_data` (Optional): if true, creates modified copies of the images to maximize accuracy (but more process cost)
>    `batch_size`: number of images that the model trainer will study at once
>    `Show_network_summary` (Optional): if true, shows the structure of the model type
Example: `def TrainModel(files= "/gdrive/My Drive/My Project/ImagesFolder", Classes=10, Epochs=100, BatchSize=24)`

The `TrainModel` function will deliver two outputs: a .h5 file that contains the trained model and a .json file that contains the classes of the model. The first file will be stored in */My Project/ImagesFolder/jobs/models* and the second one in */My Project/ImagesFolder/jobs/json*. It will store a new file model each time that accuracy is improved.

- `ImageClassifier(Image, ModelFile, JsonFile, Classes)`: the training function that requires these parameters:
>    `Image`: path to the image that you want to classify
>    `ModelFile`: path to the model trained with the `TrainModel` function.
>    `JsonFile`: path to the file that contains the list of classes trained with the `TrainModel` function.

Here is an example code to train your model (in Google Colab):
>`from google.colab import drive`
>`drive.mount('/gdrive')`
>`import os`
>
>`Classes = 2 #number of classes`
>`Epochs = 250 #humber of epochs`
>`BatchSize = 30 #batch size`
>`files = "/gdrive/My Drive/My Project/ImagesFolder"`

>`TrainModel(files, Classes, Epochs, BatchSize)`

And here is a sample code to classify your images:

>`from os import listdir`
>`from os.path import isfile, join`
>`import os`
>`tfp = 'test images/' #Test Files Path`
>`files = [f for f in listdir(tfp) if isfile(join(tfp, f))]`
>
>`for file in files:`
>`    result = ImageClassifier(str(tfp+file), ModelFile, JsonFile, Classes)`
>`    print(str(file)+": "+str(result))`
