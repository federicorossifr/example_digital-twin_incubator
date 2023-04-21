# The Incubator Digital Twin

This is a case study of an Incubator with the purpose of understanding the steps and processes involved in developing a digital twin system.
This incubator is an insulated container with the ability to keep a temperature and heat, but not cool.

To understand what a digital twin is, we recommend you read the following paper:
Feng, Hao, Cláudio Gomes, Casper Thule, Kenneth Lausdahl, Alexandros Iosifidis, and Peter Gorm Larsen. “Introduction to Digital Twin Engineering.” In 2021 Annual Modeling and Simulation Conference (ANNSIM), 1–12. Fairfax, VA, USA: IEEE, 2021. https://doi.org/10.23919/ANNSIM52504.2021.9552135.

## The Incubator Physical Twin

The overall purpose of the system is to reach a certain temperature within a box and keep the temperature regardless of content.
![Incubator](figures/system.png)

The system consists of:

- A Styrofoam box in order to have an insulated container.

- A heat source to heat up the content within the Styrofoam box.

- A fan to distribute the heating within the box

- A temperature sensor to monitor the temperature within the box

- A temperature Sensor to monitor the temperature outside the box

- A controller to communicate with the digital twin, actuate the heat source and the fan and read sensory information from the temperature sensors.

## The Digital Twin

The DT does the following:

1. Continuously monitor the assumptions made about the system and its model. This is essential for safety and a pre-condition to everything else. For instance: the uniform temperature assumption should hold whenever the fan is operating and the heating is turned off. This is a basic assumption that we make when answering what if questions. If that does not hold, it might mean the fan has stopped working.

2. Continuously compare the system behavior with the predictions of the models. E.g., when the heating element is turned on for 5 seconds, the temperature should reach 35 degrees within the next 30 seconds and then slowly go down to 25 degrees within 5 minutes.

3. Re-calibrate when 2 no longer holds (in this case, finds the new parameter for the element being warmed inside, for example, a glass of water).

4. Possibly re-tunes the controller to optimize the behavior under the newly calibrated model. E.g., instead of turning the heating element for 5 seconds, it now only turns it for 3 seconds, to reach the same 35 degrees within the next 30 seconds.

5. Answers what-if questions: Suppose you want to turn off the heating element for some hours (maybe due to power loss or some other intervention). Is there anything that you can do to keep the temperature inside the box within range? Maybe place a bottle of hot water? If so, how warm must the water be?

## First time setup and run framework

Follow the instructions in [software/README.md](software/README.md)

## More Documentation

You can find more documentation here: [docs/_build/html/index.html](docs/_build/html/index.html)

## Repository Maintenance Instructions

General guidelines (instructions are in the following subsections)

1. Run the tests as often as possible.
2. Create tests as much as possible.
3. Ask for code reviews (code readable by at least two people is more likely readable by a third)
4. Organize and document your datasets, and experiments: use the sphinx documents for this.
5. Beware of large datasets.
6. Don't be afraid of reorganizing the code and repo if you think that's necessary. This is an ongoing learning process for everyone. Discuss with Casper, Kenneth, or Claudio before doing so if you're not sure.
7. Much more on https://github.com/HugoMatilla/The-Pragmatic-Programmer


