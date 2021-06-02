# Tetris Perfect Clear helper

This was created to help with perfect clear setups in Tetris. It requires you to have created the setup shown here: https://tetris.fandom.com/wiki/Perfect_Clear_Guide. 

Given your pieces, it should output an image that looks like this:

![ITS](https://github.com/Inferno2332/Perfect-Clear/blob/master/pictures/its1.PNG)

To use it, you can do one of two things:

1. Run the cells in `perfect clear.ipynb`, and input your hold, current, and next two pieces (if you have no hold piece, input your current and next three pieces) as a 4-character string. It will output all perfect clear setups possible with your pieces.

2. On your command line, navigate to this repo and enter `py tetris/pc.py <pieces>`. For example, `py tetris/pc.py ilts`. It will open an image showing one possible perfect clear setup, if it exists.

By default, it assumes the "hook" in the setup is on the right. The optional `reverse` argument comes after `pieces` and can be set to True if the "hook" is on the other side.
