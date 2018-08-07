#!/usr/bin/env bash

original_dir=$(pwd)
shell_dir=$(cd "$(dirname "$0")"; pwd)

cd ${shell_dir}

while True:
do
    curl -v http://149.56.106.215:8000

done

cd ${original_dir}