# OHAMA-PIOS Open Source Project
Welcome to this project!
We are students with University of Agder, taking IT and Information Systems degree program. The reason to do this project is related to one of the subject called "IS-213 Open Source software" where we are required to do the practical work regarding Open Source. The aim of this project is to look into how Open Source project can be made and how it works in real life.

<h2>#Introduction</h2><br>
OHAMA PIOS project will cover different fields within Open Source. We have a plan to handle some challenges that have relations with everyday events and people need to know like temperature, humidity, sound pollution and air quality. Because of these challenges, we are going to measure such events regarding the atmosphere around us by special sensors within Open Source.<br><br>

<h2>#Requirements</h2>

Hardware:
  * <a href="https://www.raspberrypi.org/products/raspberry-pi-3-model-b/">Raspberry Pi 3</a>
  * <a href="https://www.raspberrypi.org/products/sense-hat/">SenseHat </a>
  * Dust particle sensor (more info to come)
  * Humidity Sensor
  * Temperature sensor
  * Sound sensor (dB monitoring)
  * Brightness sensor
  * Hazardous Gas 

Software: 
  * <a href="https://www.raspberrypi.org/downloads/raspbian/">Raspbian</a>
  * <a href="https://www.python.org/downloads/release/python-372/">Python 3.7</a>
  * <a href="https://github.com/plotly">Plotly</a>
  * <a href="https://plot.ly/products/dash/">Dash by plotly</a> 
  
![Graph](../master/image/Graph-v-1.01.PNG)

<h1>#Contributing</h1>
In this part we will cover how to contribute towards the project and the standard methodology used. Changes should manily be pushed to a branch, this can be overruled in situations when pair-evaluation is done. 

<h3>- Summary</h3>
<ol>
 <li>Draft the contribution.</li>
 <li>Review the contribution to follow the standard.</li>
 <li>Push the work to a development branch.</li>
 <li>Make a pull request from the branch to master for having a evaluation by another contributer.</li>
</ol> 

<h3>- Branches</h3>
In this repository there are two different types of branches:
<ol>
 <li>Master</li>
 <li>Issue / development branches</li>
</ol>

<h3>- Standards</h3>
The team has set some standards (these are guidelines) we expect to be followed when contributing towards the project. These standards should be followed when reviewing a pull request before merging a branch into master.

<h4> -- Code standards</h4>
  These standards should be considered when coding.<br>
  <ul>
  <li> Classes, methodes, functions and variables should have a descriptive name.</li>
  <li> Document what the different parts of the code does.</li>
  <li> Focus on high cohesion while limiting the coupling to a minium.</li>
  <li> Try to have as little code duplication as possible.</li>
  <ul>
