# **************************** Challenge: Activities for Kids ****************************
"""
Author: Trinity Terry
pyrun: python activities-for-kids.py
"""

# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take varying number of children's names as the argument.
def run(*children):
    for child in children:
        print(f"{child} ran like a fool!")

def swing(*children):
    for child in children:
        print(f"{child} swang like a fool!")

def slide(*children):
    for child in children:
        print(f"{child} slid like a fool!")

def hide_and_seek(*children):
    for child in children:
        print(f"{child} hid like a fool!")


run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")