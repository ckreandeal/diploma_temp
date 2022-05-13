# -*- coding: utf-8 -*-

# pip install -r requirements.txt

from astrobox.space_field import SpaceField
from kornilov import KornilovDrone

if __name__ == '__main__':
    scene = SpaceField(
        speed=3,
        asteroids_count=5,
    )
    # TODO: 1. get all asteroids positions
    #       2. get all asteroids payload
    #       3. calculate even distance point between all asteroids to place mid-drone(second base) there
    #       4. reassign these metrics on a class level
    #       5. in Drones class:
    #           - is_midbase_active attribute (to track if bas drone is waiting for resources)
    #               - if no - send closest drone to take it place
    #               - get target as far as possible
    #           - deliver to midbase drone
    #

    # TODO: Send all drones to different asteroids and then on the second trip check if any asteroids have more then
    #  100 then choose them as a next target
    drones = [KornilovDrone() for _ in range(5)]

    scene.go()

# Первый этап: зачёт!
