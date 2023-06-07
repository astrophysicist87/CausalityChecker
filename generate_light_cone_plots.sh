#! /bin/bash
#-----------

directoryToProcess=$1

# for MUSIC
grep 'FLOWPROFILE: ' $directoryToProcess/mode_2.log \
                     | awk '{print $2, $3, $4, sqrt($9**2+$10**2+$11**2)}' \
                     > $directoryToProcess/local_speed.dat





# for VISHNU
