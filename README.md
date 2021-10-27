# MOVIEPY and FFMPEG to Extract Audio and Merge with Another Video

Let's assume you have:
- Video A with Audio A
- Video B with Audio B


The final video we want to create should be: *Video A* + **Audio B**


## Potential Use
In some recordings (lectures) there are 2 files, the Webcam Video has the lecturers voice, and the screen recording has nothing. Because you cannot listen to both files at the same time, merging them is important

## Assumptions
1) Both video files are the same length (time)
2) Packages required are installed

## Is FFMPEG Necessary?
Not really, but MOVIEPY has never rendered audio in any of my projects. If you manage to make it work, please feel free to contribute to this repo
