rm -r perf/*.so
rm -r build/*
python3 setup.py build_ext --inplace
python3 -m perf
