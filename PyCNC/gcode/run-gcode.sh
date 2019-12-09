#!/usr/bin/env bash

# Copyright (c) 2019 Kyle Petryszak

# Directory that the script resides in
sdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit 1
fi

# File path
file=$1

filename=$(sed 's@.*/@@' <<< "$file")

m_file=modified-$filename
mkdir -p $sdir/modified
cp "$sdir/$file" "$sdir/modified/$m_file"

dos2unix "$sdir/modified/$m_file"
sed -i '/Z/d' "$sdir/modified/$m_file"
sed -i '/M/d' "$sdir/modified/$m_file"
sed -i 's/E/Z/g' "$sdir/modified/$m_file"
sed -i '/Z\-/d' "$sdir/modified/$m_file"

sudo pypy $sdir/../pycnc "$sdir/modified/$m_file"

exit 0
