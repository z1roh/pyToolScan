#!/usr/bin/python3
#SimpleWebScraping

from bs4 import BeautifulSoup
import requests
import argparse

description='''
[+] Simple search:
	AllFromLinkPageWeb.py -t tudominiotarget.com
'''

parser = argparse.ArgumentParser(description='Simple Web Scraping, nos permite obtener los formularios y los enlaces de una Página Web', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t', dest='url', help='URL target', required=True)
params = parser.parse_args()

print('''
 ____                    __        _______           _
/ ___|  ___ _ __ __ _ _ _\ \      / /_   _|__   ___ | |
\___ \ / __| '__/ _` | '_ \ \ /\ / /  | |/ _ \ / _ \| |
 ___) | (__| | | (_| | |_) \ V  V /   | | (_) | (_) | |
|____/ \___|_|  \__,_| .__/ \_/\_/    |_|\___/ \___/|_|
                     |_|
Design: z1r0
''')

#Petición para identificar los elementos que contienen la información
#url = input('Introducir un sitio web:\n')
r = requests.get('http://'+ params.url)

#Definimos la Sopa
data = r.text
soup = BeautifulSoup(data,'lxml')

#Definimos un bucle para obtener los formularios de la Sopa
for link in soup.find_all('form'):
	print(link.get('href'))

#Definimos un otro bucle para obtener los enlaces de la Sopa
for link in soup.find_all('a'):
	print(link.get('href'))
