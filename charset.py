from utils import readfile,loadjson
import os
CHARSET_ROOT = "charset"
GB2312= readfile(os.path.join(CHARSET_ROOT,"GB2312_CN6763.txt"))
KSX1001=readfile(os.path.join(CHARSET_ROOT,"KSX1001.txt"))
常用國字=readfile(os.path.join(CHARSET_ROOT,"常用國字.txt"))
次常用國字=readfile(os.path.join(CHARSET_ROOT,"次常用國字.txt"))
CJK = loadjson(os.path.join(CHARSET_ROOT,"cjk.json"))





