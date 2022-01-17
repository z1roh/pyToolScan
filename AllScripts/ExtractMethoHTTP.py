#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests
import nmap
import optparse
import argparse

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


if __name__ == '__main__':

	print('''
 _____      _                  _  _____           _
| ____|_  _| |_ _ __ __ _  ___| ||_   _|__   ___ | |
|  _| \ \/ / __| '__/ _` |/ __| __|| |/ _ \ / _ \| |
| |___ >  <| |_| | | (_| | (__| |_ | | (_) | (_) | |
|_____/_/\_\\__|_|  \__,_|\___|\__||_|\___/ \___/|_|

Design: z1r0
	''')

	parser = argparse.ArgumentParser(description='Scanner para devolver los métodos HTTP soportados por una página web')

	parser.add_argument('-target', dest='target', help='target IP / domain', required=True)
	parser.add_argument('-ports', dest='ports', help='The target port(s) must go separated by comma[80,8080,443 by default]', default='80,8080,443')

	parsed_args = parser.parse_args()
	port_list = parsed_args.ports.split(',')

	ip = parsed_args.target

	for port in port_list:
		if port=='80' or port=='8080' or port=='443':
			req = requests.options('http://'+ip)
			if req.status_code == 200:
				for header,value in req.headers.items():
					if header == 'Allow':
						print('En el puerto ', port)
						print('---------------------')
						print('Encontramos', header, ' --> ', value)
					if header == 'Access-Control-Allow-Methods':
						print('Ademas encontramos', header, ' --> ', value, '\n')
			else:
				print('Error code %s' %req.status_code)
		else:
			ScanNmap().nmapScanner(ip, port)

