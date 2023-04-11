# Apuntes

ver vulnerabilidades smb

`nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.208.99`

ver directorios compartidos o montables

`nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.208.99`

Utilizamos la vulnerabilidad de proFTP para copiar la clave ssh al directorio montable

Montar directorio compartido por nfs

`sudo apt install nfs-common`
`sudo mount -t nfs -o vers=4 10.10.208.99:/var /mnt/kenobiNFS`

buscar binarios con SUID

`find / -perm -u=s -type f 2>/dev/null`