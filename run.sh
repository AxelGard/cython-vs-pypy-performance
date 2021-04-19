rm -r perf/*.so
rm -r build/*
python3 setup.py build_ext --inplace
python3 perf/cy_test.py
pypy/bin/pypy3.7 -m perf
python3 perf/py_tests.py
