import sys, random, csv, pygame
from trivia import Trivia
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

running = True

while running:
  for event in pygame.event.get():
    x = 0
    # def randomize(keys):
    #   chosenQ = random.choice(keys)
    #   return chosenQ
      
    qaList = []
    with open("questionsDatabase.csv", 'r') as file:
      csvReader = csv.reader(file)
      for row in csvReader:
        qa = Trivia(row[0], row[1])
        qaList.append(qa)

    while x < 3 and running:
      qaNew = Trivia.randomize(qaList)
      print("\n" + qaNew.question)
      answer = input()
      if answer.lower() == qaNew.answer.lower():
        print("Correct! Moving on...")
        running = False
      else:
        print("Incorrect")
        qaList.remove(qaNew);
        x += 1
    if x == 3:
      print("You ran out of tries.")
      running = False

    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
