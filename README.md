# Singing Loud Flowers
## Overview
This project is inspired by the public art work ["Sonic Bloom" by Dan Corson](https://www.smithsonianmag.com/science-nature/sonic-bloom-a-new-solar-powered-sculpture-8992622/) and [John Cage's Prepared Piano](https://en.wikipedia.org/wiki/Works_for_prepared_piano_by_John_Cage). 
The Seattle Center-based sculpture is very large scale, and flower has a motion sensor of some kind, and a speaker that, when triggered, hums a tone. Each flower has a different tone and only with a group of people can the whole chorus of sound be heard. 

In my case, I wanted to simulate the motion-sensor-as-trigger for sound for a very long time, capturing the same sensibility of requiring people to come together to create the whole experience. 

## Setup for Singing Loud Flowers IoT Project
### Requirements
For this project, I'm using Raspberry Pi Zero 2 Ws as MQTT brokers, publishers, and subscribers, and for GPIO on the motion sensor. Because of the low power and RAM available for RPi Zero 2 W, I'm using Raspberry Pi OS Lite (Legacy, 64-bit) at Debian Bullseye. 

Raspberry Pis all need to be on the same network. 

Each Pi needs to have SSH enabled and ssh keys setup to the host / control client that is running Ansible scripts. I use `ssh-copy-id <username>@<remote-IP> to ensure that subsequent ssh logins do not require passwords. This helps Ansible run without hard-coding or otherwise storing secrets on the user's local machine, but those are certainly options. Use secure methods of storing passwords, and do not post passwords to your forks!

### Running Configurations with Ansible
Since my intention is to have the ability to scale the project with additional Raspberry Pis as I get them, I wanted to have a single configuration workflow to set them up. 

After your Raspberry Pis are online and you have successfully ssh'ed into them and managed password handling (i.e., `ssh-copy-id` above), Ansible can be configured to apply the same updates and setup to each of the Pis. 

In my case, I have each Pi as an individual group, and a collection of those Pis in another named group. Update your IP address or Hostnames in the `inventory.ini` file. 

Additionally, the playbook yamls will need to point to the intended device or group. Update those manually. 
