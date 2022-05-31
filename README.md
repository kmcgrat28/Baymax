# Baymax
Baymax robot
## Executive Summary
### Students cannot inventory their bodies individually and on their own time unless they go to the nurse, which could be stressful given the pandemic. Our solution? Baymax! He is cute, convenient, and comforting; further, a “real-life Baymax” could be a good tool for pediatric hospitals around the country, soothing scared children and easing processes for doctors. 
# Introduction/Background
## Let’s make a Pixar robot (again)! To ensure that we have a few basic goals in place, I propose:
a miniature Baymax robot w/ an LCD screen installed in his midriff
temperature sensor in his hand + heart rate monitor somehow incorporated
temperature + heart rate are displayed on the screen
If time and capabilities allow, I’d like to incorporate: 
antibacterial finger spray 
Baymax’s voice

## Project Management
KATHERINE: DESIGN
Baymax internal structure
KAYMIN: CODE
LCD screen depicting heart rate and body temperature
Temperature sensor
Heart rate monitor
MILESTONES:
Sketch design + complete drafts (KM) -- start working with temperature sensor + heart rate monitor (KH)
sketch design (1 day)
complete drafts (7 days)
finish temperature sensor (7 days)
finish heart rate monitor (7 days)
Finish design + execute (KM) -- combine temperature sensor + heart rate monitor code + add LCD screen (KH)
finish design (7 days)
execute design (7 days)
combine temp + heart code (7 days)
add LCD screen (7 days)
Finish + document the project (7 days)
Next steps...TBD

## Materials: 
Baymax 12’ stuffed toy, Raspberry Pi, heart rate monitor, LCD screen, temperature sensor

Hopefully, this project will serve as a convenient and discreet way for a student to inventory their wellness at the moment without disrupting their day. 
We chose Baymax because we wanted to do another Disney/Pixar character. Further, we wanted a chance to utilize the new MedTech materials. He is cuddly and friendly and all around adorable. As much as we think that this could be helpful, though the small project, it’s more for fun than anything else. We’re not looking to innovate (yet...we’ll see where the potential second project takes us), but to simply do something that can make a little bit of a difference. We may add more later once we have a better idea of potential time constraints and how long each task will take us. We’re starting with a simple design and simple functions that we can always build on later.

## Overview of Products
We intend to source our technology from Open BCI, an open source organization dedicated to “creating low-cost, high-quality biosensing hardware for brain computer interfacing.” Partnered with organizations such as Columbia Engineering and the MIT Media Lab, Open BCI is a credible organization whose materials will deliver a seamless product. 

Channels dictate the amount of data that can be processed at once by a board. 
ECG (heart rate monitoring) uses 1- 4 channels, with more channels enabling the collection of more accurate data.

## Mechatronics: 
 Raspberry Pi! The inputs will be the information taken in by the sensors and the output will be the display on the LCD screen. 
## Budget
Raspberry pi - already have
LCD - already have
Baymax stuffed animal - $20-30
Wires - already have
 Open BCI heart rate monitor - already have
Temperature sensor - already have 
Extra/unnamed supplies (estimate) - $30
* analog-to-digital converter
MAX TOTAL PRICE - $60

## Impact
Find a teenager who is perfectly in tune with their body. They exist, but they’re rare. Having a stopgap measure to ensure that physical wellness (as depicted by body temperature) and mental wellness (as depicted by heart rate monitor; if it’s too high, maybe the student is feeling anxious or ill) are where they need to be is important, especially with COVID making health anxiety high. Further, it isn’t as disruptive to a student’s day and can help them decide if they need further care, be it at the nurse’s office or home. 
This project could also be used in children’s hospitals, a comforting presence during what we’re sure is a terrifying time. Ideally, it would serve to facilitate the ease with which doctors do their jobs and ensure that the patient feels comfortable and safe. 

## Deliverables
Our final product is going to be a finished and functioning medical robot. He will have temperature sensors in one of his hands and your temperature will be displayed on the LCD screen attached to his stomach. We will use GitHub to document our process and progress. We also aim to make him easy to sanitize, to ensure that we don’t contribute to the spread of COVID.

### What are we going to turn in? 
Design drawings - Katherine is our resident designer, and she’ll likely submit paper drawings and many Onshape drafts. 
Photos and video - We’ll submit pictures and videos of each of our successful individual components and later, the working robot as a whole. 
Test procedures - All tests and prototypes will be photographed and posted on our GitHub repository with documentation specifying what was changed after the previous test and what we’re planning to change after the current one.
Commented code - Kaymin will be handling the coding aspect, and she’ll turn in commented code. She’ll also document her process on GitHub, noting what was difficult and what she did to fix it. 
Circuit diagrams - We will make fritzing diagrams of all of our wiring and upload them to GitHub with any notes we may have. 
Operating instructions - We can include operating instructions in our finished GitHub repository. 
Materials and resource requirements


