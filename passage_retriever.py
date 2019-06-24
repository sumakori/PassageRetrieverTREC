import csv
import os
import argparse

class PassageReteiver:
    def __init__(self, csv, path):
        self.fieldnames = ['TOPIC', 'PMID', 'OFFSET', 'LENGTH', 'Total_PMID', 'Location']
        self.list = []
        self.csv = csv
        self.path = path

    def retrive(self, topic, pmid, offset, length, total_pmid, location):
        html_file = self.path + '\\' + location + '\\' + pmid
        if os.path.exists(html_file):
            print('Retrieving data from %s with length %s offset %s' % (html_file, length, offset))
            print(len('Retrieving data from ' + html_file + ' with length ' + str(length) +
                      ' offset ' + str(offset)) * '*')
            
            with open(html_file) as string:
                print (string.seek(offset))
                while string.tell() < offset+length:
                    print (string.readline(),end='')
            #print(string.seek([offset:length+offset]))
            #print(len(string))

        else:
            print('File does not exist %s' % (html_file))
        
    def read_csv(self):    
        with open(self.csv) as csvfile:
            csvreader = csv.DictReader(csvfile, fieldnames=self.fieldnames, delimiter=',')

            print('Fetching RelevanceDataset. Wait')
            # Skip first line
            row = next(csvreader)
            count = 0
            for row in csvreader:
                if count < 2:
                    topic = row['TOPIC']
                    pmid = row['PMID']
                    offset = row['OFFSET']
                    length = row['LENGTH']
                    total_pmid = row['Total_PMID']
                    location = row['Location']
                    list = [topic, pmid, offset, length, total_pmid, location]
                    self.list.append(list)
                    count += 1

    def run(self):
        self.read_csv()
        for item in self.list:
            self.retrive(item[0], (item[1] + '.html'), int(item[2]), int(item[3]), item[4], item[5])

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", help="A valid dataset")
parser.add_argument("-p", "--path", help="A valid location to journal")
ARGS = parser.parse_args()

if __name__ == '__main__':
    app = PassageReteiver(ARGS.dataset, ARGS.path)
    app.run()
