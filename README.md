# Dogs-Image-Classifier
- Dogs Image Classifier classifies pet images to dogs and not dogs and identify the breeds of the classified dogs using transfer learning via PyTorch pretrained models.
- This project was done as a part of Udacity's **AI Programming with Python Nanodegree**, where a skeleton of the project was provided.
## Objectives
1. Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs.
2. Correctly classify the breed of dog, for the images that are of dogs.
3. Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve objectives 1 and 2.
4. Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.
## Project's Outline
- **Time the program:** Use Time Module to compute program runtime.
- **Get program Inputs from the user:** Use command line arguments to get user inputs.
- **Create Pet Images Labels:** 
  - Use the pet images filenames to create labels.
  - Store the pet image labels in a data structure (e.g. dictionary).
- **Create Classifier Labels and Compare Labels:**
  - Use the Classifier function to classify the images and create the classifier labels.
  - Compare Classifier Labels to Pet Image Labels.
  - Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists).
- **Classifying Labels as "Dogs" or "Not Dogs":**
  - Classify all Labels as "Dogs" or "Not Dogs" using `dognames.txt` file.
  - Store new classifications in the complex data structure (e.g. dictionary of lists).
- **Calculate the Results:**
  - Use Labels and their classifications to determine how well the algorithm worked on classifying images.
- **Print the Results**

### Note 
- The output of the each model in the project was stored in the following `.txt` files:
  - `alexnet_pet-images.txt`
  - `resnet_pet-images.txt`
  - `vgg_pet-images.txt`
