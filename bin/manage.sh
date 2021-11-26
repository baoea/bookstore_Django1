#!/usr/bin/env bash

docker-compose run bookstore python bookstore/manage.py $@
exit 0