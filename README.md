# TOOLS BUT SCANNING
Herramientas básicas de escaneo con Python3.

## Installation
Su instalación es muy sencilla, lo único que requiere es:
#### Descargar el Repositorio
```sh
> git clone https://github.com/Hans-E36/ToolScan.git
```
#### Instalar las dependencias
```sh
> pip3 install -r requirements.txt
```
#### Ejecutar la Herramienta
```sh
> python3 NmapShodanScan.py -h
```
## Scripts
### AllFormLinkPageWeb
<p>
  Se encarga de imprimir todos los formularios y enlaces de una página web enviada por argumento al programa,
  con ella se trata de extraer contenido de una página web, mediante las librerías de Python BeautifulSoup y Scrapy que nos permite extracción de información.
</p>
<p>
  Lo que conseguimos es obtener la información de una página web y procesar dicha información para extraer los datos de los formularios y los enlaces.
</p>

### WhoisDNSSearch
<p>
  Nos permnite que en base a una dirección IP o un nombre de dominio, encontrar la información relacionada con el propietario de dicho dominio y sus registros DNS correspondinetes.
</p>

### NmapShodanScan
<p>
  Nos permite realizar un simple escaneo a un objetivo y posteriormente consultar con shodan toda la información del mismo, en caso de que este tenga.
</p>

### ExtractMethodHTTP
<p>
  En base a un escaneo con nmap, si se cuenta con los puertos relacionados con servidores web, se realziar una petición HTTP utilizando el método POST para conseguir determinar si se trata de un servidor web y extraer los métodos HTTP soportados.

