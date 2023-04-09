# Notas de esta sala

Esta sala contiene informacion de que contenido se puede encontrar en los sitios web, que podrian llegar a ser de utilidad para encontrar vulnerabilidades

Se mencionan 3 tipos

- Manual
- Osint
- Automatizado

## Manual
para el manual podemos ver si existen los archivos: 

- robots.txt 
- favicon
- sitemap.xml

Tambien se pueden revisar cabeceras http o revisar el framework con el que se desarrollo el sitio.

Todos los desafios de este tema son faciles de resolver

## Osint

En el apartado de osint se encuentra
- Google Dorking: para buscar archivos, rutas o contenido especifico
- Wappalyzer: es una extension de navegador que analiza la estructura del sitio encontrando asi las tecnologias con que fue desarrollado y sus posibles versiones
- Wayback machine: tiene almacenado versiones antiguas de los sitios, cuenta con informacion a partir de los 90's y puede ser util por si en una version antigua habia comentarios en el sitio que sean de utilidad
- Github: Podemos tratar de buscar codigo fuente de la empresa en cuestion
- S3 bucket: Amazon tiene un servicio de almacenamiento que algunas veces no esta correctamente protegido

## Automatizado

Existen herramientas que haciendo uso de un wordlist pueden realizar busquedas de archivos y rutas con nombres conocidos

entre las herramientas estan

- ffuf: no la he usado
- dirb: un poco lento
- gobuster: es algo optimo

Existen mas herramientas es cuestion de ver cual se adapta en cuanto a capacidad y agresividad, ademas influye que haya un buen wordlist