## Coding Progress:
### Heartrate Sensor & LCD Screen
The heartrate sensor provides the BPM, which is then printed on the LCD screen (alongside a fun Baymax quote!). If no heartrate is detected, the text on the screen will change to reflect that. 
'''
if bpm > 0: 
		draw.text((x, top),	'Hello. I am Baymax,', font=font, fill=255)
		draw.text((x, top+10),	'your personal', font=font, fill=255)
		draw.text((x, top+20),	'healthcare companion.', font=font, fill=255)
		draw.text((x, top+30),	'Your heartrate is', font=font, fill=255)
		draw.text((x, top+40),	str(int(bpm)), font=font, fill=255)
		disp.image(image)
		disp.display()
		time.sleep(2)
		draw.rectangle((0,0,width,height), outline=0, fill=0)

	else:
		draw.text((x, top),	'No heartbeat found', font=font, fill=255)
		disp.image(image)
		disp.display()
		time.sleep(2)
		draw.rectangle((0,0,width,height), outline=0, fill=0)
		time.sleep(2)
'''

At first, I had some issues with the heartrate sensor actually reading the values. It turns out that this problem was likely due to a hardware issue: the sensors are very sensitive and even pushing on both sides of the sensor can overload and damage it. Once we got the new one, it worked like a charm. I first printed the values in terminal by writing: 
'''
bpm = p.BPM
print(bpm)
'''
The BPM printed in terminal without a problem. However, some issues did arise when I tried to put it on the LCD screen with this code:
'''
draw.text((x, top+40),	bpm, font=font, fill=255)
'''

However, though the screen would print "No heartbeat found" if that was the case, I'd get an error whenever it did pick up on a reading. Mr. Miller suggested that the problem might be with the fact that there are an infinite number of decimals in each reading and the LCD screen didn't know how many to print. So, we changed it to
'''
draw.text((x, top+40),	int(bpm), font=font, fill=255)
'''

This didn't work, so we switched int with str, and the values started to print on the screen. However, there were still a lot of decimal values and for aesthetic purposes, we preferred an integer. So, we added the following line and it worked perfectly! 
'''
draw.text((x, top+40),	str(int(bpm)), font=font, fill=255)
'''

### Servos
The servos are responsible for moving Baymax's arms. They are continuous rotation servos and move to 90 degrees when the code is initialized; when it stops running, the servos go back down to their original position. 

'''
while True:
	
	servoleft.mid()
	servoright.mid()
	time.sleep(3)
'''

The servos were extremely easy to set up in the test code, but I hit a small hurdle when attempting to integrate this aspect into the main document. First, I put the servo instructions inside the if statement; when that didn't work, I tried putting it before the while True loop, which also failed. I found that the only way that they'd react properly was if I put it before the if statement but still inside the while True loop. 

## CAD Progress:
#### Arm configuration:
##### 4in arm
![Arm 4in](https://github.com/kmcgrat28/Baymax/blob/main/Capture%20arm%204in.PNG)
##### 5in arm
![Arm 5in](https://github.com/kmcgrat28/Baymax/blob/main/arm%20photo.PNG)
##### 6in arm
![Arm 6in](https://github.com/kmcgrat28/Baymax/blob/main/Capture%20arm%206in.PNG)\
##### Basic servo holder: I did make this a bit bulkier than usual to try and protect the servo from stuffing.
![servo holder](https://github.com/kmcgrat28/Baymax/blob/main/servo%20holder%20photo.PNG)\
##### ball to attach the socket and leg to
![Socket](https://github.com/kmcgrat28/Baymax/blob/main/ball%20to%20socket.PNG)
##### Socketand leg to attach to the ball
![Leg](https://github.com/kmcgrat28/Baymax/blob/main/Capture%20leg%20bottom.PNG)
##### First print if the leg
###### The first print of the leg worked, it could snap on and move around but it was very tight and had too much pressure on it. ultimately, taking it on and causing it to break due to the thickness of the plastic and not having enough give.
![arm printed out](https://github.com/kmcgrat28/Baymax/blob/main/IMG_0006.jpg)
##### Second print if the leg
###### I thought making the plastic thinner would give us a less tight fit but still have the stability and height we needed. In reality, it just caused the whole thing to be weaker, and this model broke too.
![IMG_0008](https://user-images.githubusercontent.com/56269212/167702076-ecc34eeb-b6b0-477a-92f6-b0b509e83e39.jpg)
##### Final print of the leg (hopefully)
###### For this model I made the plastic thicker again so it would have its strength back but I lowered the top and the ellipse in the sketch so it would need less give to be attached but would still have some without adding too much pressure and breaking it.
#### The skeleton printed and assembled
![IMG_0009](https://user-images.githubusercontent.com/56269212/167702094-0897fcb4-2de7-46b7-a599-a2f371511a85.jpg)
#### The assembly coming together!!
##### this is most of the main parts getting put together, the main center, the base, the arms, the servo-holders, the servos, and the balls for the legs.
![IMG_0010](https://user-images.githubusercontent.com/56269212/167702066-11decdeb-42a0-4c56-bfa1-1d0b567312c1.jpg)

