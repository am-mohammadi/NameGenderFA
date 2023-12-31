import pandas as pd
import re
from string import punctuation

'''
Dataset source:
https://github.com/peymanslh/persian-gender-detection
'''


class Gender_detector:
    def __init__(self):
        # self.names=pd.read_excel('names.xlsx')
        print('Loading data...')
        self.names=pd.read_excel('https://raw.githubusercontent.com/am-mohammadi/NameGenderFA/main/NameGenderFA/src/NameGenderFA/names.xlsx')
        print('Data loaded.')
        self.perfixes=[
            'سیده',
            'سید'
            ]
        
        self.replace_chars=[
            {'old': 'ي', 'new': 'ی'},
            {'old': 'ک', 'new': 'ک'},
            {'old': 'السادات', 'new': ''},
            {'old': 'سادات', 'new': ''},
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
        for row in self.replace_chars:
           name=name.replace(row['old'], row['new'])
        
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
        
