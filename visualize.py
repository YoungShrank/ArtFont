#字形图可视化
import os
from PIL import ImageFont
from PIL import Image,ImageDraw
import math
TTF_ROOT = "ttfdemo"
_ttf_path = os.path.join(TTF_ROOT,'SourceHanSans-Heavy Bold Font(Google apple free open-source font)-Simplified Chinese-Traditional Chinese.otf')
font=ImageFont.truetype(_ttf_path,size=24)
EXTENSION = '.png'

def default_img_loader(path, width=64, height=64):
    """
    load image with specific size,if width or height is None (or 0), load original size
    - path: image path
    - width: width of image
    - height: height of image
    """
    if width  and height:
        return Image.open(path).convert('RGB').resize((width, height))
    return Image.open(path).convert('RGB')

def draw_axis(C,R,w,h,d,label=False):
    """
    draw axis
    - C:column number
    - R:row number
    - w:width of each cell
    - h:height of each cell
    - d:distance between two cells (or the size of the line)
    - label:whether to draw label
    # returns
    - axis:axis 
    - coord:coordinate of each cell represented by function coord(c,r)
    """
    
    dw = d+w
    dh = d+h
    if label ==False:
        DW = dw*C
        DH = dh*R
        coord = lambda c,r:(c*dw,r*dw)
    else :#label占宽为一格
        DW = dw*C+w
        DH = dh*R+h
        coord = lambda c,r:((c+1)*dw,(r+1)*dh)
    
    axis = Image.new('RGB',(DW,DH),(255,255,255))
    

    draw = ImageDraw.Draw(axis)

    for c in range(C): # 画列坐标线
        x,y = coord(c,0)
        x = x-d
        draw.line(((x,0),(x,y+DH)),fill=(0,0,0),width=d)
    for r in range(R): # 画行坐标线
        x,y = coord(0,r)
        y = y-d
        draw.line(((0,y),(x+DW,y)),fill=(0,0,0),width=d)
    #画lable
    for c in range(C):
        x,y = coord(c,0)
        draw.text((x,h/2),str(c),fill="red",font=font)
    for r in range(R):
        x,y = coord(0,r)
        draw.text((0,y),str(r),fill="red",font=font)
    
    return axis,coord
def show_grid(img_path_mat:list[list[str]],label=False,size=64):
    """
    show images indicated by img_path_mat in a grid,if the path at one coordinate doesn't exists,it will be left white
    - img_path_mat:image path matrix,the shape of img_path_mat is (R,C)
    - label:whether to draw label
    - size:size of each cell
    # returns
    - axis:the grid
    """
    R = len(img_path_mat)
    C = max([len(row) for row in img_path_mat])
    axis,coord = draw_axis(C,R,size,size,1,label=label)
    for r in range(R):
        for c in range(C):
            if c< len(img_path_mat[r]) and img_path_mat[r][c]:
                img = default_img_loader(img_path_mat[r][c],size,size)
                axis.paste(img,coord(c,r))
    return axis

def show_as_grid(img_path_list:list[str],C = None,label=False,size=64):
    """
    show images indicated by img_path_list in a grid
    - img_path_list:image path list
    - C:column number
    - label:whether to draw label
    - size:size of each cell
    # returns
    - axis:the grid
    """
    N = len(img_path_list)
    if C == None:
        C = int(N**0.5)
    C = math.ceil(N/C)
    img_path_mat = [img_path_list[i:i+C] for i in range(0,N,C)]
    axis =  show_grid(img_path_mat,label=label,size=size)
    return axis
def show_chars(font_dir_list:list[str],chars:list[str]):
    """
    show specific chars of each font,each row shows a font.
    - font_dir_list:font directory list
    - chars:chars list
    # returns
    - axis:the grid
    - mapper:font directory mapper (row index->font directory)
    """
    img_path_mat = [ ]
    mapper = {}
    for i,font_dir in enumerate(font_dir_list):
        row = []
        mapper[i] = font_dir
        for char in chars:
            img_path = os.path.join(font_dir,char+EXTENSION)
            if os.path.exists(img_path):
                row.append(img_path)
            else:
                row.append(None)
        img_path_mat.append(row)
    
    axis = show_grid(img_path_mat,label=True)
    return axis,mapper

def show_char(font_dir_list:list[str],char:str,C = None):
    """
    show a specific char of each font.
    - font_dir_list:font directory list
    - char:char
    - C:column number
    # returns
    - axis:the grid
    """
    img_path_list = [os.path.join(font_dir,char+EXTENSION) for font_dir in font_dir_list]
    return show_as_grid(img_path_list,C=C,label=True)



if __name__ == '__main__':
    axis = show_as_grid(['style.png','this.png',"gradient.png"]+['test.png','font.png']*2,label=True)
    axis.save('axis.png')
    root = r"D:\dataset\English_Gradient\train"
    font_dir_list = [os.path.join(root,font_dir) for font_dir in os.listdir(root)]
    axis  =show_char(font_dir_list,"A")
    axis.save('axis.png')

