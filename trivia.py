import random
import csv

class Trivia:
  def __init__ (self, question, answer):
    self.question = question
    self.answer = answer

  @classmethod
  def randomize (cls, keys):
    chosenQ = random.choice(keys)
    return chosenQ