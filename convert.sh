#!/usr/local/bin/tclsh

package require sound

sound::sound snd

set file_list [glob *.mp3]

foreach file $file_list { 
    snd read $file 
    snd convert -format lin16 -channels 1 -frequency 8000 
    snd write [file rootname $file].wav 
}