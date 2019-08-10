# Task Roadmap

## 0.2.0

- [ ] Use Space.current_time_step for Simulation time
- [ ] Add Creature's eye(graphic) to represent current angle

## 0.1.0

- [x] Control selected Creature with arrow keys
	- [x] Mark selected Creature, red rectangle using Bouncing Box
- [x] Display creature info (pos, size) when selected
- [x] Add buton play/pause, step time

# TODO

- [ ] Use factory pattern to create Creature
- [ ] Use pymunk shape sensor feature to do donut world
- [ ] Write specification from Keep note
- [ ] Write class diagram with plantuml
- [x] Add FPS display (see kivy-examples/kv)
- [x] Create EvoFlatWorld skeleton from poc/design_pattern/component
- [x] Rename to EvoFlatWorld

## ToFix

- [ ] Move world scatter widget make Splitter widget jump to the left side. Use another layout than Boxlayout ?

## GUI Features

- [ ] Add button activate "on click add creature at mouse cursor position"
- [ ] Add help tabulation in splitter panel. Creature: right_click display info
- [x] Add play, pause, speed up/down button

## Improve performance

- [ ] For better data locality use a list for each component type in game_system. Use profile.
- [ ] Disable pymunk debug mode. Does it have impact ?
- [ ] Compile Chipmunk in release mode
- [ ] Create Pymunk space with option threaded=True and Space.threads=x
- [ ] Creature is not a widget but a drawing instruction (Rectangle)
- [ ] Use Cython
- [ ] Use Kivent ?

## Nice to have

- [ ] Use kvlang and scatter widget for class World
- [x] Fix scatter scale up/down with mousewheel