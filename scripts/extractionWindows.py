import xml.etree.ElementTree as ET
import re
import os
import csv

#ouvre le fichier XML et l'analyse
def extract_content_from_tagrefs(file_path):
    # Load and parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Define the namespace
    ns = {'alto': 'http://www.loc.gov/standards/alto/ns-v4#'}

    # extract content for tagrefs that are in a text block
    def extract_content(tagref, text_block):
        lines = text_block.findall(f".//alto:TextLine[@TAGREFS='{tagref}']", ns)
        if not lines:
            return "-"

        concatenated_content = ' '.join(
            ' '.join(string.attrib.get('CONTENT', '') for string in line.findall("alto:String", ns))
            for line in lines
        )
        return re.sub(r'[|\[\]]', '', concatenated_content).strip()


    # extract the name of proprietaire
    def extract_proprietaire(tagref, text_block, ns):
        # Correct the XPath to search within the provided text_block
        lines = root.findall(f".//alto:TextBlock[@TAGREFS='{tagref}']/alto:TextLine[@TAGREFS='LT8']", ns)
        if not lines:
            return "-"

        # List to store the content from all strings
        concatenated_content = ' '.join(
            ' '.join(string.attrib.get('CONTENT', '') for string in line.findall("alto:String", ns))
            for line in lines
        )

        return re.sub(r'[|\[\]]', '', concatenated_content).strip()

    # extract cote from filename
    def extract_filename(filename):
        base_name = filename.split('_')
        base_name = base_name[slice(3)]
        extracted_cote = " ".join(base_name)
        print(base_name)
        return extracted_cote

    content_list = []
    for text_block in root.findall('.//alto:TextBlock', ns):
        # if there is no toponyme in the text block we don't need the info
        toponyme = extract_content('LT261', text_block)
        if toponyme == "-":
            continue
        proprietaire_content = extract_proprietaire('BT413', text_block, ns)
        parcelle = extract_content('LT268', text_block)
        terrain = extract_content('LT262', text_block)
        folio= extract_proprietaire('BT368', text_block, ns)
        cote= extract_filename(x)
	#ajoute les données à la liste content_list	
        content_list.append([
            proprietaire_content,
            toponyme,
            parcelle,
            terrain,
	       	folio,
            cote
        ])
    return content_list
    print(content_list)

path = r"/Users/Christine/Documents/MEMOIRE/Extraction_donnees"
dir_list = os.listdir(path)
with open('test.csv', 'w', newline='', encoding='utf-8') as csvfile:
    testwriter = csv.writer(csvfile, delimiter=',', quotechar=';', quoting=csv.QUOTE_ALL)
    for x in dir_list:
        file_path = "/Users/Christine/Documents/MEMOIRE/Extraction_donnees/" + x
        list_def = extract_content_from_tagrefs(file_path)

        for elem in list_def:
            print(elem)
            testwriter.writerow(elem)
