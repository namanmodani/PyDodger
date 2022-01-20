#!/usr/bin/env python3
 
# PyDodger by AlphaThesis
 
#I mports
import soy
import sys
import time
from time import sleep
from random import randint
 
# Game Status Variables
begin = False
game_in_play = False
client = soy.Client()
 
# Start for time notation
start = time.time()
 
# Defining the room - called scene
scene = soy.scenes.Room(soy.atoms.Size((15.0, 10.0, 40.0)), 1, 0, 0, 0)
 
# Defining the first level. Current version contains only 1 level.
def level_1():
 
    global client
    global scene
 
    # Defining material colour of the room
    scene.material = soy.materials.Colored('black')
 
    # Defining lights inside the black room
    scene['lighting_1'] = soy.bodies.Light((-10, 3, -10))
    scene['lighting_2'] = soy.bodies.Light((10, 3, -10))
    scene['lighting_3'] = soy.bodies.Light((5, 9, -5))
    scene['lighting_4'] = soy.bodies.Light((5, 9, -5))
 
    # Defining the position of the camera
    camera = soy.bodies.Camera((0, 1, 20))
    scene['cam'] = camera
    scene['cam'].position = soy.atoms.Position((0, 2, 18))
    scene['cam'].rotation = soy.atoms.Rotation((0, 0, 0.25))
    client.window.append(soy.widgets.Projector(scene['cam']))
 
    # Defining objects
    # Object_1: Box with gradient texture
 
    object_1 = soy.textures.Texture('./Images/tex1.jpeg')
 
    object_1_pos = randint(-3, 0)
 
    scene['object_1_1'] = soy.bodies.Box(soy.atoms.Position((object_1_pos, 0, object_1_pos)))
    scene['object_1_1'].radius = 0.1
    scene['object_1_1'].material = soy.materials.Textured(colormap = object_1)
 
    scene['object_1_2'] = soy.bodies.Box(soy.atoms.Position((0, object_1_pos, object_1_pos)))
    scene['object_1_2'].radius = 0.1
    scene['object_1_2'].material = soy.materials.Textured(colormap = object_1)
 
    # Object_2: Smoothcubes with solid texture
 
    cubemap = soy.textures.Cubemap("checkered", [soy.atoms.Color('firebrick'),
                                       soy.atoms.Color('goldenrod')])
 
    cubemap2 = soy.textures.Cubemap("checkered", [soy.atoms.Color('deeppink'),
                                        soy.atoms.Color('darkslategrey')])
 
    object_2_pos = randint(-3, 0)
 
    scene['object_2_1'] = soy.bodies.Box()
    scene['object_2_1'].radius = 0.1
    scene['object_2_1'].material = soy.materials.Textured()
    scene['object_2_1'].material.colormap = cubemap
 
    scene['object_2_2'] = soy.bodies.Box((0,0,0),(2,2,2))
 
    svgtex = soy.textures.Texture('<svg width="300" height="300"> \
           <rect width="300" height="300" style="stroke: none; fill: #ffffff"/> \
           <circle cx="80" cy="90" r="60" style="stroke: none; fill: #0000ff"/> \
           <circle cx="230" cy="70" r="50" style="stroke: none; fill: #ff00ff"/> \
           <circle cx="150" cy="220" r="70" style="stroke: none; fill: #ff0000"/> \
           </svg>')
 
    scene['object_2_2'].radius = 0.05
    scene['object_2_2'].material = soy.materials.Textured(colormap=svgtex)
 
    # Object_3: Sphere with checkered texture
 
    firebrick = soy.atoms.Color('firebrick')
    goldenrod = soy.atoms.Color('goldenrod')
 
    material = soy.materials.Textured()
    material.colormap = soy.textures.Cubemap("checkered", [firebrick, goldenrod])
 
    object_3_pos = randint(-3, 0)
 
    scene['object_3_1'] = soy.bodies.Sphere()
    scene['object_3_1'].radius = 0.6
    scene['object_3_1'].material = material
 
    scene['object_3_2'] = soy.bodies.Sphere()
    scene['object_3_2'].radius = 0.6
    scene['object_3_2'].material = material
 
    # Object_4: Sphere with graphic textures
 
    object_4 = soy.textures.Texture('./Images/tex2.jpeg')
 
    object_4_pos = randint(-3, 0)
 
    scene['object_4'] = soy.bodies.Sphere()
    scene['object_4'].radius = 0.6
    scene['object_4'].material = soy.materials.Textured(colormap = object_4)
 
    # Object_5: Sphere with graphic textures
 
    object_5 = soy.textures.Texture('./Images/tex3.jpg')
 
    object_5_pos = randint(-3, 0)
 
    scene['object_5'] = soy.bodies.Sphere()
    scene['object_5'].radius = 0.6
    scene['object_5'].material = soy.materials.Textured(colormap = object_5)
 
    # Player: Wireframed Sphere
 
    scene['player'] = soy.bodies.Sphere()
    scene['player'].material = soy.materials.Wireframed()
    scene['player'].radius = 0.5
    scene['player'].position = soy.atoms.Position((0, 0, 12))
 
    sleep(2.5)
 
    scene['object_1_1'].addForce(randint(-500, 500), randint(-500, 500), randint(-500,500))
    scene['object_1_2'].addForce(randint(-500, 500), randint(-500, 500), randint(-500,500))
 
    scene['object_2_1'].addForce(randint(-475, 475), randint(-475, 475), randint(-475,475))
    scene['object_2_2'].addForce(randint(-475, 475), randint(-475, 475), randint(-475,475))
 
    scene['object_3_1'].addForce(randint(-525, 525), randint(-525, 525), randint(-525,525))
    scene['object_3_2'].addForce(randint(-525, 525), randint(-525, 525), randint(-525,525))
 
    scene['object_4'].addForce(randint(-550, 550), randint(-550, 550), randint(-550, 550))
    scene['object_5'].addForce(randint(-450, 450), randint(-450, 450), randint(-450, 450))
 
 
    # Defining forces that the player can use
    forceR = soy.atoms.Vector((450, 0, 0))
    forceL = soy.atoms.Vector((-450, 0 ,0))
    forceF = soy.atoms.Vector((0, 0, -450))
    forceB = soy.atoms.Vector((0, 0, 450))
 
    # Using the Thrust attribute
    move_right = soy.actions.Thrust(scene['player'], forceR)
    move_left = soy.actions.Thrust(scene['player'], forceL)
    move_forward = soy.actions.Thrust(scene['player'], forceF)
    move_backward = soy.actions.Thrust(scene['player'], forceB)
 
    # Defining events
    soy.events.KeyPress.init()
    soy.events.KeyRelease.init()
 
    # Defining what actions must be taken when a certain event occurs.
    soy.events.KeyPress.addAction("W", move_forward)
    soy.events.KeyRelease.addAction("W", move_backward)
 
    soy.events.KeyPress.addAction("A", move_left)
    soy.events.KeyRelease.addAction("A", move_right)
 
    soy.events.KeyPress.addAction("S", move_backward)
    soy.events.KeyRelease.addAction("S", move_forward)
 
    soy.events.KeyPress.addAction("D", move_right)
    soy.events.KeyRelease.addAction("D", move_left)
 
