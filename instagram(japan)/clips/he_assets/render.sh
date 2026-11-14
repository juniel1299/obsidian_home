set -e
P=/tmp/reel-current/bin/python
F=$($P -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')
"$F" -y -v error -f concat -safe 0 -i concat.txt -i audio.m4a -vf "ass=${1:-layout.ass}:fontsdir=/System/Library/Fonts,format=yuv420p" -map 0:v -map 1:a -t 70 -r 30 -c:v libx264 -preset veryfast -crf 17 -threads 4 -c:a copy -movflags +faststart ../Lee_Seung_Chul_My_Love_reel.mp4
