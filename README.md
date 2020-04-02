# ABB-Robot-with-python-socket
# Controlling abb robot via socket in python - Simulation in ABB-RobotStudio

STEP 1: Copy the code in ".txt " file and paste it in the sketch of Abb-RobotStudio Rapid Editor.
STEP 2: click on apply icon and then click  check program, if error(Underlined with red) is there then debug it.
STEP 3: Go to simualtion then click on Play.
STEP 4: Check the output("program started ").
STEP 5: Now run the python file.
STEP 6: enter inputs as asked by the python script.

# WHAT to do if there is   "socket error"

STEP 1: Find the IPv4 address of your computer for socket connection.  go to run(Win+R)-> cmd -> then type "ipconfig".
STEP 2: Copy the Ipv4 address  and replace the ipv4 address in the rapid script in Robotstudio and python script. (ip adress must bt same in both the file).

# WHAT to do if there is  "robot  error"

STEP 1: connect your abb robot and go to controller tab.
STEP 2: click on add controller and then click on one click connect.
STEP 3: click on "request  write access".
STEP 4: click on "Go offline" on the right most side of options.
STEP 5: disconnectr you robot if you want to work in simulation.
