class Soldier:
    health = 5

    def take_damage(self, damage, multiplier):
        damage = damage * multiplier
        self.health -= damage
        print(self.health)
        return self.health, damage, multiplier

def new_test():
    soldier = Soldier()
    print(Soldier.take_damage(soldier, 10, 99))  # Now you're explicitly passing the instance

new_test()
#Soldier.take_damage(3, 3)
# dalinar = Soldier()
# damage, multiplier = 30, 3
#
# # Only "damage" and "multiplier" are passed as arguments
# # "dalinar" is passed implicitly as the first argument, "self"
# dalinar.take_damage(damage, multiplier)
