#!/usr/bin/env python3

#this scipt attemps to create a remote for controling a ros robot via kivy

import kivy 
from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.relativelayout import RelativeLayout 
from kivy.config import Config 
from kivy.uix.slider import Slider
from kivy.uix.label import Label 
import vars

Config.set('graphics', 'resizable', True) 
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '390')

class Pos_Size_App(App): 
	def build(self):
		def go_forward(self):
			print('forward')
			vars.X0=1
			pub()
		def go_backward(self):
			print('backward')
			vars.X1=1
			pub(self)
		def go_right(self):
			print('right')
			vars.X2=1
			pub()
		def go_left(self):
			print('left')
			vars.X3=1
			pub()
		def pub(self):
			print('x0 = ',str(vars.X0*s1.value),' x1 = ',str(vars.X1*s1.value),' x2 = ',str(vars.X2*s1.value),' x3 = ',str(vars.X3*s1.value))
			reset(self)
		def reset(self):
			vars.X0=0
			vars.X1=0
			vars.X2=0
			vars.X3=0
		shift = .3
		scaling = 2
		button_length =.25
				
		rl = RelativeLayout(size =(180, 390)) 

		b1 = Button(size_hint=(button_length+.1, button_length/scaling), 
					pos_hint={'center_x':.5, 'center_y':(.5+shift)/scaling}, 
					text = "Forward")		 
		b1.bind(on_press=go_forward)
		

		b2 = Button(size_hint =(button_length, button_length/scaling),
					pos_hint={'center_x':.5, 'center_y':(.5-shift)/scaling}, 
					 text = "Back") 
		b2.bind(on_press=go_backward)
		

		b3 = Button( size_hint =(button_length, button_length/scaling), 
					pos_hint ={'center_x':.5+shift, 'center_y':.5/scaling}, 
					text = "Right")
		b3.bind(on_press=go_right)
		

		b4 = Button( size_hint =(button_length, button_length/scaling), 
					pos_hint ={'center_x':.5-shift, 'center_y':.5/scaling}, 
					text = "Left") 
		b4.bind(on_press=go_left)
		

		s1 = Slider(orientation='horizontal',
					value_track=True,
					value_track_color=(1,0,0,1),
					pos_hint={'center_x':.5, 'center_y':.6},
					min=0,
					max=1,
					value=1)
		
		l1 = Label(text='Power 0',
					pos_hint={'center_x':.2,'center_y':.525})

		l2 = Label(text='Power 100',
					pos_hint={'center_x':.8,'center_y':.525})

		rl.add_widget(b1) 
		rl.add_widget(b2) 
		rl.add_widget(b3) 
		rl.add_widget(b4) 
		rl.add_widget(s1)
		rl.add_widget(l1)
		rl.add_widget(l2)
		return rl
		

if __name__ == "__main__": 
	Pos_Size_App().run() 
