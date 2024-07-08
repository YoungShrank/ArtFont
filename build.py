import os
from ttfutils import render,supported_chars,load_font
import random
from charset import CJK
def build_font(ttf_path:str,des_root:str,font_name =None,in_chars:set[str] = set(),ex_chars:set[str] = set(),char_lib:set[str] = None,num:int = 200,ext:str = '.png'):
    """
    依靠字体ttf,渲染该字体的一个font图像数据目录
    - ttf_path: 字体路径
    - des_root: 根目录，des_root/font_name/png
    - font_name: 字体名称，默认为ttf文件名去掉后缀
    - in_chars: 希望包含的字符,默认为空
    - ex_chars: 需要排除的字符(比如繁体字)，默认为空
    - char_lib: 字符库，默认为所有支持字符
    - num: 希望包含的字符总数，默认200
    - ext: 保存图片格式，默认png
    # returns
    - font_name: 字体名称
    - deficit: 缺失的字符数(inchar_deficit,num_deficit)
    """
    #path
    if font_name is None:
        font_name = os.path.splitext(os.path.basename(ttf_path))[0]
    des_dir = os.path.join(des_root,font_name)
    if not os.path.exists(des_dir):
        os.makedirs(des_dir)
    #load
    deficit = (len(in_chars),num)
    try :
        font = load_font(ttf_path)
    except :
        print(f"{ttf_path} is not a valid font file")
        return deficit
    if char_lib is None:
        char_lib = supported_chars(ttf_path)
    # char
    char_lib = set(char_lib) - set(ex_chars)
    avail_in = set(in_chars) & char_lib
    char_lib_left = char_lib - avail_in
    extra_num = num - len(avail_in)
    if extra_num <=0 :
        extra = set()
    elif extra_num < len(char_lib_left) :
        extra = set(random.sample(list(char_lib_left),extra_num))
    else :
        extra = char_lib_left
    deficit = (len(in_chars) - len(avail_in)),max(num - len(avail_in) - len(extra),0)
    # render
    for char in avail_in | extra :
        if char not in char_lib :
            continue
        img_path = os.path.join(des_dir,char+ext)
        img = render(font,char)
        img.save(img_path)
    return font_name,deficit

if __name__ == '__main__' :
    font_dir = 'ttfdemo/SourceHanSans-Heavy Bold Font(Google apple free open-source font)-Simplified Chinese-Traditional Chinese.otf'
    des_dir = 'root'
    font_name,defict = build_font(font_dir,des_dir,font_name="font1",in_chars="逃避行",char_lib=CJK["jp"],num=4)
    print(defict)
    
    

    
    


    