#字形图可视化
import os
from PIL import ImageFont
_ttf_path = os.path.join("charset",'SourceHanSans-Heavy Bold Font(Google apple free open-source font)-Simplified Chinese-Traditional Chinese.otf')
font=ImageFont.truetype(_ttf_path,size=24)
