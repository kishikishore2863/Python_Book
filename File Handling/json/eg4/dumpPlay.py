import json


dict1 = {
    'kishore':{
        'Quote':'why common sense is not so common ?'
    },
    'kishi':{
        'Quote':'dont be afraid to give up good to go for great!'
    },
    'steve':{
        'Quote':'stay hungry stay foolish'
    },
    'kane':{
        'Quote':'Always think outside the box'
    }
}

# with open("dump.json",'w')as file:
#     json.dump(dict1,file,indent=2)

with open("dump.json",'r') as reader:
    obj = json.load(reader)

for k,v in obj.items():
    print(k+",",end='')
    print(f" '{v['Quote']}'")