#! /bin/bash

(make && make && make && make && make) & # 5
sleep 20
(make && make && make && make && make) & # 10
