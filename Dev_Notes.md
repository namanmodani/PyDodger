# PyDodger by AlphaThesis
# Dev notes, v3

# Task 1

> Session 1
-Imported all required libraries that might be useful in the development of the game, for instance sys to add system-specific parameter, sleep to delay execution as and when need be.
-Defined game status variables and the client
-Created and mingled with different room sizes to see which one suits the game perfectly. Defined the camera, material color and lights within the room.

> Session 2
-Defined the first level.
-Made use of various objects, inspired from multiple mature examples in the PySoy library, to create smoothcubes, svg, boxes with textured gradient, a wireframed sphere amongst others.
Following is a list of examples that I took inspiration from:
Billboard.py, blocks.py, buggy_example.py, CollideBlocks.py, CubeAndSphere.py, gci2012.py, Portal.py, svg_string_example and wireframed.py
-Defined the player using a wireframes sphere.
-Defined texture, material, radius of all objects and the player.

> Session 3
-Defined random movement of objects.
-Defined forces by using the Thrust attribute, added actions through the WASD keys.
-Defined check(x,y) to sort elements in an iterable order.


# Task 2

> Session 4
-Defined a menu (Title is a WIP)
-Defined a win/lose situation and what will be printed on the terminal during the same.
-Defined the final run program.

> Session 5
-Defined the calculation of the scores, using the time module in Py3.
-Developed the graphics, for:
---the title
---the instructions menu and 
---the gameover screen.
-Changed position of the lights inside the room to improve quality of gameroom.

> Session 6
-Revised the game scoring system, which is now a different function of the time attribute.
-Appended canvases in order to incorporate the title, instructions and the gameover screen.
-Made all the three screen canvases functional and visible.

> Session 7
-Added two new objects- both graphic textured spheres to the game-room to increase complexity of the game (was found too easy in the current settings).
-Changed the randint values and speed, alongwith position and rotation attributes, again to increase the complexity of the game.
-Renamed certain elements inside the room in order to make code easier to comprehend and cleaner.
-Removed the possibility of the player leaving the confines of the room. Now, if a player strikes against the walls of the room, the sphere bounces back like it would in real life, thereby adding a more realistic effect to the game

> Session 8
-Now made it possible to view the final score on the client window's titlebar, thereby removing the requirement to switch to the terminal (another window) to check the score.
-Edited the gameover graphic according to the new final score display.
-Edited the README file.

# Task 3

> Session 9
-Redesigned the graphics of the game to make it more inherent and improve the user interface. Added the instructions graphic to a canvas.
-Rewritten the game in accordance with a system wherein the user need not make any use of the README to understand the instructions.
-Altered and randomized the speeds of the objects in the game room to make the game more fun-to-play.

> Session 10
-Added more comments to make the code cleaner and easier to comprehend for anybody interested in inspecting the game dev perspective of PyDodger.
-Added a background to the game - in space. The game now makes more sense since the objects are randomly floating around in space and it is the job of the player to maneuver past all of this.
-Improved processing of the game by making it faster and smoother by altering certain rusty blocks of code.

> The game is now complete.
