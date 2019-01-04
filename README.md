# Intrusion-Detection-System
It is a GUI of a python program which will send a notification to the host's mobile using Pushbullet API in every one hour, which will test whether the person using laptop is the host or not. If test fails i.e., if answer came 'No' from the host's mobile, program will click a photo of intruder and send it to host's mobile and lock the system.

![screenshot from 2018-05-06 13-41-18](https://user-images.githubusercontent.com/31770961/39677404-d3686cfc-5197-11e8-86e6-65055fff67e8.png)


### Special Cases:-
If host don't reply for 10 notifications(each in a interval of 1 Mins), system will lock automatically.

### Requirements:-
- Internet Connectivity
- Pushbullet Access tokens - Open pushbullet account on "pushbullet.com"
	- Click on Settings in left tab.
	- In Accounts (scroll down) and click on "Create Access Token."
	- Copy this key and paste when asked during execution.

### Used Module:-
- os - Used to lock the system.
- cv2 - Used to click picture.
- time - For Scheduling.
- socket - To check internet connectivity.
- platform - To get system characterstics.
- tkinter - Making GUI 
- pushbullet - API to send notification and image.
- ctypes - Lock windows system.

### Screenshot:-
![screenshot_20180507-011617](https://user-images.githubusercontent.com/31770961/39677412-e3a1cd0c-5197-11e8-96b2-a7d43c7975ab.png)

### Note:- It may not work with proxy internet.
