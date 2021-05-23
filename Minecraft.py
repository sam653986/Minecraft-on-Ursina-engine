from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
grass_texture = load_texture('graphics/grass_block.png')
arm_texture = load_texture('graphics/arm_texture.png')
stone_texture = load_texture('graphics/stone_block.png')
punch_audio = Audio('graphics/punch_sound.wav', loop = False, autoplay = False)
sky_texture = load_texture('graphics/skybox.png')

block_pick = 1

class Voxel(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'graphics/block',
			origin_y = 0.5,
			texture = grass_texture,
			color = color.white,
			scale = 0.5,
			highlight_color = color.cyan)

	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':	
				voxel = Voxel(position = self.position + mouse.normal)

			if key == 'left mouse down':
			    destroy(self)

class Hand(Entity):
    def __init__(self):
    	super().__init__(
    		parent = camera.ui,
    		model = 'graphics/arm',
    		texture = arm_texture,
    		scale = 0.2,
    		rotation = Vec3(150, -10,0),
    		position = Vec2(0.4,-0.6))

    	def active(self):
    		self.position = Vec2(0.3,-0.5)

    	def passive(self):
    	    self.position = Vec2(0.4,-0.6)

class Sky(Entity):
    def __init__(self):
       super().__init__(
       	parent = scene,
       	model = 'sphere',
       	texture = sky_texture,
       	scale = 150,
       	double_sided = True)    	    



window.exit_button.visible = True 

for z in range(30):
    for x in range(30):
        voxel = Voxel(position = (x,0,z))
player = FirstPersonController()
hand = Hand()
sky = Sky()
app.run()        		