# 纹彩图生成
# 用黑白图和纹彩图合成艺术字

from PIL import Image
import numpy as np
C = 3
#保存array为图像
def save_image(array:np.ndarray, path:str):
    """
    保存array为图像
    - array: [C, H, W]
    - path: 保存路径
    """
    array = array.astype(np.uint8)
    im = Image.fromarray(array)
    im.save(path)
#加载图像为array
def load_image(path:str,shape=(128,128)):
    """
    加载图像为array
    - path: 图像路径
    - shape: 图像大小
    # returns
    [C, H, W]
    """
    im = Image.open(path).convert("RGB")
    im = im.resize(shape)
    arr = np.array(im) # H,W,C
    return arr

def gradient_fcolor(W,H,direct=(0.5,0.5)):
    """
    渐变色颜色函数,(W,H)->RGB
    - w: 宽索引
    - h: 高索引
    - direct: 渐变方向
    # returns
    RGB [0:255]^3
    """
    colors = np.random.randint(0, 255, size=(2,1,3))
    s,t = colors[0],colors[1]
    imagew,imageh = np.linspace(s,t,W),np.linspace(s,t,H)
    def fcolor(w,h):
        return np.squeeze((imagew[w]*direct[0]+imageh[h]*direct[1]))
    return fcolor

#生成纯色图
def generate_pure_image(shape=(128,128)):
    """
    生成纯色图
    - shape: 图像大小
    # returns
    [C, H, W]
    """
    color = np.random.randint(0, 255, size=(1,1,3))
    pure = np.ones((*shape,C), dtype=np.uint8)*color
    return pure
#生成渐变色图
def generate_gradient_image(fcolor,shape=(128,128)):
    """
    生成渐变色图
    - shape: 图像大小
    - fcolor: 颜色函数
    # returns
    [C, H, W]
    """
    W,H = shape
    X,Y = np.meshgrid(np.arange(W),np.arange(H))
    gradient = fcolor(X,Y)
    return gradient
def generate_style_image(font_glyph:np.ndarray,color_image:np.ndarray):
    """
    生成风格图
    - font_glphy: 黑白字形图
    - color_image: 纹彩图
    # returns
    风格字符图像
    """
    back = font_glyph.astype(np.float32)/255.
    fore = 1-back
    style_image = fore*color_image+back*255
    return style_image

if __name__ == '__main__':
    path = r"D:\dataset\texture3\baidu_15.png"
    
    font_path = r"D:\毕设\resource\fsfont_data\train\Adorkable boyhood Font-Simplified Chinese\嘓.png"
    
    font_glyph = load_image(font_path)
    color_image = load_image(path)
    print(font_glyph.shape)
    style_image = generate_style_image(font_glyph,color_image)
    save_image(style_image,r"style.png")