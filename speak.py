import pyttsx3

robot_brain = "I will speak this text"

robot_mounth = pyttsx3.init()
robot_mounth.say(robot_brain)
robot_mounth.runAndWait()
