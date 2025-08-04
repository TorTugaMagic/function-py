# Function
## Mis practicas de funciones de Python.


## Crear venv
```bash
    virtualenv ~/.venv
  
```

## usar la VENV
```bash
    source ~/.venv/bin/activate
```

```bash
    vim ~/.bashrc
```
### para que se inicie el automatico VENV cuando se abrea nueva pestaña de terminal o se inicie sesion.
```bash
    presionar i
    #Al final del archivo poner: 
     source ~/.venv/bin/activate
```

## Contruir imagen a apartir del Dockerfile
```bash
    docker build .
    docker image ls
```

### Run conteiner
```Bash
docker run -p 127.0.0.1:8080:8080 <Nombre del contenedor o clave>
```

## solicitar la busqueda
```
    bash run invoke.s
```
## Buscar el puerto
```
    ps -ef | grep python
```
