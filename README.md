# Boxes

## What is this?
Boxes is a simple 2d platformer created for Horizons Polaris. For me it served as an introduction to git and larger projects overall. The reasoning for creating this using pygame over godot is that I think that the experience and understanding from having implemented features at a lower level will help in creating more polished products in the future.

## How it was made
This game is a python platformer that relies on pygame for rendering and input detection and [Nuitka](https://nuitka.net/)

## The challenges I faced along the way
### Collisions between AABBs(Axis-Aligned Bounding Boxes)
Throughout the project, I had to continously refactor the collision detection and resolution between AABBs due to my unwillingless to start with more thorough solutions. I wasted unnumerable hours rewriting the same lines over and over especially since I was unwilling to use AI or research more about how others have implemented them.
### Loading and Saving through the Map Maker
Loading and manuvering between rooms proved more difficult than I initially imagined. My first attempt at a solution worked adequetely at the time, but as the time neared for me to finally make some levels, my initial solution was far from enough. I knew that the time would come where I would have to refine the way I store data and in the end I triumphed but not without having to deal with dicts and their inability to be copied through the built-in copy() method.


## Install
### Windows
1. Download the [latest windows release](https://github.com/ivanding3/Boxes/releases) zip
2. Unzip the file
3. Run main.exe (Note: you may have to unblock the .exe file)

## Dependencies
[Pygame](https://www.pygame.org)

***Note: Python 3.14 does not currently work with Pygame. Try Pygame Community Edition if you decide to run from the repo***
## Other 

## AI Disclosure
Minimal AI was used in the creation of this project. Any AI usage was to explain holes in the pygame docs (like pygame.scaled being required for VSync), or to explore other facets of the python language. 


## Artwork
All textures are made by [ProbablyADoor](https://github.com/ProbablyaDoor)
