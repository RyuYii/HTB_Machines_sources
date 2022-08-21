# ATENEA

 [Atenea](https://atenea.ccn-cert.cni.es/home) es una plataforma de desafíos de seguridad informática compuesta por diferentes retos que abarcan diferentes campos, como Criptografía y Esteganografía, Exploiting, Forense, Networking y Reversing, entre otros.


 ![logo](https://imgs.search.brave.com/ZBgfzeBDkwY51LdAgeYXRt1zFqnd9lRdiQ5m0QT3a8Y/rs:fit:284:225:1/g:ce/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5i/S1ZTSUJmQ29OVVl3/c2pBaTM0bXhBQUFB/QSZwaWQ9QXBp)

 #### Funcion generadora

 Esta funcion te servira para genera la bandera en el formato que pide la plataforma

 ```
 md5(){
     echo -n $1 | md5sum | awk '{print "flag{"$1"}"}'
 }
 ```
 ejemplo

`md5 "cadena"`