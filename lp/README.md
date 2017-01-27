# instalacion 

***se ha modificado el formato para el comentario de "##region..." ahora es "# region..." para compatibilizar con los estándares***

## Linux y Mac

1 .- crear un symlink de este directorio "lptornado"  a /ruta_a_path_de_python/lp ( ojo con el lp )

	$sudo ln -s /ruta_a_lptornado /usr/lib/python2.7/lp

2 .- ubicar carpeta de "package" en sublime text
3 .- agregar un symlink del directorio lptornado_sublime, al directorio package/User

	$sudo ln -s /Users/ricardo/git_loadingplay/lptornado.git/lptornado_sublime/ /Users/ricardo/Library/Application\ Support/Sublime\ Text\ 3/Packages/lptornado


## para usar mysql

```sh
$ pip install MySQLdb
```

## para usar con postgres

```sh
$ pip install psycopg
```

# Windows


la carpeta de Package se encuentra en %appdata%/Sublime Text 3/Packages

```sh
    c:\  explorer %appdata%
```

# backup and restore data

## postgres

backup

```sh
    $ sudo -u postgres pg_dump --role=mprint --data-only --column-inserts -W mprint > bak20150121.sql
```


restore

```sh
    $ sudo -u postgres psql mprint < bak20150129.dump
```



## mysql

backup

```sh
    $ sudo mysqldump -u root -p[root_password] [database_name] > dumpfilename.sql
```

restore

```sh
    $ sudo mysql -u root -p[root_password] [database_name] < dumpfilename.sql
```


## running testing

```
watchmedo shell-command     \
--patterns="*.py;*.txt"     \
--command='clear && python -m tests' \
--recursive     \
/Users/ricardo/git_loadingplay/lptornado.git
```
