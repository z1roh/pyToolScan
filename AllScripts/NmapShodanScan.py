#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import optparse
import argparse
import nmap
import sys
import shodan

description =""" Ejemplo de uso:
		[+] Escaneo básico
			python3 NmapShodanScan.py -target 127.0.0.1 -key <api_key>

		[+] Escaneo indicando un puerto
			python3 NmapShodanScan.py -target 127.0.0.1 -port 21 -key <api_key>

		[+] Escaneo con varios puertos:
			python3 NmapShodanScan.py -target 127.0.0.1 -port 21,22,23 -key <api_key>

		[*] Por defecto nmap realiza el scaneo con los siguientes parámetros:
			nmap -oX -p <ports> -sV <ip> """

class ScanNmap:

	def __init__(self):
		self.scanner = nmap.PortScanner()

	def nmapScanner(self, host, port):
		try:
			print('checking port ' + port + ' .....')
			self.scanner.scan(host, port)

			print('[*] Executing command: %s' % self.scanner.command_line())
			self.state = self.scanner[host]['tcp'][int(port)]['state']
			print('[*] ' + host + 'tcp/' + port + ' ' + self.state)

		except Exception as e:
			print('Error to connect with ' + host + ' for port scanning')
			pass

def ScanShodan():
        try:
				#Insertamos la contraseña
                ShodanKeyString =  key

                ShodanApi = shodan.Shodan(ShodanKeyString)
                results = ShodanApi.host(str(ip))
                for result in results:
                        print('%s : %s' %(result, results[result]))
        except shodan.APIError as e:
                print('Error: %s' % e)

if __name__ == '__main__':

	print('''
 ____                  _   _ ____  _____      _ _
/ ___|  ___ __ _ _ __ | \ | / ___||  ___|   _| | |
\___ \ / __/ _` | '_ \|  \| \___ \| |_ | | | | | |
 ___) | (_| (_| | | | | |\  |___) |  _|| |_| | | |
|____/ \___\__,_|_| |_|_| \_|____/|_|   \__,_|_|_|

Design: z1r0
	''')

	parser = argparse.ArgumentParser(description='Scanner de Nmap que ejecuta un escaneo de nmap contra un objetivo y posteriormente lanza un escaneo en Shodan para obtener más información.', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)

	parser.add_argument('-target', dest='target', help='target IP / domain', required=True)
	parser.add_argument('-ports', dest='ports', help='The target port(s) must go separated by comma[80,8080,443 by default]', default='80,8080,443')
	parser.add_argument('-key', dest='key', help="Set the Key'shodan", required=True)

	parsed_args = parser.parse_args()
	port_list = parsed_args.ports.split(',')

	ip = parsed_args.target
	key = parsed_args.key

	for port in port_list:
		ScanNmap().nmapScanner(ip, port)

	ScanShodan()
