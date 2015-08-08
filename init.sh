#!/bin/bash

function init {
	uwsgi-2.7 -s /tmp/uwsgi.sock --module app --callable app &
}

USAGE="Usage: $0 [init | kill | restart]"

if [ "$#" == "0" ]; then
	echo "$USAGE"
	exit 1
fi

if [ "$1" == "init" ]; then
	init
elif [ "$1" == "kill" ]; then
	pkill uwsgi
elif [ "$1" == "restart" ]; then
	pkill uwsgi
	init
fi
