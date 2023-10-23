# CRYPTOHACK

Una plataforma divertida y gratuita para aprender criptografía moderna

[Sitio](https://cryptohack.org/)

## Introduccion

En la plataforma hay diferentes desafios que involucran el buscar banderas

Estas banderas normalmente estarán en el formato crypto{y0ur_f1rst_fl4g}. El formato de bandera le ayuda a verificar que encontró la solución correcta.

## Python

Es una buena idea el usar python para el encriptado por lo que saber este lenguaje es fundamental

```py
#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))

```

Tambien podemos usarlo para conectarnos de forma remota a distintos servidores y automatizar procesos

```py
#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

request = {
    "buy": "clothes"
}
json_send(request)

response = json_recv()

print(response)

```