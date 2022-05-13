import random

from astrobox.core import Drone


class KornilovDrone(Drone):
    my_team = []


    def on_born(self):
        self.target = self._get_my_asteroid()
        self.move_at(self.target)
        self.my_team.append(self)

    def _get_my_asteroid(self):
        if self.target is None:
            return random.choice(self.asteroids)
        else:
            for ast in self.asteroids:
                if ast.payload > 100:
                    return ast
                else:
                    return self.my_mothership

    def on_stop_at_asteroid(self, asteroid):
        self.load_from(asteroid)

    def on_load_complete(self):
        if self.payload != 100:
            self.target = self._get_my_asteroid()
            if self.target is not None:
                self.move_at(self.target)
            else:
                self.target = self.my_mothership
                self.move_at(self.target)
        else:
            self.move_at(self.my_mothership)

    def on_stop_at_mothership(self, mothership):
        self.unload_to(mothership)

    def on_unload_complete(self):
        if self.target == self.my_mothership:
            self.update_sleep_state()
        if self._target_is_empty(self.target):
            self.target = self._get_my_asteroid()
            self.move_at(self.target)
        else:
            self.move_at(self.target)

    def _target_is_empty(self, target):
        if target.payload == 0:
            return True
        else:
            return False

    def on_wake_up(self):
        self.target = self._get_my_asteroid()
        if self.target:
            self.move_at(self.target)
