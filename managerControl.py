import pyglet
from game import hud

class Manager():
    def __init__(self, batch):
        self.batch = batch

        self.units = []
        self.doodads = []
        self.missiles = []
        self.huds = []
        self.floatingTexts = []
        self.players = []
        self.stats = []
        self.buffs = []
        self.specialEffects = []
        self.texturePacks = []
        self.sounds = []
        self.tilesets = []
    
    def update(self, dt):

        for unitObject in self.units:
            unitObject.update(dt)
            if unitObject.alive == False:
                self.units.remove(unitObject)
                del unitObject 

        for hudObject in self.huds:
            for icon in hudObject.icons:
                if icon.key == 'A' and hudObject.player.attack != None:
                    icon.update(hudObject.player.attack.cooldownTime, hudObject.player.attack.cooldown)
                if icon.key == 'Q' and hudObject.player.skillQ != None:
                    icon.update(hudObject.player.skillQ.cooldownTime, hudObject.player.skillQ.cooldown)
                elif icon.key == 'W' and hudObject.player.skillW != None:
                    icon.update(hudObject.player.skillW.cooldownTime, hudObject.player.skillW.cooldown)
                elif icon.key == 'E' and hudObject.player.skillE != None:
                    icon.update(hudObject.player.skillE.cooldownTime, hudObject.player.skillE.cooldown)
                elif icon.key == 'R' and hudObject.player.skillR != None:
                    icon.update(hudObject.player.skillR.cooldownTime, hudObject.player.skillR.cooldown)
            for bar in hudObject.bars:
                if bar.barType == 0:
                    bar.update(hudObject.player.health, hudObject.player.healthMax + hudObject.player.bonus.healthMax)
                else:
                    bar.update(hudObject.player.energy, hudObject.player.energyMax + hudObject.player.bonus.energyMax)

        for floatingTextObject in self.floatingTexts:
            if floatingTextObject.opacity < 100:
                floatingTextObject.update(dt)
            else:
                floatingTextObject.text.delete()
                self.floatingTexts.remove(floatingTextObject)
                del floatingTextObject
        
        for specialEffectObject in self.specialEffects:
            specialEffectObject.update(dt)
            if specialEffectObject.alive == False:
                specialEffectObject.sprite.delete()
                self.specialEffects.remove(specialEffectObject)
                del specialEffectObject 