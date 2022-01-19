import json

with open("annotations/instances_val2017.json", 'r') as load_f:
    f = json.load(load_f)
p= f["images"] 
count1=0
count2=0

f['annotations'] = list(filter(lambda x:x['bbox'][2]*x['bbox'][3]<=4096,f['annotations']))


im_set = set([int(x["image_id"]) for x in f['annotations']])

def is_ok(x):
    if int(x["id"]) in im_set:
        global count1
        count1 += 1
        return True
    else:
        global count2
        count2 += 1
        return False
f["images"] = list(filter(is_ok,f['images']))
print("count1:{}".format(count1))
print("count2:{}".format(count2))
#f["images"] = list(filter(lambda x:int(x["id"] in im_set),f['images']))
with open("annotations/val.json", "w", encoding='utf-8') as f1:
    f1.write(json.dumps(f))

#count1:3052
#count2:1948
