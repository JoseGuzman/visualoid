# OrganoStation

[![CodeFactor](https://www.codefactor.io/repository/github/joseguzman/organostation/badge)](https://www.codefactor.io/repository/github/joseguzman/organostation)

The [OrganoStation](http://www.organostation.com) is a customized system to obtain neurophysiological signals (e.g., EEG)
in brain organoids or other in vitro preparations.
It also contains a visualization app to document and analyze electrical or fluorescence signals.

## List of contents of directories 
```
.
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- config.py
|-- organostation
|   |-- __init__.py
|   |-- dashboards
|   |   |-- testboard
|   |   `-- visualoid
|   |-- guest 
|   |   |-- routes.py
|   |   |-- static
|   |   `-- templates
|   |-- premium
|   |   |-- static
|   |   `-- templates
|   |-- static
|   `-- templates
|       |-- blueprintinfo.jinja2
|       |-- layout.jinja2
|       `-- navigation.jinja2
|-- requirements.txt
|-- run.sh
`-- wsgi.py
```

## Installation
 * You may need to install [Node.js](https://nodejs.org/en/download/) and less with `npm install less`

### Installation with 'requirements.txt'
Type `bash run.sh`

### Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

Type `pip install pipenv` to install pipenv and create an environment
using 

```shell
$ git clone https//github.com/JoseGuzman/organostation.git
$ cd organostation
$ mkdir .venv
$ pipenv shell
$ pipenv update 
$ python wsgi.py
```

## Docker 
