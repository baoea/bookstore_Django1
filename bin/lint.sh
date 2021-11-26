#!/usr/bin/env bash

set -e

if [ "$1" == "-h" -o "$1" == "--help" ]; then
  echo "Run lint command."
  echo ""
  echo "Usage: `basename $0`"
  echo "       `basename $0` --fix"
  exit 0
elif [ "$1" == "--fix" ]; then
  docker-compose run bookstore python -m isort .&& \
  docker-compose run bookstore python -m black ./bookstore/&& \
  docker-compose run bookstore python -m flake8 ./bookstore
else
  docker-compose run bookstore python -m isort . --check-only && \
  docker-compose run bookstore python -m black ./bookstore/ --check && \
  docker-compose run bookstore python -m flake8 ./bookstore
fi
