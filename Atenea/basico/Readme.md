# Ejercicios resueltos

Resolucion de [Ejercicios](https://atenea.ccn-cert.cni.es/challenges?category=bsica) basicos recuerde poner la respuesta en el formato solicitado.

## hash

`echo -n 'LearnTheHashFunction' | md5sum`

## hash 2

`echo -n 'ThisIsAMoreSecureHashFunction' | sha256sum`

`echo -n 'hash_sha256sum' | md5sum`

## hash 3

se utilizo la pagina

[hashes.com](https://hashes.com/en/decrypt/hash)

pero puedes usar cualquier otra.

`echo -n 'cadenaEncontrada' | md5sum`

## ASCII

funcion que transforma de ascii a texto.

`echo '080 097 115 115 119 111 114 100 032 112 097 114 097 032 115 117 112 101 114 097 114 032 101 108 032 114 101 116 111 058 032 084 104 101 065 083 067 073 073 084 097 098 108 101 033' | awk '{ for(i=1;i<=NF;i++) printf("%c",$i); print "";  }'`

## Base64

contenido del archivo

UmVjdWVyZGEgcXVlIGN1YW5kbyBjb2RpZmljYXMgYWxnbyBlbiBiYXNlNjQgTk8gbG8gZXN0w6Fz
IGNpZnJhbmRvLCBzaW5vIHF1ZSBzaW1wbGVtZW50ZSBsbyBlc3TDoXMgY29kaWZpY2FuZG8uDQoN
CkxhIGNvbnRyYXNlw7FhIHBhcmEgc3VwZXJhciBlc3RlIHJldG8gZXM6IHJlY3VlcmRhcXVlYmFz
ZTY0Tk9lc2NpZnJhcg0KCg==

decodificando

`echo 'UmVjdWVyZGEgcXVlIGN1YW5kbyBjb2RpZmljYXMgYWxnbyBlbiBiYXNlNjQgTk8gbG8gZXN0w6Fz
IGNpZnJhbmRvLCBzaW5vIHF1ZSBzaW1wbGVtZW50ZSBsbyBlc3TDoXMgY29kaWZpY2FuZG8uDQoN
CkxhIGNvbnRyYXNlw7FhIHBhcmEgc3VwZXJhciBlc3RlIHJldG8gZXM6IHJlY3VlcmRhcXVlYmFz
ZTY0Tk9lc2NpZnJhcg0KCg==' | base64 --decode`

## Hex

`echo "50617373776f72643a2044346d7054686548337821" | xxd -p -r`

## XOR

obtenemos las cadenas en hexadecimal.

`echo "encryptXORkey" | xxd`

`base64 -d <<< HQERKhYCLDc9KgQX | xxd`

obtenemos las cadenas en hexadecimal y tienen que ser del mismo tamano para hacer la operacion XOR.

- 656e6372797074584f526b65

- 1d01112a16022c373d2a0417

Se uso [esto](https://xor.pw/)

Y luego obtenemos el mensaje

`echo "786f72586f72586f72786f72" | xxd -p -r`

## Entropy

Para este ejercicio utilice la herramienta que recomienda [cyberchef](https://gchq.github.io/CyberChef/)

Se busca la opcion de entropy y puedes subir la carpeta entera!

luego con shannon scale puedes ver los numeros y con un poco de paciencia encuentras el mayor

Sin embargo existen mas formas de automatizar,

## Magic number

`xxd magicnumber | head -n 1`

## Strings

`strings lookinside | grep -i '.com'`

## Metadatos

solo fue necesario usar la herramienta [exiftool](https://exiftool.org/)

## Metadatos 2

Usamos la misma herramienta

## Variable

Si sabes de programacion no hay problema, caso contrario revisa la documentacion que proporciona la plataforma.

## Variable 2

Si usaste Linux es pan comido, ya que solo es un echo, o no?

## Python

instalas librerias (usa [entornos virtuales](https://www.programaenpython.com/miscelanea/crear-entornos-virtuales-en-python/) te sera util, y recuerda que el mejor nombre para tu entorno es .venv >.o )

`pip install pycrypto`

agregas un print para que muestre el mensaje y listo!


## C

La manera rapida en Linux

`gcc script.c`

`./a.out`

Luego puedes investigar mas detalles

## Java

Hay que decompilar una clase, por lo cual se uso [cfr](https://github.com/leibnitz27/cfr), sin embargo, se puede usar herramientas online u otras de tu preferencia.

`java -jar cfr.jar main.class`
