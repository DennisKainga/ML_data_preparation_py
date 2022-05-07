import shutil
import glob
import os

class_names=[]
base_dir= os.path.join('path/to/base/of/dataset/')

def create_dataset(): 
    #scan through the directory to find image classes
    for class_name in os.listdir(base_dir):
        #use os.path.join to get full path of item
        path_to_images=os.path.join(base_dir,class_name)
    
        #check if current item is a directory
        if os.path.isdir(path_to_images):
            #scan the directory contents os.listdir returns an array of all items
            #.glob unlike os.listdir returns the full path to image os.listdir returns an array with only images
            #.glob also matches files in directory with pattern specified as arguement
            class_names.append(class_name)
            images = glob.glob(path_to_images+ '/*.jpg')
            #slice value assings 80% of images to trining and 20% of images to validation
            slice_value = round(len(images)*0.8)
            #can be read as for simplicity from 0 - 80% and from 80%  - 100% where 0.8 correspond to 80%
            training_images,val_images = images[:slice_value],images[slice_value:]
            
            train_path = os.path.join(base_dir,'train',class_name)
            val_path = os.path.join(base_dir,'val',class_name)
            
            for training_image in training_images:
                #create directories for training image classes
                if not os.path.exists(train_path):
                    os.makedirs(train_path)
                shutil.move(training_image,train_path)

            num_trainig,num_val,total_images = len(training_images),len(val_images),len(images)

            train_percent = round((num_trainig/total_images)*100)
            val_percent = round((num_val/total_images)*100)
            
            print('{} \nTotal {}:\n{} Training images ({}%)\n{} Validation images ({}%)\n'.format(class_name.title(),total_images,num_trainig,train_percent,num_val,val_percent))
            for val_image in val_images:
                if not os.path.exists(val_path):
                    os.makedirs(val_path)
                shutil.move(val_image,val_path)
            
            #delete folder after image transfer is done
            shutil.rmtree(path_to_images)

create_dataset()

          