# Sorting the elements in an iterable order
def check(x, y):
    return sorted(x) == sorted(y)
 
# Defining what must be displayed if the player is alive, or has lost.
def w_l():
    global scene
    global game_in_play
    true = (1, 0, 0, 0)
    rotate_value = scene['player'].rotation
    print(rotate_value)
    if check(rotate_value, true):
        print(rotate_value, 'Good going')
    else:
        game_in_play = False
        print(rotate_value, 'Game Over. Better luck next time!')
        end = time.time()
        score = int(end - start)*100
        print("Your score is", score, ". Well played!")
        sleep(1)
        client.window.title = "Your final score: " + str(score)
        title = soy.textures.Texture('./Images/gameover.jpeg')
        canvas = soy.widgets.Canvas(title)
        client.window.append(canvas)
        sleep(8)
        quit()
 
def menu():
    global game_in_play
    client.window.title = "PyDodger by AlphaThesis"
    title2 = soy.textures.Texture('./Images/title.jpeg')
    canvas2 = soy.widgets.Canvas(title2)
    client.window.append(canvas2)
    sleep(4)
    title3 = soy.textures.Texture('./Images/instructions.jpeg')
    canvas3 = soy.widgets.Canvas(title3)
    client.window.append(canvas3)
    sleep(8)
    game_in_play = True
    print('PyDodger started!')
 
# Final running program
if __name__ == '__main__':
    while client.window:
        if game_in_play is True and begin is False:
            begin = True
            level_1()
        elif game_in_play is False:
            begin = False
            menu()
        else:
            sleep(.125)
            w_l()
