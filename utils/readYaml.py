import  yaml
class ReadYaml(object):
    """初始化文件"""
"""    #传参相对路径+文件名
    def  __int__(self,*file_name):
        self.file = file_name
"""
yamlList=[]
def read_oneYamlData(self,fileName):
    with open(fileName, 'r', encoding='utf-8') as f:
        yamlData = yaml.load(f.read(), Loader=yaml.FullLoader)
        return yamlData


def read_multiRowYamlData(self,fileName):
    with open(fileName, 'r', encoding='utf-8') as f:
        yamlData = yaml.load(f.read(), Loader=yaml.FullLoader)
        for i in yamlData:
            yamlList.append(i)
            return yamlList


