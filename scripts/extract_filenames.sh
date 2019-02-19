#!/bin/bash
ls --width=1  *.wav  | sed -e s/.wav// -e s/// > name_list.txt;
