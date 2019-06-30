import csv
import os
import argparse

class PassageReteiver:
    def __init__(self, csv, path):
        self.fieldnames = ['TOPIC', 'PMID', 'OFFSET', 'LENGTH', 'Total_PMID', 'Location']
        self.fieldnames_para = ['TOPIC', 'PMID', 'OFFSET', 'LENGTH', 'Total_PMID', 'Paragraph']
        self.list = []
        self.csv = csv
        self.path = path
        self.paragraphs = []
        self.csv_paragraph = ' RelevanceDataset_paragraphs.csv'

    def retrive(self, topic, pmid, offset, length, total_pmid, location):
        html_file = self.path + '\\' + location + '\\' + pmid
        if os.path.exists(html_file):
            print('Retrieving data from %s with length %s offset %s' % (html_file, length, offset))
            print(len('Retrieving data from ' + html_file + ' with length ' + str(length) +
                      ' offset ' + str(offset)) * '*')
            
            paragraph = ''
            with open(html_file) as string:
                print (string.seek(offset))
                while string.tell() < offset+length:
                    paragraph += (string.readline())
                    #print (string.readline(),end='')
                print(paragraph)
            list = [topic, pmid.replace('.html',''), offset, length, total_pmid,
                    paragraph.replace('\"','')]
            self.paragraphs.append(list)
        else:
            print('File does not exist %s' % (html_file))

    def write_retrieved_paragraphs(self, list):
        with open(self.csv_paragraph, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames_para, delimiter = ',',
                                    escapechar=' ', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for item in list:
                #paragraph = item[5].replace('\"','')
                #print (pmid)
                #print (paragraph)
                #paragraph = paragraph.strip()
                writer.writerow({'TOPIC': item[0], 'PMID': item[1].replace('.html', ''),
                                'OFFSET' : item[2], 'LENGTH': item[3],
                                'Total_PMID': item[4], 'Paragraph': item[5]})
    

    def read_csv(self):    
        with open(self.csv) as csvfile:
            csvreader = csv.DictReader(csvfile, fieldnames=self.fieldnames, delimiter=',')

            print('Fetching RelevanceDataset. Wait')
            # Skip first line
            row = next(csvreader)
            count = 0
            for row in csvreader:
                #if count < 5:
                topic = row['TOPIC']
                
                pmid = row['PMID']
                offset = row['OFFSET']
                length = row['LENGTH']
                total_pmid = row['Total_PMID']
                location = row['Location']
                list = [topic, pmid, offset, length, total_pmid, location]
                self.list.append(list)
                    #count += 1

    def run(self):
        self.read_csv()
        for item in self.list:
            self.retrive(item[0], (item[1] + '.html'), int(item[2]), int(item[3]), item[4], item[5])
        print ('len of lists %s paragraphs %s' % (len(self.list), len(self.paragraphs)))
        self.write_retrieved_paragraphs(self.paragraphs)
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", help="A valid dataset")
parser.add_argument("-p", "--path", help="A valid location to journal")
ARGS = parser.parse_args()

if __name__ == '__main__':
    app = PassageReteiver(ARGS.dataset, ARGS.path)
    app.run()
