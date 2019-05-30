#!/bin/bash

for((i=0;i<=40;i++));
do
    for((j=0;j<=255;j++));
    do
        ping -w 1  192.168.$i.$j >> pingLog
    done

done 
