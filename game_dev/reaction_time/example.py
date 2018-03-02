import pygame, sys, time, xlwt, os, os.path
from pygame.locals import *

#Test Intervals
test1 = [0,7,3,9,19,8]
test2 = [4,14,11,3,2,6]

#Storage Lists
listk = []
lists = []
liste = []

#frames per second setting
FPS = 30
fpsClock = pygame.time.Clock()

#Display
side = "Left"
#side = "Right"

#Record ocular dominance
input_dominance = raw_input("Dominant Eye (L/R): ").lower()

if input_dominance == "l":
    dominance = "Left"
elif input_dominance == "r":
    dominance = "Right"

#Choose test
input_test = raw_input("Test (1-2): ")
if input_test == "1":
    intervallist = test1
elif input_test == "2":
    intervallist = test2

pygame.init()

#Set up window
pygame.event.set_grab(1)
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode((1280,800),FULLSCREEN)
shape = screen.convert_alpha()
pygame.display.set_caption("Visual Reaction Time Test (Left)")

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)

#Stimuli
stimulusl = pygame.Rect(100,350,100,100)
stimulusr = pygame.Rect(1080,350,100,100)

#Side of display for stimuli
stimulus = stimulusl
#stimulus = stimulusr

def start(number):
    """Starting sequence"""
    #Create a font
    font = pygame.font.Font(None,200)

    #Render the text
    text = font.render(str(number), True, WHITE)

    #Create a rectangle
    textRect = text.get_rect()

    #Center the rectangle
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    #Blit the text
    screen.blit(text, textRect)
    pygame.display.update()

    #Pause for 1s
    time.sleep(1)

    #Clear screen
    screen.fill(BLACK)
    pygame.display.update()
    

    
def flash(interval):
    """Flashes stimulus"""
    #Keypress flag
    k = 0
    #Draw on surface object
    time.sleep(interval)
    screen.fill(BLACK)
    pygame.event.clear()
    pygame.draw.rect(screen,WHITE,stimulus)
    pygame.display.update(stimulus)
    t0=time.clock()
    lists.append(t0)
    k = 1

    #Pauses for 1.5s
    while time.clock()-t0 <1.5: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if k == 1:
                    listk.append(time.clock())
                    k += 1

    #Clears screen
    pygame.draw.rect(screen,BLACK,stimulus)
    pygame.display.update(stimulus)

def fade(interval):
    """Fades in stimulus"""
    #Keypress flag
    k = 0
    time.sleep(interval)
    screen.fill(BLACK)
    pygame.event.clear()
    DURATION = 2.0 # seconds
    t0 = time.clock()
    ratio = 0.0 # alpha as a float [0.0 .. 1.0]
    t0=time.clock()
    
    lists.append(t0)
    k = 1
    while ratio < 1.0:
        current_time = time.clock()
        ratio = (current_time - t0) / DURATION
        if ratio > 1.0: # In case it's a bit late
            ratio = 1.0
        
        screen.fill(BLACK)
        shape.fill(BLACK)
        alpha = 255 * ratio
        #Draw on surface object       
        pygame.draw.rect(shape,(255, 255, 255,alpha),stimulus)
        #screen.set_alpha(128)
        screen.blit(shape,(0,0))
        pygame.display.update(stimulus)
        fpsClock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if k == 1:
                    listk.append(time.clock())
                    k += 1

    #Pauses for 1.5s
    while time.clock()-t0 <3: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if k == 1:
                    listk.append(time.clock())
                    k += 1

    #Clears screen
    pygame.draw.rect(screen,BLACK,stimulus)
    pygame.display.update(stimulus)
    
def display_end():
    """Display 'End'"""
    #Create a font
    font = pygame.font.Font(None,200)

    #Render the text
    text = font.render("END", True, WHITE)

    #Create a rectangle
    textRect = text.get_rect()

    #Center the rectangle
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    #Blit the text
    screen.blit(text, textRect)
    pygame.display.update()

#Call function to initiate start sequence
for i in reversed(range(1,4)):
    start(i)

#Pause for 2s
time.sleep(2)

time.clock()

#Call fade or flash function to present stimuli with intervals
flash(intervallist[0])
flash(intervallist[1])
flash(intervallist[2])
fade(intervallist[3])
fade(intervallist[4])
fade(intervallist[5])

#Pause for 3s
time.sleep(3)

#Call function to display end
if input_test == "1":
    display_end()
else:
    time.sleep(3)

#Pause for 1s
time.sleep(1)

def spreadsheet():
    """Write data to spreadsheet .xls"""
    #Prepare spreadsheet
    book = xlwt.Workbook(encoding="utf-8")
    data = book.add_sheet("Data")

    #Write header
    data.write(0, 0, "Display")
    data.write(1, 0, "Dominance")
    data.write(2, 0, "Test")

    data.write(0, 1, side)
    data.write(1, 1, dominance)
    data.write(2, 1, input_test)

    #Write data
    data.write(4, 1, "Stimulus Time")
    data.write(4, 2, "Reaction Time")
    data.write(4, 3, "Time Elapsed")

    i=4
    j=4
    k=4

    for n in lists:
        i = i+1
        data.write(i, 1, n)

    for n in listk:
        j = j+1
        data.write(j, 2, n)

    #Calculate and record time elapsed
    for n in listk:
        #liste.append(list
        k = k + 1
        formula = "C{}-B{}".format(k+1,k+1)
        data.write(k, 3, xlwt.Formula(formula))

    #Temp "flash" & "fade"
    data.write(5, 0, "Flash")
    data.write(6, 0, "Flash")
    data.write(7, 0, "Flash")
    data.write(8, 0, "Fade")
    data.write(9, 0, "Fade")
    data.write(10, 0, "Fade")

    #Determine filename
    TARGET_DIR = 'data/'
    n = sum(1 for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f)))
    filename = "{}Trial_{}_{}.xls".format(TARGET_DIR,n+1,side[0])

    #Write file
    book.save(filename)

#Call function to write to spreadsheet
spreadsheet()
    
#Exit
pygame.quit()
sys.exit()

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()