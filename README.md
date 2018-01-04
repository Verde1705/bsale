# Bsale Python

un **APIclient** para acceder de forma más facil a la api de bsale usando python.

## Instalación

usando pip:

```sh
$ pip install git+https://github.com/loadingplay/bsale.git --process-dependency-links
```

o descargando el código fuente:

```sh
$ git clone https://github.com/loadingplay/bsale.git
$ cd bsale
$ python setup.py install
```

## Uso

ejemplo:

```python
import bsale

client = bsale.API(token="[YOUR_ACCESS_TOKEN]")

client.Document.Create({
    "documentTypeId": 8,
    "officeId": 1,
    "priceListId": 18,
    "emissionDate": 1407715200,
    "expirationDate": 1407715200,
    "declareSii": 1
})

```

## Dónde continuar

por ahora, no tenemos documentacion, pero cada metodo ha sido testeado usando httmock

https://github.com/loadingplay/bsale/tree/master/tests
