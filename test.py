from bardapi import Bard
import json
#Create your own .json file in same directory of code and and enter the token in the file.
with open('credentials.json', 'r') as f:
    file = json.load(f)
    token = file['token']

bard = Bard(token=token)
response = bard.get_answer("What is machine learning?")['content']
print(response)