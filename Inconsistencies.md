# Pain Points - PySoy Dev

---

# PyDodger 1.0

> Finding permissible values of pre-defined functions.
	
While working with PySoy, the only way to find out about the various attributes of certain functions and modules is by looking at the other examples. For a very simple example, a first-time user would not know what kind of shapes (s)he will be able to generate using soy.bodies()

Similarly, attributes like colormap are known not of, unless one studies and notes down all the examples in PySoy.

That is, for the game I made, I had to primarily resort to learning from the examples provided. I incorporated everything I could from the examples; I’ve elaborated upon this  attached dev notes.

> PySoy docs are inadequate.

The PySoy documentation is lacking. First-time users would find PySoy development much simpler if there were more PyDocs for soy.materials, soy.scenes classes, similar for textures, light, containers and camera. There aren’t many libraries, nor are there many tutorials that a beginner could work on.

> API issues

When I tried running PySoy files across different systems - the API tended to change in not only functionality, but also interface. In some systems, the file was extremely smooth, in others, it crashed a couple of times before working moderately well. I believe this inconsistency may prove to act as an extremely fatal flaw.

> UI Issues

The UI/UX could be improved massively by acting upon multiple small things here and there. Channels could be split, widgets could be improved, a scrollbar could be added, and there could be pre-existing themes for the user to choose from.

> Suggestions:

Develop an IDE specifically for PySoy development
Use modern versions of OpenGL for rendering
Improve the lacking documentation, convert multiple files (redundant) to a single, organised and concise document
Make the program easy to download
Put up tutorials to do the same on the Copyleft Games YouTube channel.

---

# PyDodger 2.0 + 3.0

> Could not make the title interactive as the PySoy events module (keypress/keyrelease) are purely binded to in-game actions.

> Wasn’t able to include mouse pointer integration and controls using the third party library: the JNativeHook, as it made the game glitch and jammed the VM altogether.

> Recreated the game using first person-player, however the game glitched and stopped working at times. Furthermore, the gameplay wasn’t remotely as good as observable in third-person.

> (Potential Issue I might continue facing in the future) Created a Blender 3-D model to implement inside the room, however calling functions and implementing the code for the integration of the model was rather difficult.


