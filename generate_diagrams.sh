#!/bin/bash

build_diagram(){    
    echo "Building ${1}"
    python $1
}

for path in $(find -name \*_diagram.py); do
    build_diagram $path
done

for path in $(find -name \*_chart.py); do
    build_diagram $path
done

echo "All diagrams generated"