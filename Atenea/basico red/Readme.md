## Modelo TCP/IP

TCP/IP es un conjunto de protocolos que permiten la comunicación entre los ordenadores pertenecientes a una red. La sigla TCP/IP significa Protocolo de control de transmisión/Protocolo de Internet. Proviene de los nombres de dos protocolos importantes incluidos en el conjunto TCP/IP, es decir, del protocolo TCP y del protocolo IP.

Este modelo incluye cuatro capas. Para superar el reto indica el número de capa (en formato numérico, por ejemplo: 15) correspondiente a la capa de Internet.

### Solucion

Se cuenta de abajo hacia arriba.

![image](https://imgs.search.brave.com/9boy300L9kOi-lAK8pAT5lyQvS5TAKCC2dQIzapE3-0/rs:fit:942:728:1/g:ce/aHR0cHM6Ly9pbWFn/ZS5zbGlkZXNoYXJl/Y2RuLmNvbS9ucHMx/MDctdG1wLTEwMDQy/MTE4MDAyMi1waHBh/cHAwMi85NS9wcm90/b2NvbG8tdGNwaXAt/MTYtNzI4LmpwZz9j/Yj0xMjcxODcyODI5)

## Direccion IP

La dirección IP es un conjunto de números que identifica a un equipo dentro de una red que utilice el protocolo Internet Protocol (IP) o que corresponde al nivel de red del modelo TCP/IP.

La versión 4 de la dirección IP (IPv4) utiliza un formato de 4 números separados por un punto entre ellos.

Para superar este reto, indica cuál es una IPv4 válida:

- 45.2.6..1
- 192.1t8.32.8
- 8.8.8.8.8
- 3:4:5:6
- 212.27.123.45
- 00.25.350.56
- 128.76.64.258

### Solucion

Solo hay que saber que el formato de una direccion ip (version 4) va de la siguiente forma

X.X.X.X

Donde: X puede ser un valor entre 0 y 255

Con eso en mente se puede ver la respuesta.

## Direccion IPv6

IPv6 es el sucesor del primer protocolo de direccionamiento de Internet, Internet Protocol versión 4 (IPv4). A diferencia de IPv4, que utiliza una dirección IP de 32 bits, las direcciones IPv6 tienen un tamaño de 128 bits. Por lo tanto, IPv6 tiene un espacio de direcciones mucho más amplio que IPv4.

Una dirección IPv6 (128 bits) se representa mediante ocho grupos de cuatro dígitos hexadecimales, cada grupo representando 16 bits (dos octetos). Los grupos se separan mediante dos puntos (:).

Para superar este reto, averigua la IPv6 válida:

- 192.168.1.1
- 80.40.32.112.0.0.1.12
- ab00.12cd.4eef.2100.4e11.0a22.3333.1f44
- 2001:0aa8:13ed:0000:0000:ff7a:98ff:0001
- 2ae3::0::0233:1:
- 8.8.8.8
- 1aad:3aaa:13ej:0000:0000:ff7a:98ff:0001

### Solucion

Como en el anterior se puede seguir esa logica revisando las premisas, sin embargo puedes usar la [web](https://www.linkwebbie.com/apps/index/ipv6-validator/) para validar la opcion que creas correcta.

## Direcciones IP privadas y públicas

Una dirección IP puede ser privada o pública. Las IPs privadas se utilizan para las comunicaciones de los equipos dentro de una red local, mientras que las IPs públicas se utilizan para las comunicaciones a través de Internet.

Por ejemplo, en una red doméstica, en la que se tiene un router ADSL o de fibra, los equipos conectados a él mediante wifi o cable tendrán una dirección IP privada, pero saldrán a Internet usando la misma dirección IP pública.

Los rangos de IPs privadas están definidos dentro del RFC1918.

Para superar este reto, indica cuál de las siguientes IPs es una IP privada:

- 8.8.8.8
- 192.178.1.1
- 172.25.0.3
- 85.32.11.0
- 172.0.0.1
- 12.10.25.4
- 11.22.33.44
- 0.0.0.0

### Solucion

Revisa la documentacion!

## DHCP

El protocolo de configuración dinámica de host (en inglés: Dynamic Host Configuration Protocol, también conocido por sus siglas de DHCP) es un protocolo de red de tipo cliente/servidor mediante el cual un servidor DHCP asigna dinámicamente una dirección IP y otros parámetros de configuración de red a cada dispositivo en una red para que puedan comunicarse con otras redes IP. Este servidor posee una lista de direcciones IP dinámicas y las va asignando a los clientes conforme estas van quedando libres, sabiendo en todo momento quién ha estado en posesión de esa IP, cuánto tiempo la ha tenido y a quién se la ha asignado después.

En el fichero adjunto, el servidor DHCP asigna una IP privada a un equipo. Indica de qué IP se trata.

[file](https://atenea.ccn-cert.cni.es/download?file_key=fb8932b02032325f41bb140e66faedd45163a612f941d56af9b4802f754b3885&team_key=343bee252e8abb99be6877f715991a6457470ad034881e03ed1d0c07df1096aa)

### Solucion

Abrimos el archivo con [wireshark](https://www.wireshark.org/), revisando el historial en la columna de Destino vemos las IP a las que van los paquetes.

## Máscara de red

La máscara de red es una combinación de bits que sirve para delimitar el ámbito de una red de ordenadores. Su función es indicar a los dispositivos qué parte de la dirección IP es el número de la red, incluyendo la subred, y qué parte es la correspondiente al host.

Para superar este reto, indica la equivalencia en el formato CIDR de esta máscara de red (por ejemplo: 37):

- 255.255.255.0

## Máscara de red 2

La máscara de red se puede representar en diversos formatos.

Para superar este reto, indica la equivalencia en formato decimal de la máscara /20 del formato CIDR (por ejemplo: 255.255.255.0)

### Solucion

Esta [referencia](https://docs.oracle.com/cd/E19957-01/820-2981/exlvx/index.html) sirve para ambos desafios.


## MAC

La dirección MAC (Media Access Control) es un identificador único para cada dispositivo de red. Se la conoce también como dirección física, y su valor depende del fabricante.

Para superar este reto, indica el fabricante (primera letra en mayúsculas) de la tarjeta de red con la siguiente dirección MAC:

fc:f8:ae:f1:fd:ec:8a:aa

### Solucion

Buscar en Google xD

## Puerto

En el ámbito de Internet, un puerto es el valor que se usa, en el modelo de la capa de transporte, para distinguir entre las múltiples aplicaciones que se pueden conectar al mismo host, o puesto de trabajo.

Aunque muchos de los puertos se asignan de manera arbitraria, ciertos puertos se asignan, por convenio, a ciertas aplicaciones particulares o servicios de carácter universal.

Para superar este reto, indica el puerto asignado por convenio para HTTP.

## Puerto 2

Para superar este reto, indica el puerto asignado por convenio para HTTPS.

## Puerto 3

Para superar este reto, indica el puerto de origen más bajo utilizado para las comunicaciones en el fichero de captura de tráfico que se adjunta.

[archivo](https://atenea.ccn-cert.cni.es/download?file_key=b30e9786754fdbb5052ff6e50827b6dcfc0fa6f8bc1db8521a6b7872c5942112&team_key=343bee252e8abb99be6877f715991a6457470ad034881e03ed1d0c07df1096aa)

### Solucion de puertos

Para los 2 primeros solo es leer la documentacion, son puertos bastante conocidos

Para el 3 el uso de wireshark es importante, la respuesta esta en un puerto poco comun para la comunicacion y que sea bajo.

## DNS

El sistema de nombres de dominio (DNS) sirve como traductor de direcciones IP a nombres de dominio y viceversa. Se podría decir que es como una agenda de Internet.

Para pasar este reto indica el nombre de dominio correspondiente a la siguiente dirección IP:

8.8.8.8

### Solucion

`nslookup 8.8.8.8`

## DNS 2

El sistema de nombres de dominio sirve como traductor de direcciones IP a nombres de dominio y viceversa. Es como una agenda de Internet.

Para pasar este reto indica la dirección IPv4 correspondiente al siguiente dominio:

www.ccn-cert.cni.es

### Solucion

[referencia](https://www.nslookup.io/domains/www.ccn-cert.cni.es/dns-records/)

## Telnet

Telnet es el nombre de un protocolo de red que nos permite acceder a otra máquina para manejarla remotamente como si estuviéramos sentados delante de ella. El puerto que se utiliza generalmente es el 23. Debido a que las comunicaciones se realizan sin ningún tipo de cifrado, se considera un protocolo inseguro.

En la siguiente captura de tráfico un usuario se ha conectado remotamente a un servidor utilizando este protocolo. Para ello, ha tenido que autenticarse mediante usuario y contraseña. Para superar este reto, indica la contraseña utilizada.

[telnet](https://atenea.ccn-cert.cni.es/download?file_key=a859dc59f36b89085e5a952308ba92b0b8383b71a8055430af945d3c32f18552&team_key=343bee252e8abb99be6877f715991a6457470ad034881e03ed1d0c07df1096aa)

### Solucion

usando wireshark y revisando en orden los paquetes de TELNET, podemos ver el password letra por letra.