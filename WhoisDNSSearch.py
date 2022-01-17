#!/usr/bin/python3

#Importamos librerias
import pythonwhois
import dns
import dns.resolver
import dns.reversename
import pprint
import argparse

description='''
[*] Simple search:
	python3 WhoisDNSSearch.py -t <domain/ip>
'''

parser = argparse.ArgumentParser(description='Simple recopilador Whois & registros DNS', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t',dest='url',help='URL target', required=True)
params = parser.parse_args()


#Definimos el domino o ip
#url = input('Introduzca una Ip o un nombre de Dominio:\n')
dominio = input('Es un nombre de dominio? y/n: ')

if dominio == 'y':
	url = params.url
else:
	#Soporte dns inverso
	url = dns.reversename.from_address(str(params.url))

def WhoisQuery():
	#Servidor raiz
	whois_rootServer = pythonwhois.net.get_root_server(url)
	if whois_rootServer == whois_rootServer:
		#Recuperar el servidor raiz
		print('El servidor raiz de ' + str(url) + ' es: ' + pythonwhois.net.get_root_server(url))
	else:
		print('No tiene Servidor raiz')

	#Recuperar un diccionario con toda la información
	whois = pythonwhois.get_whois(url)
	print('[*] Realizando petición whois..')
	Flow = input('Deseas obtener toda la información del Dominio? y/n: ')
	if Flow == 'y':
		whoisFull = pythonwhois.net.get_whois_raw(url)
		pprint.pprint(whoisFull)
	else:
		#Se obtiene las llaves del diccionario solicitado
		print('')
		for key in whois.keys():
			print(key)
		keys = input('\nSelecciona una etiqueta de la información que deseas:\n')
		print('')
		print(whois[keys])
		return

def DNSquery():
	#Forma básica de definir las variables
	ansA = dns.resolver.resolve(url,'A')
	ansMX = dns.resolver.resolve(url,'MX')
	ansAAAA = dns.resolver.resolve(url,'AAAA')
	ansNS = dns.resolver.resolve(url,'NS')


	#Imprimimos las variables definidas
	print('')
	print('\nCONSULTAS DNS')
	print('--------------------------------------------')
	print('--------------------------------------------')
	print('\nDirecciones IPv4')
	print('--------------------------------------------')
	print(ansA.response.to_text())
	print('\nServidores de Correo')
	print('--------------------------------------------')
	print(ansMX.response.to_text())
	print('\nServidores de Nombre')
	print('--------------------------------------------')
	print(ansNS.response.to_text())
	print('\nDirecciones IPv6')
	print('--------------------------------------------')
	print(ansAAAA.response.to_text())

if __name__ == '__main__':

	print('''
 _        ___           _     ____  _   _ ____
\ \      / / |__   ___ (_)___|  _ \| \ | / ___|
 \ \ /\ / /| '_ \ / _ \| / __| | | |  \| \___ \

  \ V  V / | | | | (_) | \__ \ |_| | |\  |___) |
   \_/\_/  |_| |_|\___/|_|___/____/|_| \_|____/

Design: z1r0
	''')

	WhoisQuery()
	DNSquery()

