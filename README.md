# Singing Loud Flowers
## Overview
This project is inspired by the public art work ["Sonic Bloom" by Dan Corson](https://www.smithsonianmag.com/science-nature/sonic-bloom-a-new-solar-powered-sculpture-8992622/) and [John Cage's Prepared Piano](https://en.wikipedia.org/wiki/Works_for_prepared_piano_by_John_Cage). 
The Seattle Center-based sculpture is very large scale, and flower has a motion sensor of some kind, and a speaker that, when triggered, hums a tone. Each flower has a different tone and only with a group of people can the whole chorus of sound be heard. 

In my case, I wanted to simulate the motion-sensor-as-trigger for sound for a very long time, capturing the same sensibility of requiring people to come together to create the whole experience. 

## Setup for Singing Loud Flowers IoT Project
### Requirements
For this project, I'm using Raspberry Pi Zero 2 Ws as MQTT brokers, publishers, and subscribers, and for GPIO on the motion sensor. Because of the low power and RAM available for RPi Zero 2 W, I'm using Raspberry Pi OS Lite (Legacy, 64-bit) at Debian Bullseye. 


