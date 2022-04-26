# Tools Scanning

## Description

Proyecto básico de creación de herramientas de escaneo de redes con Python3. El proposito en este caso es comprender las diferentes librerías y tecnología en cuanto a
Python se refiere.

## Installation
La instalación requiere la siguiente secuencia de comandos:

```text
git clone https://github.com/Hans-E36/ToolScan.git
pip3 install -r requirements.txt
```
**Example Execution**
```text
python3 NmapShodanScan.py -h
```

## Scripts Description
### AllFormLinkPageWeb

Se encarga de imprimir todos los formularios y enlaces de una página web enviada por argumento al programa, con ella se trata de extraer contenido de una página web, mediante las librerías de Python BeautifulSoup y Scrapy que nos permite extracción de información.

Lo que conseguimos es obtener la información de una página web y procesar dicha información para extraer los datos de los formularios y los enlaces.

### WhoisDNSSearch
Nos permnite que en base a una dirección IP o un nombre de dominio, encontrar la información relacionada con el propietario de dicho dominio y sus registros DNS correspondinetes.

### NmapShodanScan
Nos permite realizar un simple escaneo a un objetivo y posteriormente consultar con shodan toda la información del mismo, en caso de que este tenga.

### ExtractMethodHTTP
En base a un escaneo con nmap, si se cuenta con los puertos relacionados con servidores web, se realziar una petición HTTP utilizando el método POST para conseguir determinar si se trata de un servidor web y extraer los métodos HTTP soportados.
