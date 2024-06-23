#对象序列化|文件读写
import json
import yaml

def loadjson(path):
    """读json
    - path :文件地址
    """
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)
def savejson(path,obj):
    """保存json
    - path :文件地址
    - obj :保存的python对象
    """
    with open(path,"w",encoding="utf-8") as f:
        json.dump(obj,f,indent=4,ensure_ascii=False)
def loadyml(path):
    """读yml
    - path :文件地址
    """
    with open(path,"r",encoding="utf-8") as f:
        obj=yaml.load(f, Loader=yaml.FullLoader)
        return obj
def getvalues(dic:dict,keys:str):
    """
    获得keys对应的值
    - dic :字典
    - keys 空格分开的若干键名
    """
    return [dic.get(key) for key in keys.split()]
def readfile(path):
    """
    读文件
    - path :文件地址
    """
    with open(path,"r",encoding="utf-8") as f:
        return f.read()
def writefile(path,txt):
    """
    写文件
    - path :文件地址
    """
    with open(path,"w",encoding="utf-8") as f:
        f.write(txt)
    


if __name__ == '__main__':
    pass