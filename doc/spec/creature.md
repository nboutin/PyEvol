# Creature

## Shape

* circle

## Neural Network

### Input

Inner sensors:
* bias (constant)
* tick (periodic impulse)
* health (food)
* thirst (water)

Outer sensors:
* Eyes*2 (left/right) (see Eyes model)


### Output

* Power*2 (left/right)
* Eat (wants to eat)
* Drink (wants to drink)
* Mate (wants to reproduce)

## Eyes

### Model A

* nearest food distance
* two values

### Model B

* 2D eyes
* see res/eye_model_b.png
* field of view is overlaping
* horizontal bargraph for each eyes
* How many inputs to represents bargraph ?

### Model B1

* add RGB colors