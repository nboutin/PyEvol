# TODO

- [ ] Use factory pattern to create Creature
- [ ] Use pymunk shape sensor feature to do donut world
- [ ] Write specification from Keep note
- [ ] Write class diagram with plantuml
- [x] Add FPS display (see kivy-examples/kv)
- [x] Create EvoFlatWorld skeleton from poc/design_pattern/component
- [x] Rename to EvoFlatWorld

## Task

- [ ] Display creature info (pos, size) when selected
- [x] Add buton play/pause, step time

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

## Nice to have

- [ ] Use kvlang and scatter widget for class World
- [x] Fix scatter scale up/down with mousewheel