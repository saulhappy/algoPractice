# -*- coding: utf-8 - *-


# Use the namedtuple function to create a GymExercise class whose instances
# will have three attributes: name, weight, and reps.

# Assign a squat variable to a GymExercise tuple object with
# a name of “squat”, a weight of 265, and a rep count of 3.

# Assign a bench variable to a GymExercise tuple object with
# a name of “benchpress”, a weight of 185, and a rep count of 5.

# Assign a deadlift variable to a GymExercise tuple object with
# a name of “deadlift”, a weight of 225, and a rep count of 6.

# Assign a press variable to a GymExercise tuple object with
# a name of “press”, a weight of 120, and a rep count of 8.

import collections

GymExercise = collections.namedtuple("GymExercise", "name, weight reps")

squat = GymExercise("squat", 265, 3)
bench = GymExercise("benchpress", 185, 5)
deadlift = GymExercise("deadlift", 225, 6)
press = GymExercise("press", 120, 8)
