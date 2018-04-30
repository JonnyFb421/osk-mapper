About On-Screen Keyboad Mapper
======
OSK Mapper's goal is to easily bind the coordinates of the position for each key represented on the on-screen keyboard.  
Other classes may inherit this class, and upon calling `super().__init__()` receives class variables such as `self.A, self.TAB, self.UP`.  When used in conjunction with PyAutoGui, this module can help aid automation across various use cases where PyAutoGui cannot interact with a program directly.  

Version 0.0.1

Installing
------
Install this module by running:
```bash
pip install osk_mapper
```

Usage
------
```python
import time

import pyautogui
from osk_mapper.mapper import KeyLocations

class SampleBot(KeyLocations):
    def __init__(self):
        super().__init__()
        self.direction = 'right'
    
    def run(self, direction, duration):
        if direction == 'right':
            pyautogui.mouseDown(self.RIGHT)
            self.direction = 'right'
        elif direction == 'left':
            pyautogui.mouseDown(self.LEFT)
            self.direction = 'left'
        time.sleep(duration)
        pyautogui.mouseUp()

    def loot(self):
        loot_directions = [self.LEFT, self.RIGHT]
        for direction in loot_directions:
            for x in range(5):
                pyautogui.mouseDown(direction)
                time.sleep(0.1)
                pyautogui.mouseUp()
                # Z is the loot button
                pyautogui.mouseDown(self.Z)
                time.sleep(1)
                pyautogui.mouseUp()
            if direction == self.LEFT:
                self.run('right', 1)
            elif direction == self.RIGHT:
                self.run('left', 1)
```

Development Setup
------
```bash
pip install -e osk_mapper[dev]
```
Tests are written using Pytest

