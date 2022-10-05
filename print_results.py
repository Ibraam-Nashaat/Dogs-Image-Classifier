
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    print("\nThe CNN model is {}".format(model))
    print("No of images is {}".format(results_stats_dic["n_images"]))
    print("No of dog images is {}".format(results_stats_dic["n_dogs_img"]))
    print("No of Not a dog images is {} ".format(results_stats_dic["n_notdogs_img"]))
    print("percenatge of match is {} %".format(results_stats_dic["pct_match"]))
    print("percenatge of correct dogs is {} %".format(results_stats_dic["pct_correct_dogs"]))
    print("percenatge of correct breed is {} %".format(results_stats_dic["pct_correct_breed"]))
    print("percenatge of correct not dogs is {} %".format(results_stats_dic["pct_correct_notdogs"]))
    
    n_correct_dogs=results_stats_dic["n_correct_dogs"]
    n_correct_notdogs=results_stats_dic["n_correct_notdogs"]
    n_images=results_stats_dic["n_images"]
    n_correct_breed=results_stats_dic["n_correct_breed"]
    if print_incorrect_dogs == True and n_correct_dogs + n_correct_notdogs != n_images :
        print("\nMisclassified dogs :")
        for key in results_dic.keys():
            if sum(results_dic[key][3:]) == 1:
                print("\nPet image label: {:>26}, Classifier label: {:>30}".format(results_dic[key][0],results_dic[key][1]))
                      
    
    if print_incorrect_breed == True and n_correct_dogs != n_correct_breed:
        print("\nMisclassified breed's of dogs :")
        for key in results_dic.keys():
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("\nPet image label: {:>26}, Classifier label:{:>30}".format(results_dic[key][0],results_dic[key][1]))
   