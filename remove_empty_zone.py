import glob
import os
from lxml import etree

'''This script removes empty zone. Sometimes, ghost zones are created using eScriptorium. Those can be hard to find.
In that case, it might be good to use this script. Pay attention though that it will remove all empty zone and
most of the time, empty zones are just normal mistakes. The zones are actually visible.
We suggest to use this script while commenting out the removing part, in order to flag empty zones first.
Manually check if it is or not a ghost lines, correct the lines if possible and when you cannot do otherwise, use this script.'''

files_list = glob.glob(r"\\C:\Users\Christine\Documents\GitHub\Registre_foncier_de_Verbier\VTM_Depot_entrainement\VTM_Depot_entrainement\data\*.xml") #getting our list of XML files in our directory

for file in files_list:
    tree = etree.parse(file) #parsing tree
    root = tree.getroot() #getting root


    #Removing empty lines
    for t in root.iter('{*}TextBlock'):
        line = t.find('{*}TextLine')
        if line is None:
            print(file)
            #print('TextBlock with ID:',t.attrib['ID'], 'contains no TextLine')
            t.getparent().remove(t)
            print('TextBlock with ID:',t.attrib['ID'], 'has been removed')

    tree.write(file)
