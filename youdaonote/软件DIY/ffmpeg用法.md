录视频的时候选择24帧/s ，avi格式





截取视频



"H:\Program Files\AutoCutVideo\ffmpeg.exe" -i "20241222152733-信息技术课临别赠言-视频-1-merged-1735026648649.mp4" -ss 00:02:06 -codec copy -to  01:45:35 "1.MP4"



"C:\Program Files\乐影音下载器\ffmpeg.exe" -i "C:\Users\i\Videos\乐影音下载\《首席夜话》 20121118 朱清时：你是人才吗？.mp4" -ss 00:00:44 -codec copy -to  00:08:27.8 "有想法的贺建奎老师（《首席夜话》20121118）.MP4"



E:\360云盘\编程\Python\QDownloader\ffmpeg\ffmpeg.exe -i "录制_2015_11_16_11_24_31_267.MP4" -ss 00:00:00 -codec copy -to  00:00:40 "1.mp4"



ffmpeg -i "It Is A Small World.mp3" -ss 00:14:5 -codec copy -to 00:00:37  "1.mp3"

ffmpeg -i "It Is A Small World.mp3" -ss 00:01:02 -codec copy -to 00:01:21  "2.mp3"





从视频文件里提取音频



"C:\Users\i\LYYDownloader-dev\ffmpeg.exe" -i 

input.f4v 

-ss 00:00:07.00 -to 00:00:37.00 -map 0:a -codec copy output.aac



"C:\Program Files\乐影音下载器\ffmpeg.exe" -i "D:\乐影音下载\7231.flv" -ss 00:00:00 -to 01:04:39.500 -map 0:a -codec copy 李敖香港演讲.aac



http://superuser.com/questions/683371/ffmpeg-command-convert-a-part-of-video-file-to-an-audio-file



视频消音

 ffmpeg -i 1.mp4 -map 0:v -codec copy a.mp4





剪辑音频



# Trim from 00:02:54.583 to end of file



ffmpeg -i 5.mp3 -ss 00:00:46 -c copy output.mp3



# Trim from 00:02:54.583 for 5 minutes



ffmpeg -i 5.mp3 -ss 00:00:00 -to 00:47:00-acodec copy output.mp3



垂直翻转对称

ffmpeg -i in.avi -vf "vflip" out.avi





ogg转MP3



ffmpeg -i raw_011.ogg -acodec libmp3lame raw_011.mp3





 -i C:\致敬Mdict\英美发音\data\A-frame.spx raw_013.MP3





Useful FFmpeg Commands



http://www.labnol.org/internet/useful-ffmpeg-commands/28490/



 



合并视频（相同编码）



mylist.txt







# this is a comment



file '/path/to/file1'



file '/path/to/file2'



file '/path/to/file3'







ffmpeg -f concat -i mylist.txt -c copy output.MP4







合并视频（不同编码）

ffmpeg -loop 1 -i 1.png -t 3 1.mpg

ffmpeg -i 2.avi -qscale:v 1 2.mpg

ffmpeg -loop 1 -i 3.png -t 3 3.mpg

ffmpeg -loop 1 -i 4.png -t 3 4.mpg





ffmpeg -i concat:"1.mpg|2.mpg|3.mpg|4.mpg" -c copy intermediate_all.mpg



ffmpeg -i intermediate_all.mpg -qscale:v 2 5.flv







ffmpeg -i concat:"1.mpg|2.mpg|3.mpg|4.mpg|5.mpg" -c copy intermediate_all.mpg





------------合并视频音频（要求视频无声音）

ffmpeg -i intermediate_all.mpg -i test03.mp3  -c:v copy -c:a aac -strict experimental -shortest output.mpg           #这个不行的啦

ffmpeg -i intermediate_all.mpg -i test03.mp3  -c:v copy -c:a aac -strict experimental -shortest output.flv





http://www.ffmpeg.org/faq.html#toc-Concatenating-using-the-concat-protocol-_0028file-level_0029







图片转视频



ffmpeg -loop 1 -i 1.png -t 3 1.avi



#指定每秒15帧



ffmpeg -loop 1 -r 15 -i 1.png -t 3 1.avi





淡出

ffmpeg -i output.mp3 -af afade=t=out:st=40:d=6 test03.mp3



做法是先fade音频，start_time和duration都是秒（指明时分秒会出错），fade出来后再和视频用360快剪辑合并

"C:\Program Files\乐影音下载器\ffmpeg.exe" -i Breathingplace.m4a -af "afade=t=out:start_time=124:duration=6"   "2Breathingplace.m4a"



淡入淡出

ffmpeg -i INPUT -af afade=t=in:st=60:d=4,afade=t=out:st=125:d=5 OUTPUT



St=起始时间       d=duration





合并视频音频

ffmpeg -i 5.avi -i test03.mp3  -c:v copy -c:a aac -strict experimental -shortest output.avi



ffmpeg -i intermediate_all2.mpg -i test03.mp3  -c copy -shortest output2.mpg



ffmpeg -i 1.mp4 -i 1.m4a  -c:v copy -c:a aac -strict experimental a.mp4



ffmpeg  -i a1.mp4 -i 1.m4a  -vcodec copy -acodec copy a.mp4



8000hz解决方法

ffmpeg -y -i  end.mp4 -i 20150318-214128.mp3 -map 0:0 -map 1:0 -c:v

copy -c:a libmp3lame -ar 44100 -aq 0 withaudio.mp4



顺时针旋转90度

ffmpeg -i 2.mp4 -vf "transpose=1" b.mp4



0 = 90CounterCLockwise and Vertical Flip (default)

1 = 90Clockwise

2 = 90CounterClockwise

3 = 90Clockwise and Vertical Flip





180°转



ffmpeg -i 3.mp4 -vf "transpose=2,transpose=2" c.mp4



提升至2倍音量

"D:\BaiduYunDownload\编程\Python\Project\LYYDownloader-qt5\ffmpeg.exe" -i "D:\BaiduYunDownload\2 dx dy的意思  微分的定义  导数符号的意思\dx dy的意思  微分的定义  导数符号的意思.flv"  -vcodec copy  -af "volume=2"  louder_file.flv



If we want our volume to be half of the input volume:

ffmpeg -i input.wav -filter:a "volume=0.5" output.wav


150% of current volume:

ffmpeg -i input.wav -filter:a "volume=1.5" output.wav

https://trac.ffmpeg.org/wiki/AudioVolume