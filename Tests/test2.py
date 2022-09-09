from TrafficSimulation import *

# Create simulation
sim = Simulation()

# Add multiple roads

pos = [
    (0,0),(148,0),(300,0),(448,0),
    (0,100),(148,100),(300,100),(448,100),
    (0,200),(148,200),(300,200),(448,200),
    ]

sim.create_roads([
    #0,1,2
    (pos[0], pos[1]),(pos[1],pos[2]),(pos[2],pos[3]),
    #3,4
    (pos[3], pos[7]),(pos[7],pos[11]),
    #5,6,7
    (pos[11], pos[10]),(pos[10],pos[9]),(pos[9],pos[8]),
    #8,9
    (pos[8], pos[4]),(pos[4],pos[0]),


    #interseccion
    #10,11
    (pos[9], pos[5]),(pos[5],pos[1]),
    #12,13
    (pos[2], pos[6]),(pos[6],pos[10]),
    #14,15,16
    (pos[4], pos[5]),(pos[5],pos[6]),(pos[6],pos[7]),


])

sim.roads[0].vehicles.append(
  Vehicle({
    "path": dijstra(0,15)
  })
)

sim.roads[0].vehicles.append(
  Vehicle({
    "path": dijstra(0,4)
  })
)

sim.roads[0].vehicles.append(
  Vehicle({
    "path": dijstra(0,7)
  })
)

sim.roads[5].vehicles.append(
  Vehicle({
    "path": dijstra(5,10)
  })
)

sim.roads[5].vehicles.append(
  Vehicle({
    "path": dijstra(5,4)
  })
)

sim.roads[5].vehicles.append(
  Vehicle({
    "path": dijstra(5,14)
  })
)


sim.create_signal([[10], [14]])
sim.create_signal([[12], [15]])

# Start simulation
win = Window(sim)
win.offset = (-218, -110)
win.run(steps_per_update=5)