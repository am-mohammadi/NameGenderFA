# NameGenderFA
Detecting the gender of Persian names with automatic cleaning of input

__________________________________________________
Example:

from NameGenderFA import NameGenderFA

gd=NameGenderFA.Gender_detector()

name='علی123! عزیزی'

gender, cleaned_name=gd.detect(name)
__________________________________________________
output:
('male', 'علی')
__________________________________________________
gender: male/female/None

cleaned_name: cleaned name

Gender_detector.perfixes: removes some perfixes like "سید", you can set it manually

Gender_detector.replace_chars: replace some characters like 'ي' to 'ی' or 'السادات' to ''

also punctuations and numbers will be remove.
