#!/bin/bash

DOCKER_FILE="gtramontina/diagrams:0.22.0"

build_diagram(){    
    echo "Building ${1}"
    python $1
}

echo "Pulling Docker Image..."

for path in $(find -name \*_diagram.py); do
    build_diagram $path
done

echo "All diagrams generated"