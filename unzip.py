from zipfile import ZipFile

#zip_files = ['ajepidem.zip', 'ajpcell.zip', 'ajpendometa.zip', 'ajpheart.zip', 'ajplung.zip']
zip_files = ['ajepidem.zip', 'ajpcell.zip', 'ajpendometa.zip', 'ajpgastro.zip', 'ajpheart.zip',
            'ajplung.zip', 'ajprenal.zip', 'alcohol.zip', 'andrology.zip', 'annonc.zip',
            'bjanast.zip', 'bjp.zip', 'blood.zip', 'carcinogenesis.zip', 'cercor.zip',
            'development.zip', 'diabetes.zip', 'endocrinology.zip', 'euroheartj.zip',
            'glycobiology.zip', 'humanrep.zip', 'humolgen.zip', 'ijepidem.zip', 'intimm.zip',
            'jantichemo.zip', 'jappliedphysio.zip', 'jbc-1995.zip', 'jbc-1996.zip', 'jbc-1997.zip',
            'jbc-1998.zip', 'jbc-1999.zip', 'jbc-2000.zip', 'jbc-2001.zip', 'jbc-2002.zip',
            'jbc-2003.zip', 'jbc-2004.zip', 'jbc-2005.zip', 'jcb.zip', 'jclinicalendometa.zip',
            'jcs.zip', 'jexpbio.zip', 'jexpmed.zip', 'jgenphysio.zip', 'jgenviro.zip',
            'jhistocyto.zip', 'jnci.zip', 'jneuro.zip', 'mcp.zip', 'microbio.zip',
            'molbiolevol.zip', 'molendo.zip', 'molhumanrep.zip', 'nar.zip', 'nephrodiatransp.zip',
            'peds.zip', 'physiogenomics.zip', 'rheumatolgy.zip', 'rna.zip', 'toxsci.zip']

for item in zip_files:
    with ZipFile(item, 'r') as zipObj:
        print('Please wait. Extracting %s' % zipObj)
        # Extract all the contents of zip file in current directory
        zipObj.extractall()