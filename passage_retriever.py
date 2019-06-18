import csv
import os
from bs4 import BeautifulSoup

class PassageReteiver:
    def __init__(self, csv, path):
        self.fieldnames = ['TOPIC', 'PMID', 'OFFSET', 'LENGTH']
        self.list = []
        self.csv = csv
        self.path = path

    def retrive(self, topic, pmid, offset, length):
        print('Retriveing pmid. Wait')
        for dirpath, dirnames, files in os.walk(self.path):
            #print (dirnames, dirpath)
            #print ('pmid %s' % pmid)
            #print (files)
            if pmid in files:
                print(os.path.join(dirpath, pmid))
                print(40 * '*')
                print('Reading %s in path %s with offset %s & length %s' % (pmid, os.path.join(dirpath), offset, length))
                print(40 * '*')
                with open(os.path.join(dirpath, pmid), 'r') as file:
                    #text = ''.join(BeautifulSoup(file, "html.parser").findAll(text=True))
                    text = file.read()
                    print(text[offset:offset+length])
                print(40 * '*')
        
    def read_csv(self):    
        with open(self.csv) as csvfile:
            csvreader = csv.DictReader(csvfile, fieldnames=self.fieldnames, delimiter=',')

            print('Fetching RelevanceDataset. Wait')
            # Skip first line
            row = next(csvreader)
            count = 0
            for row in csvreader:
                if count < 100:
                    topic = row['TOPIC']
                    pmid = row['PMID']
                    offset = row['OFFSET']
                    length = row['LENGTH']
                    #print ('%s,%s,%s,%s' % (topic, pmid, offset, length))
                    list = [topic, pmid, offset, length]
                    self.list.append(list)
                    count += 1
            print('Fetched RelevanceDataset')

    def     run(self):
        self.read_csv()
        #print (len(self.list))
        for item in self.list:
            self.retrive(item[0], (item[1] + '.html'), int(item[2]), int(item[3]))

if __name__ == '__main__':
    app = PassageReteiver('RelevanceDataset.csv', '.')
    app.run()
