
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
   
    file_names= listdir(image_dir)
    results_dic=dict()
    for file_name in file_names:
        if file_name.startswith('.'):
            continue
        else:
            if file_name not in results_dic:
                pet_name=file_name.lower().split('_')
                label=""
                for word in pet_name:
                    if word.isalpha():
                        label+=word+" "
                label=label.strip()
                results_dic[file_name]=[label]
    return results_dic
