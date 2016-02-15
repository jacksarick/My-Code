{- 
  Game "Asteroids" using the Gloss library

  Pedro Vasconcelos <pbv@dcc.fc.up.pt> 2014
  Department of Computer Science
  Faculty of Science, University of Porto
-}

module Main where

import System.Random 
import Graphics.Gloss
import Graphics.Gloss.Interface.Pure.Game

- Representation of the "world" game
- List of objects with the following invariant:
- * Is never empty; 
- * The first element is * always * the ship of the player.
World type = [Object]

- An object in space
- A pair of form and movement
Object type = (Shape, Movement) 

- Forms of different objects 
date Shape = Asteroid Float - asteroids (size)
           | Laser Float - "lasers" (decay) 
           | Ship - the player's ship
          

- Representing the motion of an object
- Position, linear speed, direction and angular velocity
type = Movement (Point - center position 
                 Vector, - linear speed
                 Float - orientation (degrees)
                 Float - angular velocity (deg / s)
                 )


- Test whether an object is an asteroid 
isAsteroid :: Object -> Bool
isAsteroid (Asteroid _, _) = True
isAsteroid _ = False

- Test whether laser
isLaser :: Object -> Bool
isLaser (Laser _, _) = True
isLaser _ = False


- | Draw all objects
drawWorld :: World -> Picture
drawWorld objs = pictures (map drawObj objs)
 

- | Draw an object in correct position and orientation
drawObj :: Object -> Picture
drawObj (shape, ((x, y) _, ang, _)) 
  = Xy $ translate rotate ang $ drawShape shape


- | Draw the shape of an object (centered at the origin)
drawShape :: Shape -> Picture
drawShape Ship color = green ship 
drawShape (Team Laser) = yellow color laser
drawShape (size Asteroid) = color red (scale size size asteroid)

- | Basic figures
ship, laser, asteroid :: Picture
polygon ship = [(20.0) (- 10.10), 
                (-5.0) (- 10, -10), (20.0)]
laser line = [(0.0) (10.0)]
asteroid polygon = [(-10.5) (- 5, 10), (10.5),
                    (5, -5), (- 5 -10) (- 10.5)]


- | Next movement state after interval dt ''
move :: Float -> Movement -> Movement
moves t ((x, y), (dx, dy), ang, angV) 
  = ((X ', y'), (dx, dy), ang 'angV)
    where x = wrap (x + dx * dt) maxWidth
          y = wrap (y + dt * dy) maxHeight
          ang 'ang = + dt * angV
          wrap h max | h> h-max = 2 * max
                     | H <-max = h + 2 * max
                     | Otherwise = h

- | Move an object by an interval dt ''
moveObj :: Float -> Object -> Object
moveObj dt (shape, mov) = (shape, move dt mov)


- | Advance the simulation of the world an interval dt ''
updateWorld :: Float -> World -> World
updateWorld dt = collisions. dt decay. map (moveObj dt)



- | Decay of projectiles "laser" in the game
Decay :: Float -> World -> World
decay dt (ship: objs) = ship: filter remain (map decr objs)
  where
    - Reduce the decay time of "lasers"
    decr (Laser t, mov) = (Laser (t-dt), mov)
    decr obj = obj
    - Test whether an object has not disappeared
    - (Ie must remain in play)
    remain (Laser t, mov) = t> 0 - "lasers" only positive time
    remain _ = True - everything else remains

  
- | Detect address collisions and
collisions :: World -> World
collisions (ship: objs) = ship: (frags ++ objs' ++ objs' ')
  where rocks = filter isAsteroid sounds - all asteroids
        lasers = filter isLaser sounds - all lasers
        frags = concat [fragment rock | rock <-rocks, 
                        any (`hits`rock) lasers]
        objs' = [obj | obj <-rocks, 
                 not (any (`hits`obj) lasers)] 
        objs '' = [obj | obj <-lasers, 
                 not (any (obj`hits`) rocks)]
        
        
- Check for collision between two objects
- Only between "lasers" and asteroids
hits :: Object -> Object -> Bool        
hits (Laser _ ((x, y), _, _, _)) (sz Asteroid ((x ', y'), _, _, _))
  = (X-x ') ** 2 + (y-y) ** 2 <= (10 * sz) ** 2
hits _ _ = False


- Fragment an asteroid into smaller pieces
- Eliminates too small fragments
fragment :: Object -> [Object]
fragment (sz Asteroid, (pt, (dx, dy), ang, angV))
  | Sz '> = 1 = [(sz Asteroid' (pt, vel ', ang, angV)) | vel' <- vels]
  | Otherwise = []
  where sz '= 0.5 * sz
        vels = [(dy, dx), (- dx, dy), (dx -dy), (- dy, -dx)]


- | React to key events triggered by player
react :: Event -> World -> World
- * Run the ship (left / right)
react (eventKey (SpecialKey KeyLeft) keystate _ _) (ship: objs) 
  = (Ship ': objs)
  where (Ship, (pos, vel, ang, angV)) = ship
         angV '= if keystate == Down Then (-180) else 0
         ship '= (Ship, (pos, vel, ang, angV'))
         
react (eventKey (SpecialKey KeyRight) keystate _ _) (ship: objs) 
  = (Ship ': objs)
  where (Ship, (pos, vel, ang, angV)) = ship
         angV '= if keystate == Down Then 180 else 0
         ship '= (Ship, (pos, vel, ang, angV'))


- * Accelerate the ship forward
react (eventKey (SpecialKey KeyUp) Down _ _) (ship: objs) 
  = (Ship ': objs)
  where (Ship, (pos, (dx, dy), ang, angV)) = ship
        dx '= dx + 10 * cos (-ang / 180 * pi)
        dy 'dy = + 10 * sin (-ang / 180 * pi)
        ship '= (Ship, (pos, (dx, dy'), ang, angV))


- * Shoot a new projéi just read on wikipedia que
react (eventKey (SpecialKey keyspace) Down _ _) (ship: objs) 
  = (Ship: proj: objs)
  where (Ship, (pos, _, ang, _)) = ship
        vel = (400 * cos (-ang / 180 * pi), 400 * sin (-ang / 180 * pi))
        proj = (Laser 1 (pos, vel, ang, 0)) - decays after 1 sec.

- * All other events: Ignore
_ react world = world        



- | Create a random asteroid
randRock :: IO Object
randRock the pos = <- randPoint
              vel <- randVel
              angV <- randomRIO (-90.90)
              ang <- randomRIO (-180.180)
              sz <- randomRIO (1.4)
              return (sz Asteroid, (pos, vel, ang, angV))

randVel :: IO Vector
randVel = dx <- randomRIO (-50.50)
             dy <- randomRIO (-50.50)
             return (dx, dy)
                
randPoint :: IO Point                
randPoint = the x <- randomRIO (-maxWidth, maxWidth)
               y <- randomRIO (-maxHeight, maxHeight)
               return (x, y)
             

- Constant
maxWidth, maxHeight :: Float
maxWidth = 300
maxHeight = 300

fps :: Int
fps = 60

main :: IO ()
main = do
  rocks <- sequence [randRock | _ <- [1..10]]     
  play black window fps (ship: rocks) drawWorld react updateWorld
  where 
    = ship (Ship, ((0,0), (0,0), 0, 0)) - starting position of the ship

window = InWindow "Asteroids" (2 * maxWidth round, 2nd round maxHeight) (0.0)