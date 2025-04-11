# ADNameGen - AD Name Combinator

**ADNameGen** es una herramienta diseñada para generar combinaciones comunes de nombres de usuarios en entornos de Active Directory (AD) basados en listas de nombres y apellidos.

La herramienta toma una lista de nombres completos y genera posibles combinaciones como:

- Nombre completo.
- Inicial de nombre + apellido.
- Nombre + inicial del apellido.
- Combinaciones con puntos, entre otras.

## Requisitos

- Python 3.x

## Instalación

- Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Retxus/ADNameGen.git
```

## Uso

```bash
python ADNameGen.py -h
usage: ADNameGen.py [-h] -i INPUT -o OUTPUT [--capitalize]

Common user name generator in AD environments.

options:
  -h, --help           show this help message and exit
  -i, --input INPUT    File with full names.
  -o, --output OUTPUT  File to save the combinations.
  --capitalize         Capitalize the first letter of name and lastname.
```

## Archivos de ejemplo

```bash
python ADNameGen.py -i users.txt -o save_users.txt

--------------------------------
 ADNameGen - AD Name Combinator

           by @Retxus
--------------------------------

Reading names from: users.txt

[*] Generates 53 combinations and saved in 'save_users.txt'.
```
