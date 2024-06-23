from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
def render(font:ImageFont,char:str,shape=(128,128),padding = 16):
    """
    根据字体渲染字符字形图
    - font: 字体
    - char: 字符
    - shape: 输出大小
    - padding: 留白
    # returns
    - image: 字形图
    """
    l,t,r,b = font.getbbox(char,anchor="lt")
    max_size = max(r-l, b-t)+padding*2
    image = Image.new("RGB",(max_size,max_size),color=(255,255,255))
    draw = ImageDraw.Draw(image)
    draw.text((padding,padding),char,font=font,anchor="lt",fill=(0,0,0))
    image = image.resize(shape)
    return image

def supported_chars(ttf_path,encodings=((3,10),(3,1))):
    """判断一个字体文件支持的所有字符
    - ttf_path : font地址
    - encodings (platformId,encodingID)的列表，表示支持的平台/编码(差不多这个意思)
    # warning
    并不总是管用的，还是可能包含不支持的字符，所以后面要注意
    """
    ttf =TTFont(ttf_path)#根据地址获得对象
    chars=set()
    for subtable in ttf["cmap"].tables:#subtable
        table_encoding=subtable.platformID, subtable.platEncID
        for encoding in encodings:
            if subtable.platformID in [0,1,2,3] or encoding==table_encoding:#表和平台一致
                cmap_encoding = subtable.getEncoding()#获得subtable的编码
                # Cmap isn't supported
                if cmap_encoding is None:
                    continue
                else: 
                    for byt in subtable.cmap:#code 到char的映射
                        try :
                            ch=int(byt).to_bytes(length=2,byteorder='big', signed=False).decode(cmap_encoding)
                            if len(ch)<2: chars.add(ch)
                        except :
                            print(byt)
                            continue
    return chars



if __name__ == "__main__":
    import os
    ttf_path  = os.path.join("ttfdemo","SourceHanSans-Heavy Bold Font(Google apple free open-source font)-Simplified Chinese-Traditional Chinese.otf")
    chars = " ".join(supported_chars(ttf_path))
    #print(chars)
