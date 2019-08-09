# Neural Network

## Model A

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

## Idea/Concept

Input:

- Constant:
 - bias
 - tick (periodic pulse, different frequence)
 - wave (sinusoidale)

- Inner:
 - food_status
 - water_status
 - Lifespan
 - speed
 - acceleration

- Outer:
 - eyes
 - touch sensor
 - smell sensor (food, other creature)
 - magnetic field (knows North direction, add noise to avoid perfection)
 - memory slots
 - detect that other are familly (parent,children)
 
Output:

- sleep
- eat
- drink
- share food with other
- memory slots