# TODO

- [ ] Add FPS display (see kivy-examples/kv)
- [ ] Use factory pattern to create Creature
- [ ] Use pymunk shape sensor feature to do donut world
- [ ] Write specification from Keep note
- [ ] Write class diagram with plantuml
- [x] Create EvoFlatWorld skeleton from poc/design_pattern/component
- [x] Rename to EvoFlatWorld

## Improve performance
- [ ] For better data locality use a list for each component type in game_system. Use profile.
- [ ] Disable pymunk debug mode. Does it have impact ?
- [ ] Compile Chipmunk in release mode
- [ ] Create Pymunk space with option threaded=True and Space.threads=x

## Nice to have
- [ ] Use kvlang and scatter widget for class World
- [x] Fix scatter scale up/down with mousewheel