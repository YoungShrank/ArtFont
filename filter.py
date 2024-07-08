import numpy as np
import os
from PIL import Image
import shutil
from ttfutils import load_font,render
def load_image(path:str):
    """
    default image loader
    """
    image = Image.open(path)
    return image
def equal(image1:Image.Image,image2:Image.Image):
    """
    return if two images are equal
    """
    image1:np.ndarray = np.array(image1)
    image2:np.ndarray = np.array(image2)
    if image1.shape == image2.shape:
        return np.equal(image1,image2).all()
    else :
        return False
def in_images(image:Image.Image,images:list[Image.Image]):
    """
    return if the image is in the dir
    - image: image 
    - dir: dir
    """
    for image_ in images:
        if equal(image,image_):
            return True
    return False

def add_fault(new_path,fault_dir):
    """
    add fault image to fault dir,this function is used to collect fault examples
    - fault_dir: dir of fault images
    - new_path: path of new fault image
    """
    new_image = load_image(new_path)
    images = [load_image(os.path.join(fault_dir,name)) for name in os.listdir(fault_dir)]
    if not in_images(new_image,images):
        shutil.copy(new_path,fault_dir)
def filter_fault(ttf_path,fault_dir,chars):
    """
    filter fault chars in ttf,please make sure the same render parameters  are used
    - ttf_path: ttf file path
    - fault_dir: dir of fault images
    - chars: chars to filter
    # return:
    - fault_chars: chars in fault
    - support_chars: chars supported by ttf
    """
    fault_chars = set()
    chars = set(chars)
    try :
        font = load_font(ttf_path)
    except :
        return chars,set()
    fault_images = [load_image(os.path.join(fault_dir,name)) for name in os.listdir(fault_dir)]
    for char in chars :
        try :
            image = render(font,char)
            if in_images(image,fault_images):
                fault_chars.add(char)
        except :
            fault_chars.add(char)
    return fault_chars,chars - fault_chars
    

if __name__ == '__main__':
    fault_dir = 'faults'
    new_path = '锴.png'
    add_fault(new_path,fault_dir)

    

