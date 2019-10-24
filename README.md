## Intrusion Detection System
This project helps reduce the threat of people peeking into device while the owner is not around. 
Employing push-bullet to send a verification message to the mobile number of the owner requesting authentication, this project is aimed at catering to its users the security of their devices, alongside a mechanism to identify the miscreant who tried to use the computer while he wasn’t around.
The basic way this product works is that an authentication message is sent to the registered phone number using push-bullet requesting verification from the owner. The intervals when this verification message is sent can be modified by the user. Now, there are two scenarios that could happen. First, the owner is using the laptop at that time, and he verifies it. The program does nothing more and waits to resend the verification message after the predefined period of time.
Second and the crucial scenario is when at receiving the verification message the owner doesn’t reply in affirmative. When this happens a snapshot of the person using the computer is clicked through the webcam and sent to the owner via push-bullet.
Also after sending the image to the owner computer will be locked automatically.

![screenshot from 2018-05-06 13-41-18](https://user-images.githubusercontent.com/31770961/39677404-d3686cfc-5197-11e8-86e6-65055fff67e8.png)

## Requirements
- Internet Connectivity
- Pushbullet Access tokens - Open pushbullet account on "pushbullet.com"
	- Click on Settings in left tab.
	- In Accounts (scroll down) and click on "Create Access Token."
	- Copy this key and paste when asked during execution.

## Used Module
- cv2
- socket
- tkinter
- pushbullet
