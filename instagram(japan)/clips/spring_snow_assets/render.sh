set -e
P=/tmp/reel-nov09/bin/python
F=$($P -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')
"$F" -y -v error -f concat -safe 0 -i concat.txt -i audio.m4a -vf "tpad=stop_mode=clone:stop_duration=0.1,ass=${1:-layout.ass}:fontsdir=/System/Library/Fonts,format=yuv420p" -map 0:v -map 1:a -t 68.1 -r 30 -c:v libx264 -preset fast -crf 17 -threads 4 -c:a copy -movflags +faststart ../PENTAGON_Spring_Snow_reel.mp4
