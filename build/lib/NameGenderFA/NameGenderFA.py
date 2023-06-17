import pandas as pd
import re
from string import punctuation

'''
Dataset source:
https://github.com/peymanslh/persian-gender-detection
'''


class Gender_detector:
    def __init__(self):
        self.names=pd.read_excel('names.xlsx')
        self.perfixes=[
            'سیده',
            'سید'
            ]

    def detect(self, raw_name):
        raw_name=raw_name.strip()
        raw_name=self.replace_per(raw_name)
        raw_name=self.remove_perfix(raw_name)
        names=raw_name.split(' ')
        name=names[0]
        name=name.strip()
        name = re.sub(f'[{punctuation}؟،٪×÷»«]+', '', name)
        name=''.join([i for i in name if not i.isdigit()])
      
        
        
        gender=self.names[self.names.name==name].gender.to_list()
        if len(gender)==0:
            return None, name
        else:
            return gender[0], name
        
    def replace_per(self, name):
        old='ي'
        new='ی'
        name=name.replace(old, new)
        
        old='ک'
        new='ک'
        name=name.replace(old, new)
        
        old='السادات'
        new=''
        name=name.replace(old, new)
        
        old='سادات'
        new=''
        name=name.replace(old, new)
        
        
        return name
    
    def remove_perfix(self, name):
        for perfix in self.perfixes:
            name_splitted=name.split(perfix)
            if len(name_splitted)>1:
                name=name_splitted[1]
            else:
                name=name_splitted[0]
            
        return name.strip()
        
if __name__=='__main__':
    gd=Gender_detector()
    gender, cleaned_name=gd.detect('علی123!')
        
