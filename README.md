# Cambridge Bumps Simulator

Fully interactive, visual simulator for the Cambridge University's [May Bumps races](https://www.cucbc.org/bumps), built with Python and Tkinter.

Running the script with Python (instructions below) will load a graphical user interface which displays the Mays 2025 start order, finishing order, and lines tracking each crew's performance. 

The user can input results and dynamically visualise changes across the four days of racing. This is done by selecting the bump type, and then clicking on the row of which crew is to bump up within that day's column. A highlighting function visualises which crews will be swapped whenever the cursor hovers over a crew.

<img width="1512" alt="image" src="https://github.com/user-attachments/assets/b3843768-c413-453f-8aff-e3db69b17b8b" />


## How to use

The prerequisites are simple: **Python 3** and a device to run it on
(if you do not have Python, it can easily be installed [here](https://www.python.org/downloads/))

No other dependencies are required.

**It is simple to download and load the simulator:**

1. download the 'cambridge_bumps_simulator.py' file from this repository
2. open a terminal, and ensure you are at the location where that file is stored on your computer
3. type `python bumps_simulator.py` and click enter
4. the simulator now should load

    
There are buttons to select either the men's or women's divisions, to select which bump type to input, to undo the last input, or to reset the simulator
Again, results are input by clicking on the row of the crew to bump, within a specific day's column. The crews to be swapped will be highlighted.
Behaviour of bumps obeys distinct divisions, with only the sandwich boat being able to move between these each day. The crew which finishes a lower division as sandwich boat in one day will then have the possibility for a second race, where they can now move upwards.

Full details on the

