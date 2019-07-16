# Game Loop

* http://gameprogrammingpatterns.com/game-loop.html
* http://gafferongames.com/game-physics/fix-your-timestep/
* http://www.koonsolo.com/news/dewitters-gameloop/

## Basic

Run as fast as possible.

```
while true:
  processInput()
  computeAI()
  computePhysics()
  render()
```

## Sleep

60 FPS = 16ms per frame.
Process current frame and wait until it's time for the next one.
It does not help with the game runs too slowly.

```
while true:
  start = currentTime()
  
  processInput()
  compute()
  render()
  
  sleep(start + ms_per_frame - currentTime)
```

## Variable time step

For each frame, we determine how much real time passed since the last game update.
Game engine is responsible for advancing game world _elapsed_ time.

* Game plays at consistent rate
* better hardware = smoother gameplay

```
lastTime = currentTime()
while true:
  current = currentTime()
  elapsed = current - lastTime
  
  processInput()
  compute(elapsed)
  render()

  lastTime = current
```

## Fixed update time step, variable rendering

* update game AI and physics at fixed time step
* allow flexibility when rendering

```
ms_per_update = 1/60 // must > compute() time to execute
previous = currentTime()
lag = 0.0 //real-time passed
while true:
  current = currentTime()
  elapsed = current - previous
  lag +=  elapsed
  
  processInput()
  
  while(lag >= ms_per_update)
    compute(elapsed)
    lag -= ms_per_update
    
  render(lag/ms_per_update)
```

