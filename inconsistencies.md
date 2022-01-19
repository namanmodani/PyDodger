# Pain Points - PySoy Dev

---

## PyDodger 1.0

### Inadequacy of PySoy documentation.

- The PySoy documentation is lacking. First-time users would find PySoy development much simpler if there were more PyDocs for soy.materials, soy.scenes classes, similar for textures, light, containers and camera. A lack of libraries and tutorials makes PySoy beginner-unfriendly.

### Finding permissible values of pre-defined functions.
	
- Only pre-existing examples allow understanding the function attributes. For instance: a first-time user would not know the generable shapes using soy.bodies(). Similarly, attributes like colormap are known not of, unless one studies and notes down all the examples in PySoy. For PySoy, I had to primarily resort to learning from the examples provided. Read: Dev Notes.

### API issues

When I tried running PySoy files across different systems - the API changed in not only functionality, but also interface. In some systems, the file run was butter smooth, in others, it crashed.

### UI Issues

The UI/UX could be improved massively. Examples: split channels, redesign widgets, append scrollbars, and add pre-existing themes for the user to choose from.

### Suggestions:

- Incorporate the usage of modern versions of OpenGL for rendering.
- Improve the lacking documentation, convert multiple files (redundant) to a single, organised and concise document.
- Make the program user-friendly and easy-to-download. Upload tutorials to Copyleft YouTube.

---

## PyDodger 2.0 + 3.0

- Uneasy Blender integration.
- PySoy events module (keypress/keyrelease) are purely binded to in-game actions. Leads to a lack of title interaction.
- The JNativeHook was unable to include mouse pointer integration and controls. Jammed the game.
- Game glitches in FPP >> TPP.