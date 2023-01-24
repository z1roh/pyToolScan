# Tools Scanning

## Description

Proyecto básico de creación de herramientas de escaneo de redes con Python3. El proposito en este caso es comprender las diferentes librerías y tecnología en cuanto a
Python se refiere.

## Installation
La instalación requiere la siguiente secuencia de comandos:

```sh
git clone https://github.com/Hans-E36/ToolScan.git
pip3 install -r requirements.txt
```
**Example Execution**
```python3
./NmapShodanScan.py -h
```

## Scripts Description
### AllFormLinkPageWeb

Se encarga de imprimir todos los formularios y enlaces de una página web enviada por argumento al programa, con ella se trata de extraer contenido de una página web, mediante las librerías de Python BeautifulSoup y Scrapy que nos permite extracción de información.

Lo que conseguimos es obtener la información de una página web y procesar dicha información para extraer los datos de los formularios y los enlaces.

##### Banner de Ayuda de la herramienta
<img width="1397" alt="image" src="https://user-images.githubusercontent.com/72032027/214210396-3e2c1d32-193f-43f9-a48a-6f9064cbdaef.png">

Usando el parámetro '-t' podemos introducir el dominio objetivo del que deseamos obtener los formularios y los enlaces.

#### Primer Despliegue de la herramienta
<img width="1398" alt="image" src="https://user-images.githubusercontent.com/72032027/214210740-e3e1d78f-77d6-462a-8ff0-6bb265d81df4.png">

#### La simple ejecución del script ejecuta las acciones pertinentes
```sh
./AllFormLinkPageWeb.py
```
----
### WhoisDNSSearch
Nos permnite que en base a una dirección IP o un nombre de dominio, encontrar la información relacionada con el propietario de dicho dominio y sus registros DNS correspondinetes.

##### Banner de Ayuda de la herramienta
<img width="834" alt="image" src="https://user-images.githubusercontent.com/72032027/214211133-d73cc873-3d31-485e-bd75-f578fa48af79.png">

#### Porción de una simple búsqueda
<img width="1009" alt="image" src="https://user-images.githubusercontent.com/72032027/214211223-45b1b852-8c51-4c82-84d4-69f86b1214f7.png">

#### Simple arrgelo de la salida de las consultas DNS
<img width="693" alt="image" src="https://user-images.githubusercontent.com/72032027/214211285-986bd96a-089e-4188-b7d3-6d338d456a93.png">

No es la mejor opción, pero de momento es actualmente la implementada en el script y es funcional.

#### Ejemplo de visualización
<img width="719" alt="image" src="https://user-images.githubusercontent.com/72032027/214211450-7ce43167-1369-417b-a627-300d9a092a8c.png">

----
### NmapShodanScan
Nos permite realizar un simple escaneo a un objetivo y posteriormente consultar con shodan toda la información del mismo, en caso de que este tenga.

#### Banner de ayuda de NmapShodanScan.py
<img width="1399" alt="image" src="https://user-images.githubusercontent.com/72032027/214211744-b831d385-1de6-407d-b7c2-f5d393881ca3.png">

#### Ejemplo de uso del script
<img width="1397" alt="image" src="https://user-images.githubusercontent.com/72032027/214211811-e4ee57d3-3a7e-435b-b508-a12cb25b6749.png">

----
### ExtractMethodHTTP
En base a un escaneo con nmap, si se cuenta con los puertos relacionados con servidores web, se realziar una petición HTTP utilizando el método POST para conseguir determinar si se trata de un servidor web y extraer los métodos HTTP soportados.

#### Banner de ayuda del script
<img width="1066" alt="image" src="https://user-images.githubusercontent.com/72032027/214211932-6ac7cfc7-4c6e-4ea0-818c-b8396a839214.png">

#### Ejecución del script
<img width="1397" alt="image" src="https://user-images.githubusercontent.com/72032027/214211987-337f6d93-e5be-40e7-aa4b-597e78ad2978.png">

----
Estos scripts son sencillas implementaciones, pero se han desarrollado principalmente para aprender y profundizar en el contexto de Python para pentesters.
