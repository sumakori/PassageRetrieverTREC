import csv
import operator
import pandas as pd

class SortDataset():
    def __init__(self, dataset, datasetSorted):
        self.dataset = open(dataset,'r')
        self.csvfile = csv.reader(self.dataset,delimiter=',')
        self.datasetSorted = datasetSorted
        self.dictionary = 'dictionary.csv'

    def sort(self):
        self.sort_csv = sorted(self.csvfile, key=operator.itemgetter(1))
        self.sort_csvnoheader = self.sort_csv[:-1]

    def create_dataset(self, file):
        print('Start sorting')
        self.sort()
        header = self.sort_csv[-1]
        print('Stop sorting')
        print(header)
        print('Start writing')

        with open(self.datasetSorted, 'w', newline='') as csvfile:
            fieldnames = ['TOPIC','PMID','OFFSET','LENGTH','SPANID','RELEVANCE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()
            # Write individual row using dictionary
            for item in self.sort_csvnoheader:
                dictionary = dict(zip(fieldnames, item))
                writer.writerow(dictionary)
    
    def add_count(self):
        df_Sorted = pd.read_csv(self.datasetSorted)
        df_Dictionary = pd.read_csv(self.dictionary)

        column_location = []
        # Create a new column which includes count of PMID instance
        total_PMID = df_Sorted['PMID'].value_counts().rename('Total_PMID')
        df_Sorted = df_Sorted.join(total_PMID, on='PMID')

        frame_PMID = df_Sorted['PMID']
        # Use set_index to prepare dictionary with html and location
        dictionary = df_Dictionary.set_index('html_file')['location'].to_dict()

        for item in frame_PMID:
            if int(item) in dictionary:
                column_location.append(dictionary[item])

        # Drop spanid and relevance
        df_Sorted = df_Sorted.drop(columns=['SPANID'])
        df_Sorted = df_Sorted.drop(columns=['RELEVANCE'])
        df_Sorted['Location'] = column_location
        #
        # Do not write index to csv file
        df_Sorted.to_csv(self.datasetSorted, index=False)
        print (df_Sorted)

    # Make a list of PMIDs with no duplicates
    def pmids(self):
        df = pd.read_csv(self.datasetSorted)
        #df = df.drop_duplicates()
        list = df.PMID.unique()

    def run(self):
        self.create_dataset(self.datasetSorted)
        self.add_count()
        #self.pmids()

if __name__ == '__main__':
    app = SortDataset('RelevanceDataset.csv','RelevanceDataset_sorted.csv')
    app.run()