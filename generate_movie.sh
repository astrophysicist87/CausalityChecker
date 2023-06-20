#!/usr/bin/env bash
#------------------

cwd=`pwd`

filePath=`readlink -e $1`
fileDirec=`dirname $filePath`
fileName=`basename $filePath`

eDec=$4

(
	cd $fileDirec
	rm -rf frames slides out.mp4 out_wReg.mp4
	mkdir frames
	mkdir slides

  echo 'Splitting file using split --lines='$3' -d --suffix-length=4 '$fileName' frames/frame'
  # assuming same number of lines for each tau...
	split --lines=$3 -d --suffix-length=4 $fileName frames/frame
	nFiles=`\ls -1 frames/frame* | wc -l`
	#for ((i=$nFiles; i<=$[nFiles+10]; i++))
	for i in $(seq -f "%04g" $nFiles $[nFiles+10])
	do
		echo > frames/frame${i}
	done
	for file in frames/frame*
	do
		mv $file $file".dat"
	done
)

	# Get total number of frames
	i=`\ls -1 $fileDirec/frames/frame* | wc -l`

	# This generates frames for the animations
	echo 'Executing python generate_frames.py '$2' 0 '$i' '$fileDirec'/frames '$fileDirec'/slides' $4 $5
	python generate_frames.py $2 0 $i $fileDirec/frames $fileDirec/slides $4 $5

        # This generates frame sequence plots specifically for paper
        echo 'Executing python generate_plots.py '$2' 0 '$i' '$fileDirec'/frames '$fileDirec'/slides' $4 $5
        python generate_plots.py $2 0 $i $fileDirec/frames $fileDirec/slides $4 $5

(
	cd $fileDirec
	framesPerSecond=60
	pngs2mp4 $framesPerSecond slides/slide%04d.png out.mp4  
        #framesPerSecond=5
        #pngs2mp4 $framesPerSecond slides/slide_wReg%04d.png out_wReg.mp4
)
