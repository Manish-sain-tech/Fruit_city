import random 
import pygame
pygame.init()
##########################################

display_width=330
display_height=480
win =pygame.display.set_mode((display_width,display_height))

font=pygame.font.SysFont('chiller',30)

pygame.display.set_caption("Fruit_juice")

#score and level
score=0
level=1
high_score=0
#loading characters


fruit_width=40
fruit_height=40

bucket_width=56
bucket_height=32
#fruit png
apple=pygame.transform.scale((pygame.image.load('apple1.png')),(fruit_width,fruit_height))
orange=pygame.transform.scale((pygame.image.load('orange2.png')),(fruit_width,fruit_height))
watermallon=pygame.transform.scale((pygame.image.load('watermallon.png')),(fruit_width,fruit_height))
mango=pygame.transform.scale((pygame.image.load('mango.png')),(fruit_width,fruit_height))
#background & bucket
bg=pygame.image.load('fruitcity.jpg')
fruitcity_intro=pygame.image.load('fruitcity_intro.jpg')
bucket=pygame.transform.scale((pygame.image.load('bucket.png')),(bucket_width,bucket_height))

#to fix fps
clock=pygame.time.Clock()
#win.blit(fruitcity_intro,(0,0))

#####################################################

#initial cordinate for bucket
x=155
y=330
#fruit_velocity
fruit_vel=0
bucket_vel=5
#init fruits
y_mango=random.randint(-70,-60)
x_mango=random.randint(fruit_width,330)-fruit_width 

y_apple=random.randint(-40,-30)
x_apple=random.randint(fruit_width,330)-fruit_width

y_orange=random.randint(-10,0)
x_orange=random.randint(fruit_width,330)-fruit_width

y_watermallon=random.randint(-8000,-7770)
x_watermallon=random.randint(fruit_width,330)-fruit_width 

#flags
left=False
right=False
hit=False
fruit_drop=False


#####################################################
#music=pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1)

#####################################################

def redrawGameWindow():
    
    win.blit(bg,(0,0))
    
    win.blit(watermallon,(x_watermallon,y_watermallon))
    win.blit(apple,(x_apple,y_apple))
    win.blit(mango,(x_mango,y_mango))
    
    win.blit(orange,(x_orange,y_orange))
    
    
    if right or left :
        win.blit(bucket,(x,y))
    else:
        win.blit(bucket,(x,y))

    
    score_label=font.render(f"score:{score}",1,(0,0,0))
    level_label=font.render(f"level:{level}",1,(0,0,0))
    high_score_label=font.render(f"High score:{high_score}",1,(0,0,0))

    win.blit(score_label,(display_width-score_label.get_width()-60,display_height-50))
    
    win.blit(level_label,(level_label.get_width()-20,display_height-50))
    
    win.blit(high_score_label,(display_width//2,50))

    pygame.display.update()


#####################################################
#main loop
run=True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    


       

######################################################    
#collision
    if x<=x_orange<=x+bucket_width and y<=y_orange+fruit_height<=y+30:
        score+=5
        y_orange=random.randint(-10-fruit_width,-fruit_width)
        x_orange=random.randint(0,330-fruit_width)
    if x<=x_watermallon<=x+bucket_width and y<=y_watermallon+fruit_height<=y+30:
        score+=50
        y_watermallon=random.randint(-8000-fruit_height,-7770-fruit_width)
        x_watermallon=random.randint(0,330-fruit_width)

    if x<=x_mango<=x+bucket_width and y<=y_mango+fruit_height<=y+30:
        score+=20
        y_mango=random.randint(-70-fruit_width,-60-fruit_width)
        x_mango=random.randint(0,330-fruit_width)

    if x<=x_apple<=x+bucket_width and y<=y_apple+fruit_height<=y+30:
        score+=10

        y_apple=random.randint(-40-fruit_width,-30-fruit_width)
        x_apple=random.randint(0,330-fruit_width)

#######################################################
#normal motion of fruits       
    if y_watermallon<490:
        
        y_watermallon+=fruit_vel+5# drop velocity

        
    else:
        y_watermallon=random.randint(-8000-fruit_height,-7770-fruit_width)
        x_watermallon=random.randint(0,330-fruit_width) 

    
    if y_mango<490:
        
        y_mango+=fruit_vel+4
        
        
    else:
        y_mango=random.randint(-70-fruit_width,-60-fruit_width)
        x_mango=random.randint(0,330-fruit_width)
    
        
    if y_apple<490:
        
        
        y_apple+=fruit_vel+3
    else:
        y_apple=random.randint(-40-fruit_width,-30-fruit_width)
        x_apple=random.randint(0,330-fruit_width)

    if y_orange<490:
        
        y_orange+=fruit_vel+2
        
        
    else:
        y_orange=random.randint(-10-fruit_width,-fruit_width)
        x_orange=random.randint(0,330-fruit_width)
###############################################################
        #if fruit touch bottom
    if y_watermallon>display_height or y_mango>display_height or y_apple>display_height or y_orange>display_height:
        score-=4

    if high_score<score:
        high_score=score
        
        
################################################################        
# keys
    keys=pygame.key.get_pressed()
    if keys[pygame.K_0]:
        fruit_drope=True
        
    if keys[pygame.K_LEFT] and x>0:
        x-=bucket_vel
        left=True
        right=False
        

    elif keys[pygame.K_RIGHT] and x<330-bucket_width:
        x+=bucket_vel
        
        right=True
        left=False
    else:
        
        right=False
        left=False
    

            
    redrawGameWindow()
pygame.quit()            
