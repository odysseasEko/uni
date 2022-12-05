#!/bin/bash

echo "Hello Odysseas! Whats the name of the new website?";

read varname;

echo "Great creating $varname files!"

mkdir $varname;
cd $varname;
touch $varname-Main.html;
touch $varname-Style.css;
touch $varname-Code.js;
mkdir content;
ls;
sleep 1
echo "have fun in SPACE!";
sleep 1
vim;