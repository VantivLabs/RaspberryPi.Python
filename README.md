# RaspberryPi.Python

#Overview

This repository will provide information about the Raspberry Pi specifically for those that are going to accept the Vantiv API challenge at Money20/20.  There will be some interesting challenges with these hardware components but we believe without challenge there is no reward.  Check out these repositories for code to get you jumpstarted.

Infrastructure in the financial world is mind numbing, and detecting issues quickly is a high priority for platform teams.  What if we could send each one of the merchants, or financial institutions, a cheap device that would help us detect processing issues before they happened?  Enter the Raspberry Pi!

This code is going to integrate to the Vantiv platform, using the Mercury SOAP API, and periodically send a transaction.  The code will then run some quick analysis on the results and flash a green or red LED based on that analysis.  As you will see the analysis is trivial in the code, but this is a small step to what could be an actual product.  Think about the ability to have a low cost processing platform within each merchant environment...the opportunity is vast!

You might notice that there is both a Python repository and a C# repository (https://github.com/VantivLabs/RaspberryPi.CSharp).  Both will perform the same work, but this repository is built on top of the Raspbian OS while the C# code is built on top of Windows IoT.  Arguments can be made for which one is better but the resulting conclusion will be different for everyone.  The good news is that there is sample code for both so you get a jumpstart regardless of which option you choose.

We will not add images to this repo, mainly because that would be redundant, which makes for a slightly more boring repo, but if you want to see the images head on over to the C# repo!


#Unboxing

Each team (limited to the first ten teams) that is interested in accepting the Raspberry Pi Vantiv challenge will receive this kit: http://www.canakit.com/raspberry-pi-starter-ultimate-kit.html.

Please see the corresponding entry in the C# repository for more:  https://github.com/VantivLabs/RaspberryPi.CSharp#unboxing-the-raspberry-pi

#Setup

Please see the corresponding entry in the C# repository:  https://github.com/VantivLabs/RaspberryPi.CSharp#setup

The first time the device boots up you will need to configure the WiFi USB dongle.  As mentioned in the C# repository, Windows IoT only works with the Raspberry Pi WiFi dongle, but Raspbian will work with the WiFi dongle that is shipped in the CanaKit, so you're in luck if you choose the Raspbian build because it will work out of the box. Initially you will need to  boot with the USB keyboard/mouse and HDMI cable so that you can setup the wireless. Login to the Raspberry Pi, run startx which will boot the graphical UI, and then configure the wireless.  The CanaKit quickstart guide provides all of the necessary information.  After that setup is complete you can use any SSH utility (PUTTY from windows) to access the Raspberry Pi.

When you are logged in, working with the Pi is mostly the same as working with any other Linux variant.

#Writing Code

There are two files in the repo:

* Mercury.py -- this provides a Mercury class that will connect and send a transaction to the Mercury REST endpoint.  Nothing too exciting about this.  Most of the attributes of the json use hard coded values which are pefect for this type of application.  In other words, we're not actually trying to send a payment transaction, but we're testing the entry points to validate that they are working.

* dowork.py -- this sets up the hardware to function correctly, calls the Mercury class to send a transaction, and performs the analytics to decide which LED to flash.  Again this is a simple script that allows many 'jumping off' points for further functionality.

As with C#, this is not the most elegant code but it gets the job done.  There are two functions that flash the LEDs, then a for-loop is entered that times a transaction to the platform and then, based on the outcome of that transaction, will flash the red or green LED.

There certainly seems to be less code written for Python vs. C# version but that might simply be based on lack of refactoring.  Additionally the Python code (or Raspbian itself) performs better than the code written on Windows IoT.  Again that is a simple observation and might be comparing apples to oranges, but please feel free to run both and provide feedback.   If there is anything we love more than hacking with hardware, it's hacking with hardware with hundreds of our friends!

#Hardware

Not much was mentioned above about the hardware but it should be straightforward to setup the two LEDs, two resistors, and wires following the pictures.  If the pictures are not good enough have a look at the tutorials below in 'Useful Links'.

#Good Things to Know

Please see the corresponding entry in the c# repository:  https://github.com/VantivLabs/RaspberryPi.CSharp#good-things-to-know

#Useful Links

https://github.com/InitialState/piot-101/wiki -- great tutorial on getting everything up and running, it applies even more to Raspbian than Windows IoT so we will make an exception and list this one twice.

#Other Cool Things

Please see the corresponding entry in the c# repository:  https://github.com/VantivLabs/RaspberryPi.CSharp#other-cool-things
