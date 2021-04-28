# cython-vs-pypy-performance

This project is a compearance of PYPY and Cython.

PYPY the just in time compiler compered to Cython a mix of C and python.  


## install && run

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
sh run.sh
```

## results

```json
{
    "factorial": {
        "python":0,
        "cython":0,
        "pypy":0,
    },

    "matrix multiply": {
        "python":0,
        "cython":0,
        "pypy":0,
    },

    "adding numbers": {
        "python":0,
        "cython":0,
        "pypy":0,
    },
}
```

The results will be garphs in `graph/img/`
