from main_gun_entity import Main_gun_entity


class Gun1(Main_gun_entity):
    def __init__(self):

        self.shoot_speed = 100
        self.ammo_size = 50
        self.damage = 1
        self.bullet_speed = 10
        self.ammo = self.ammo_size

        super().__init__(self.shoot_speed, self.ammo_size, self.damage, self.bullet_speed, self.ammo)
