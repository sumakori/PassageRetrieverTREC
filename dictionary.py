import os
import glob

class Journals:
    def __init__(self):
        self.dictionary = []
        self.journals = ['ajepidem', 'ajpcell', 'ajpendometa', 'ajpgastro', 'ajpheart',
                        'ajplung', 'ajprenal', 'alcohol', 'andrology', 'annonc',
                        'bjanast', 'bjp', 'blood', 'carcinogenesis', 'cercor',
                        'development', 'diabetes', 'endocrinology', 'euroheartj',
                        'glycobiology', 'humanrep', 'humolgen', 'ijepidem', 'intimm',
                        'jantichemo', 'jappliedphysio', 'jbc-1995', 'jbc-1996', 'jbc-1997',
                        'jbc-1998', 'jbc-1999', 'jbc-2000', 'jbc-2001', 'jbc-2002',
                        'jbc-2003', 'jbc-2004', 'jbc-2005', 'jcb', 'jclinicalendometa',
                        'jcs', 'jexpbio', 'jexpmed', 'jgenphysio', 'jgenviro',
                        'jhistocyto', 'jnci', 'jneuro', 'mcp', 'microbio',
                        'molbiolevol', 'molendo', 'molhumanrep', 'nar', 'nephrodiatransp',
                        'peds', 'physiogenomics', 'rheumatolgy', 'rna', 'toxsci']

    def create_dictionary(self, journal):
        print ('Reading html file ' , journal)
        html_files = ''
        if os.path.exists(journal):
            html_files = glob.glob(journal + "/*.html")
            for file in html_files:
                journal, file = file.split('\\')
                list = [file, journal]
                self.dictionary.append(list)

    def store_dictionary(self):
        with open ('dictionary.csv' , 'w+') as file:
            header = 'html_file,location\r'
            file.write(header)
            for item in self.dictionary:
                value = item[0].replace('.html','') + ',' + item[1] + '\r'
                file.write(value)

    def display_dictionary(self):
        for item in self.dictionary:
            print(item)

    def run(self):
        #self.create_dictionary('blood')
        for item in self.journals:
            self.create_dictionary(item)
        self.store_dictionary()
        self.display_dictionary()

if __name__ == '__main__':
    app = Journals()
    app.run()
