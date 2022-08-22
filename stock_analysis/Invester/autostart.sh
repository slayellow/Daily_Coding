#!/bin/bash

echo "------------------------------"
echo "Export PATH"
echo "------------------------------"
echo ""
export 
PATH=/Users/hongjinseog/opt/anaconda3/bin:/Users/hongjinseog/opt/anaconda3/condabin:/opt/homebrew/opt/qt@5/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/opt/local/bin:/opt/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/VMware 
Fusion.app/Contents/Public:/Library/Apple/usr/bin

echo "------------------------------"
echo "Source Conda.sh"
echo "------------------------------"
echo ""
source /Users/hongjinseog/opt/anaconda3/etc/profile.d/conda.sh

echo "------------------------------"
echo "Conda Activate Py39"
echo "------------------------------"
echo ""
conda activate
conda activate py39

echo "------------------------------"
echo "Run Python File"
echo "------------------------------"
echo ""
python DBUpdater.py
