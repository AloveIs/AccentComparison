#!/bin/sh
# the next line restarts using wish \
exec tclsh8.6 "$0" "$@"

package require snack

snack::sound s

set frame_l 0.05
set f [open list.txt]
set list [read $f]
close $f

foreach file $list {
 s read $file

 set fd [open [file rootname $file].f0 w]
 puts $fd [join [s pitch -method esps -framelength $frame_l] \n]
 close $fd

 set fd [open [file rootname $file].frm w]
 puts $fd [join [s formant -framelength $frame_l] \n]
 close $fd

 set fd [open [file rootname $file].pwr w]
 puts $fd [join [s power -framelength $frame_l] \n]
 close $fd
}


exit
