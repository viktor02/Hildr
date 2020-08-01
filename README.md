# GTracker

GTracker is a tracker of your time spent playing games.

### How its work

GTracker checks if a process from the list is running, 
and if it finds one, it records the time.

### How to install?

1. Install requirements
```
python3 -m pip install -r requirements.txt
```
2. Add the main binary file of your game to the `games.txt`
3. Run program `python3 main.py`

#### I have Windows, what to do
Ready to run executables [here](https://github.com/viktor02/GTracker/releases/latest)

#### How to build with cx_freeze
Install cx_freeze, run `python setup.py build`