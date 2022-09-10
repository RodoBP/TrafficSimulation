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
    (pos[9], (148,98)),((148,98),pos[1]),
    #12,13
    (pos[2], (300,102)),((300,102),pos[10]),
    #14,15,16
    (pos[4], (150,100)),((150,100),(302,100)),((302,100),pos[7]),


])

sim.create_vehicle(0,15)
sim.create_vehicle(0,4)
sim.create_vehicle(0,7)

sim.create_vehicle(5,4)
sim.create_vehicle(5,2)
sim.create_vehicle(5,10)


sim.create_signal([[10], [14]])

sim.create_signal([[12], [15]])

# Start simulation
win = Window(sim)
win.offset = (-218, -110)
win.run(steps_per_update=5)