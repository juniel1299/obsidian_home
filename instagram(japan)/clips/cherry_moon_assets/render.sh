set -e
P=/tmp/reel-nov09/bin/python
F=$($P -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')
"$F" -y -v error -f concat -safe 0 -i concat.txt -i audio.m4a -vf "ass=${1:-layout.ass}:fontsdir=/System/Library/Fonts,format=yuv420p" -map 0:v -map 1:a -t 56 -r 30 -c:v libx264 -preset fast -crf 17 -threads 4 -c:a copy -movflags +faststart ../Cherry_Filter_Moonlight_Boy_reel.mp4
