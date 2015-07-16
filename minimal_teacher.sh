#!/bin/bash
# the absolutely simplest teacher implementation possible
while nc -l -p 56789; do echo -e "\n--------------RELOAD--------------\n" ; done
