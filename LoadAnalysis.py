#LoadAnalysis will read the storage parsed by CompleteLevel and produce a graphic dashboard to show analysis
from xmlrpc.client import FastParser
import pygame
import sys
import matplotlib.pyplot as plt
from sqlalchemy import false
import matplotlib.pyplot as plt



pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 20)

class Button():
    
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            		    # importing the required module

						# x axis values
						x = ["Easy","Medium","Hard","Expert"]
						# corresponding y axis values
						y = [2,4,1,5]
  
						# plotting the points 
						plt.plot(x, y)
  
						# naming the x axis
						plt.xlabel('Difficulty')
						# naming the y axis
						plt.ylabel('Time taken in Minutes')
  
						# giving a title to my graph
						plt.title('Sudoku Analytic Report') 
						# function to show the plot
						plt.show()
						print("Analytic Report Generated!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (250, 100))

button = Button(button_surface, 200, 340, "Generate Analytic Report")

action = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())

	screen.fill("white")

	button.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()