# PyDodger: Dev notes v3.4

## Task 1

### Session 1
- Imported required libraries, for instance sys (to add system-specific parameter), sleep (to delay execution), soy, time, randInt.
- Defined game status variables and the client.
- Played around with different room sizes to gauge suitability. Defined the camera, material color and lights within the room. Initiated scene.   

### Session 2
- Defined the first level, using objects inspired by mature examples in the PySoy - to create smoothcubes, svgs, textured gradient boxes, and wireframed spheres.
- Inspiration list: Billboard.py, blocks.py, buggy_example.py, CollideBlocks.py, CubeAndSphere.py, gci2012.py, Portal.py, svg_string_example, wireframed.py.
- Defined the player using a wireframed sphere. Invoked functions to determine physical attributes (texture, material, radius) of objects and the player.

### Session 3
- Defined random movement of objects, and forces by using the Thrust attribute. Appended actions via WASD.
- Sorted elements in an iterable order using check(x, y).

## Task 2

### Session 4
- Defined a menu (Title is a WIP), a win/lose situation, and case-wise terminal outputs.
- Coded the final run program, writing the algorithm for score calculation using the time module in Py3.
- Designed graphics (using Figma + Canva), for the:
    - title,
    - instructions menu, and 
    - game-over screen.
- Altered position of the lights to improve gameroom quality.

### Session 5
- Revised the game scoring system, and refactored it into a different function within time().
- Appended canvases to incorporate title, instructions and the gameover screen. Checked screen canvases for functionality and visibility.
- Added two graphic textured spheres to increase complexity of the game (earlier determined 'too easy'). Also changed randint values and speed, alongside position and rotation attributes.


### Session 6
- Renamed certain elements inside the room in order to increase code readability.
- Eliminated the case scenario where the player can leave the confines of the room. Upon strikes against the walls of the room, the player object bounces back like it would in real life. Induced realism.
- Ensured easy final score visibility on the client window's titlebar, eliminating the requirement to switch to the terminal to check the score.
- Edited the gameover graphic according to the new final score display. 

## Task 3

### Session 7
- Redesigned graphics to improve the user interface. Added the instructions graphic to a canvas.
- Rewritten the game in accordance with a system wherein the user can inherently understand game instruction, without making use of the README to understand instructions.
- Altered and randomized the speeds of the objects in the game room to make the game more fun-to-play.

### Session 8

- Added more comments to improve code readability. 
- Appended a background to the game to induce realism, depicting the universe. This explains the zero gravity objects.
- Improved processing of the game by refactoring rusty blocks of code, and thereby runtime.