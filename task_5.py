"""
5)AK-47
Soldier Ryan has an AK47
Soldiers can fire ("tigi-tigitishh").
Guns can fire bullets.
Guns can fill bullets - increase the number of bullets(reloads)

Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
Where soldier will fire from a gun and reload, and fire one more time.
"""
import time
from clint.textui import progress


class Gun():
    """название оружия ==> type_gun
    начальное количество патронов в магазине ==> mags
    максимальное кол-во патронов в магазине ==> patron"""
    def __init__(self, type_gun, mags, patron):
        self.type_gun = type_gun
        self.mags = mags
        self.patron = patron

class Soldier(Gun):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Я солдат по имени {self.name.title()}, и у меня есть {self.type_gun} в котором {self.mags} патронов"
    
    def reload_gun(self, patron):
        for i in progress.bar(range(self.patron - self.mags)):
            self.mags += 1
            time.sleep(.20)
        return self.mags

    def shooting(self):
        i = 0
        patron = self.mags
        while  1:
            trigger = int(input("для стрельбы нажмите '1', для выхода нажмите 2:\n"))
            if self.mags == 0:
                print('нет патронов, что делать? \nПерезарядка!!!')
                self.reload_gun(patron)
            elif trigger == 1:
                print("=<* БАХ")
                self.mags -= 1
                i += 1 
            elif trigger == 2:
                trigger = int(input(f"в магазине еще есть {self.mags} патронов,для перезарядки '1', для выхода нажмите '2', для продолжения стрельбы 3 \n"))
                if trigger == 1:
                    self.reload_gun(patron)
                elif trigger == 2:
                    print(f"Удачи на гражданке тебе солдат {self.name}")
                    break
                elif trigger == 3:
                    continue

sold1 = Soldier('Tom')
sold1.type_gun = 'AK47'
sold1.mags = 5
sold1.patron = 30
print(sold1)
sold1.shooting() 



