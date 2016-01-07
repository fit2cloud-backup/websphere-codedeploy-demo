#!/bin/bash

echo install dependencies
DIRECTORY=/opt/websphere-demo
if [ ! -d "$DIRECTORY" ]; then
	mkdir $DIRECTORY
fi