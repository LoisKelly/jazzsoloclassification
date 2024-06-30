# Extracting Influences: Audio Classification of Jazz Solos


This project is the exploration of using convolutional neural network processes within machine learning models to classify instrumental Jazz solos by artist. The aim of this project was to take Jazz solos and see if an AI model could identify who the soloist may be influenced by. 
It explores two approaches to audio classification, one using raw WAV files in a CNN nework and another using image classificaiton by training a CNN on spectogram images made from the audio files. 

### Notebooks:
Pre-Processing data - This notebook processes the data, including converting MIDI files to WAV, sorting files by artist, splitting the data into smaller chunks and creating spectograms. 
WAV CNN Classifier - Using code from Week 6 AI for Media, this notebook includes the code for a CNN classifier model for raw WAV files. 
Spectograms Classifier - This notebook is adapted from https://github.com/jeffprosise/Deep-Learning/blob/master/Audio%20Classification%20(CNN).ipynb. It includes the code for an image classifier that is used to classify the audio. 

### Installation
All necessary imports are at the top of each notebook. 

### Credits:
- https://github.com/JinayJain/timidity
- https://stackoverflow.com/questions/60105626/split-audio-on-timestamps-librosa 
- https://jazzomat.hfm-weimar.de/dbformat/dbcontent.html
- https://stackoverflow.com/questions/10989005/do-i-understand-os-walk-right
- https://github.com/JinayJain/timidity 


### LLM Disclaimer 
Throughout this work LLMs have been used for help with working through errors, explanation of code/processes and occasionally for writing code. It has been cited where LLM code has been used. 
