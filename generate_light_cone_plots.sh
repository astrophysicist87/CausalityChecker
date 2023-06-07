#! /bin/bash
#-----------

directoryToProcess=$1

echo 'Resetting frame directory'
rm -rf $directoryToProcess/light_cone_frames && mkdir -p $directoryToProcess/light_cone_frames


# for MUSIC
echo 'Compute local speeds'
grep 'FLOWPROFILE: ' $directoryToProcess/mode_2.log \
                     | awk '{print $2, $3, $4, sqrt($9**2+$10**2+$11**2)}' \
                     > $directoryToProcess/local_speed.dat

# combine causality and local speed data
echo 'Consolidate light cone data'
./get_light_cone_data_src/get_light_cone_data \
  $directoryToProcess/causality_check_w_characteristic_velocities.dat \
  $directoryToProcess/local_speed.dat \
  > $directoryToProcess/light_cone_data.dat

# split into frames
echo 'Split into frames'
split --lines=$2 -d --suffix-length=4 \
        $directoryToProcess/light_cone_data.dat \
        $directoryToProcess/light_cone_frames/light_cone_frames

# generate a movie from these frames
echo 'Generate movie'
python3 generate_light_cone_movie.py \
          $directoryToProcess/light_cone_frames/light_cone_frames*

# for VISHNU
