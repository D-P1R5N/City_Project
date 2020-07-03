![Sample Image of City Generated](https://imgur.com/zP7NAg5.png)

# City_Project
A project with the intention of making randomized city layouts with future hopes of simulated traffic.

Currently the "City" generated makes randomized segments of roads. Currently working on a technique to assure road connections. It uses random choices to determine what kind of road it will be creating, what kind of offset from the origin it will have, and in the case of diagonal roads, whether it should be inverted or not.

# Traffic
A future hope is that this will be used as a grid for simulating traffic. 

# Traffic Control
On top of the hopes of simulating traffic, the underlying concept is controlling traffic in a manner that would ensure every "vehicle" object can start in a location and reach any location while coordinating it's movements with other "vehicle" objects. This is to allow interactions such as lane merges, turns, road closures, sudden stops, and more. 

The idea behind controlling traffic is that the vehicle will only know what it is expected to do within several travel nodes. Other vehicles may give requests to alter the expected trajectory of another vehicle to allow for interactions without collisions. It should hopefully then ripple that one vehicle may influence all other vehicles that rely on a specific interaction so that there are no "surprises". 
