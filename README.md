## Grass Blowing in the Wind with Pygame

I saw a cool video that had some simulated grass blowing in the wind using pygame, and I thought Hey, I can use pygame!
While the example was much better than mine, I'm quite proud of what I managed to scrape together.
The project is split up into three files, for each step of progresion I took.

The first; CalcAll.py. I set up all the basic logic for the grass to sway in the wind, but it has to calculate, rotate, and then scale each blade of grass.
Because in the 500x500 window I made there is 2,500 individual blades of grass, it takes a long time for each frame to render.

In the next file, PreCalc.py, all the variations of grass are saved to there own list. This lets me simply call the specific variation of grass I am looking for.
This bumps the performance considerably, and on my device, increased the frame-rate from `~30 to ~55, near the limit of 60.

In the original project I saw, the grass would be pushed away by the mouse pointer, making it look as though the pointer was among the grass.
This is the final file, PushyGrass.py. On my laptop, it cost me `~10 frames, due to all the checks I have to make, as well as having to calculate the values again.

I'm still very happy with the project, even with the poorly crafted blades of grass, and I could easily encorperate the grass into future projects, maybe with a few less blades though.
