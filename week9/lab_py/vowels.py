import csv
import json

def frequency(c, string):
    return string.lower().count(c)

def frequencies(string):
    data = {}
    for c in "aeiou":
        data[c] = frequency(c,string)
    return data
    
def save_to_txt(structure):
    handler = open('data.txt','w')
    for data in structure:
        for key in data.keys():
            handler.write(f'{key} --> {data[key]}')
            handler.write("\n")
    handler.close()

def read_from_txt(file):
    handler = open(file,'r')
    structure = handler.read()
    print(structure)
    
def save_to_csv(structure):
    with open('data.csv','w',newline='') as handler:
        writer = csv.writer(handler)
        for data in structure:
            for key in data.keys():
                writer.writerow([key,data[key]])
    handler.close()

def read_from_csv(file):
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

def save_to_json(structure):
    with open('data.json','w') as handler:
        json.dump(structure,handler,indent=2)
    handler.close()
        
def read_from_json(file):
    handler = open(file,'r')
    json_obj = json.load(handler)
    print(json.dumps(json_obj,indent=4))
    handler.close()
    
def run():
    structure = []
    s = input("String: ")
    while s != "*":
        structure.append(frequencies(s)) # list of dictionaries
        save_to_txt(structure)        
        save_to_csv(structure)        
        save_to_json(structure)
        s = input("String: ")
        
    read_from_txt('data.txt')
    read_from_csv('data.csv')
    read_from_json('data.json')
run()