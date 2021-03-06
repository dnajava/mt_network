__author__ = "Ilpo Kantonen"
__date__ = "$20.1.2021 2:01:51$"
"""
Cluster network program. It makes nodes.csv and links.csv to Gephi. Gephi can display a network of mt-dna matches
in one haplogroup. The match clusters can be subgroups to that haplogroup. Grouping depends on GD values between
matches. You can also print MDKA:s as txt and xml file and a spreadsheet.

This is the main purpose to this program. You can do other things with this program too. Be free to modify code.
If you think you know better methods to do something, feel free to contact and tell to Ilpo at ilpo@iki.fi.

Input to this program are downloaded mt-dna match lists from FTDNA. Output are nodes.csv and links.csv. With Gephi
you can do beautiful graphs of GD network.

Version 0.2.1.
"""

from os import path
from kit import Kit
from cnetwork import Nclusters
from mtsettings import HAPLOGROUP
from mtsettings import OUTPUTDIR

def menu():
    command = '9'
    while command[0] != '0':
        print('1. Show GD network')
        print('2. Make nodes.csv and links.csv to Gephi?')
        print('3. Print clusters')
        print('4. Clusters to XML')
        print('5. Clusters to spreadsheet')
        print('6. Show MDKAs')
        print('0. Exit\n\n')
        command = input('Your choice:')

        if command[0] == '1':
            n.show()
        if command[0] == '2':
            n.gephi()
        if command[0] == '3':
            n.show()
        if command[0] == '4':
            n.mk_xml()
        if command[0] == '5':
            print('Not working yet')
        if command[0] == '6':
            n.show_mdkas()


if __name__ == '__main__':
    fname: str = HAPLOGROUP + '.json'
    n = Nclusters()

    if path.isfile(fname):
        print('There is already a network of haploroup', HAPLOGROUP, 'clusters. Reading.')
        n.read(fname)
    else:
        print('Reading', HAPLOGROUP, 'kits.')

        kits = []                                           # This is list of kits. First empty.
        kits_to_list = Kit.read_kits()                      # Read information of kits from kits.csv.

        for k in kits_to_list:
            new_kit = Kit(k[0], k[1], k[2], HAPLOGROUP)     # Create kit which have information and clustered matches.
            kits.append(new_kit)                            # Add to list.

        for k in kits:                                      # Add every kits every GD clusters to netclusters
            for z in k.gds:
                n.add(z)

        dint = 0
        while n.delete_duplicates():                        # First delete duplicates
            dint += 1
        if dint:
            print('Removed', dint, 'duplicate clusters.')

        sint = 0
        while n.split_clusters():                           # Then split non GD uniform clusters
            sint += 1
        if sint:
            print('Splitted', sint, ' clusters.')

    menu()
    n.write(OUTPUTDIR + HAPLOGROUP + '.json')

# n.mk_txt(1)                                       # Print one cluster (MDKAs)
# n.mk_xml()                                        # Print in XML form
# n.gephi()                                         # Write nodes.csv and links.csv to Gephi
