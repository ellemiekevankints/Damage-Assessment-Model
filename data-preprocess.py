import os
import shutil
from PIL import Image

def organize_data():
    
    """ Split the data into a training group and testing group. Each group will be 
    organized into damage and non-damage folders, corresponding to the two class labels.
    """
     
    for file in os.listdir('data/raw-train-data'):
        
        if file.endswith('pre_disaster.png'):         
            src = 'data/raw-train-data/' + file 
            shutil.copy(src, 'data/train/no-damage')
    
        elif file.endswith('post_disaster.png'):
            src = 'data/raw-train-data/' + file  
            shutil.copy(src, 'data/train/damage')
        
        else: 
            src = 'data/raw-train-data/' + file  
            shutil.copy(src, 'data/train/other')
    
    print("DONE PROCESSING TRAINING IMGS")
      
    for file in os.listdir('data/raw-test-data'):
    
        if file.endswith('pre_disaster.png'):      
            src = 'data/raw-test-data/' + file
            shutil.copy(src, 'data/test/no-damage')
        
        elif file.endswith('post_disaster.png'): 
            src = 'data/raw-test-data/' + file
            shutil.copy(src, 'data/test/damage')
        
        else: 
            src = 'data/raw-test-data/' + file
            shutil.copy(src, 'data/test/other')

    print("DONE PROCESSING TESTING IMGS") 
    
    for file in os.listdir('data/raw-valid-data'):
        
        if file.endswith('pre_disaster.png'):      
            src = 'data/raw-valid-data/' + file
            shutil.copy(src, 'data/valid/no-damage')
        
        elif file.endswith('post_disaster.png'): 
            src = 'data/raw-valid-data/' + file
            shutil.copy(src, 'data/valid/damage')
        
        else: 
            src = 'data/raw-valid-data/' + file
            shutil.copy(src, 'data/valid/other')

    print("DONE PROCESSING VALIDATION IMGS")   

def compress_data():
    
    """ Compress each image file to 512x512 pixels. """
    
    for file in os.listdir('data/train/damage'):
        
        src = 'data/train/damage/' + file 
        img = Image.open(src)
        img = img.resize((512,512), Image.ANTIALIAS)
        
        dst = 'processed-data/train/damage/' + file
        img.save(dst, optimize=True, quality=95)
    
    for file in os.listdir('data/train/no-damage'):   
        
        src = 'data/train/no-damage/' + file 
        img = Image.open(src)
        img = img.resize((512,512), Image.ANTIALIAS)
        
        dst = 'processed-data/train/no-damage/' + file
        img.save(dst, optimize=True, quality=95) 
    
    for file in os.listdir('data/test/damage'):
        
        src = 'data/test/damage/' + file 
        img = Image.open(src)
        img = img.resize((512,512), Image.ANTIALIAS)
        
        dst = 'processed-data/test/damage/' + file
        img.save(dst, optimize=True, quality=95) 
        
    for file in os.listdir('data/test/no-damage'):
        
        src = 'data/test/no-damage/' + file 
        img = Image.open(src)
        img = img.resize((512,512), Image.ANTIALIAS)
        
        dst = 'processed-data/test/no-damage/' + file
        img.save(dst, optimize=True, quality=95)  
    
    for file in os.listdir('data/valid/damage'):
            
        src = 'data/valid/damage/' + file 
        img = Image.open(src)
        img = img.resize((512,512), Image.ANTIALIAS)
        
        dst = 'processed-data/valid/damage/' + file
        img.save(dst, optimize=True, quality=95)  
     
    for file in os.listdir('data/valid/no-damage'):
            
        src = 'data/valid/no-damage/' + file 
        img = Image.open(src)
        img = img.resize((512,512), Image.ANTIALIAS)
        
        dst = 'processed-data/valid/no-damage/' + file
        img.save(dst, optimize=True, quality=95)   

# MAIN PROGRAM
def main():     
    organize_data()
    compress_data() 
    
# DRIVER CODE
if __name__ == "__main__":
    main()