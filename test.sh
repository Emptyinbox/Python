#!/bin/bash
pid_python=$(pidof python)
echo $pid_python

A=$( printf '%04d' $pid_python )
echo $A
kill -15 $A