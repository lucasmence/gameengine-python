import pyglet
from game import units
from game import abilities
from game import attackTypes
from game import collision

class BaseUnit(units.Unit):
    def __init__(self, mainBatch, positionX, positionY, owner, manager):    
        super().__init__(mainBatch, positionX, positionY, owner, manager)

        self.sprite.update(scale=1.00)
        self.name = 'base-unit'
        self.attackSpeed = 0.5
        self.healthMax = 100
        self.healthRegeneration = 0.2
        self.energyMax = 100 
        self.armor = 0
        self.movementSpeed = 150
        self.health = self.healthMax + self.bonus.healthMax 

######################################################################################################################################

class Hero(BaseUnit):
    def __init__(self, mainBatch, positionX, positionY, owner, manager):    
        super().__init__(mainBatch, positionX, positionY, owner, manager)
        
        self.model.load('warrior', '', manager)

        self.sprite.update(scale=1.00)
        self.name = 'hero'
        self.attackSpeed = 0.3
        self.healthMax = 50
        self.healthRegeneration = 0.2
        self.energyMax = 10 
        self.armor = 10
        self.movementSpeed = 120

        self.skillQ = abilities.Shuriken(self, self.manager)
        self.skillW = abilities.ShieldBlock(self, self.manager)
        self.attack = attackTypes.Slash(self, self.manager) 

        self.health = self.healthMax + self.bonus.healthMax

        self.sprite.image = self.model.texturePack.textureFiles['stand'][0].sprite

class SkeletonWarrior(BaseUnit):  
    def __init__(self, mainBatch, positionX, positionY, owner, manager):    
        super().__init__(mainBatch, positionX, positionY, owner, manager)

        self.model.load('skeleton-warrior', '', manager)

        self.name = 'skeleton-warrior'
        self.attackSpeed = 1
        self.healthMax = 10
        self.energyMax = 10 
        self.energyRegeneration = 0.2
        self.healthRegeneration = 0.00
        self.armor = 0
        self.movementSpeed = 20
        self.minimumRange = 50

        self.skillQ = None
        self.attack = attackTypes.Slash(self, self.manager) 

        self.sprite.image = self.model.texturePack.textureFiles['stand'][0].sprite
    
    def update(self, dt):
        self.moving = True
        distance = collision.distance(self.diferenceX, self.diferenceY)
        super().update(dt)

        if (collision.distance(self.diferenceX, self.diferenceY) <= 100):
            self.cast(self.A, self.moveX, self.moveY)  

class SkeletonArcher(BaseUnit):  
    def __init__(self, mainBatch, positionX, positionY, owner, manager):    
        super().__init__(mainBatch, positionX, positionY, owner, manager)

        self.model.load('skeleton-archer', '', manager)

        self.name = 'skeleton-archer'
        self.attackSpeed = 2.25
        self.healthMax = 10
        self.energyMax = 10 
        self.energyRegeneration = 0.2
        self.healthRegeneration = 0.00
        self.armor = 0
        self.movementSpeed = 20
        self.minimumRange = 400

        self.skillQ = None
        self.attack = attackTypes.Arrow(self, self.manager) 

        self.sprite.image = self.model.texturePack.textureFiles['stand'][0].sprite
    
    def update(self, dt):
        self.moving = True
        distance = collision.distance(self.diferenceX, self.diferenceY)
        super().update(dt)

        if (collision.distance(self.diferenceX, self.diferenceY) <= 500):
            self.cast(self.A, self.moveX, self.moveY)  
   

class SkeletonArcherHero(BaseUnit):  
    def __init__(self, mainBatch, positionX, positionY, owner, manager):    
        super().__init__(mainBatch, positionX, positionY, owner, manager)

        self.model.load('skeleton-archer', '', manager)

        self.name = 'skeleton-archer'
        self.attackSpeed = 2.00
        self.healthMax = 10
        self.energyMax = 10 
        self.energyRegeneration = 0.2
        self.healthRegeneration = 0.00
        self.armor = 0
        self.movementSpeed = 100

        self.skillQ = None
        self.attack = attackTypes.Arrow(self, self.manager) 

        self.sprite.image = self.model.texturePack.textureFiles['stand'][0].sprite
