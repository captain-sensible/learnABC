'''
author: andy brookes 
aka:  captain_sensible
email: andybrookestar@gmail.com
web: http://www.ginbrookesfoundation.org

app displays each letter of alphabet, an animal whos name begins with relevant letter of alphabet
then app gives audio of sound animal makes, and someone speaking name of animal
app is suitable for children of all ages, but particularly useful for kids learning alphabet!
'''
from random import randint

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


class Andy(BoxLayout,Image):
	count = -1
	sound1 =           SoundLoader.load("blank.ogg")
	sound2 =           SoundLoader.load("blank.ogg") 
	sound3 =           SoundLoader.load("blank.ogg") 
	tempAnimDesc = []
	tempAnimImage = []
	tempAnimSound = []
	tempAnimNoun = []
	subcount = 0
	Window.clearcolor = (1, 1, 1, 1)
	
	InAlphabet =("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"  )
	InventeryLs = ("LetterSound/a.ogg", "LetterSound/b.ogg","LetterSound/c.ogg", "LetterSound/d.ogg","LetterSound/e.ogg","LetterSound/f.ogg","LetterSound/g.ogg", "LetterSound/h.ogg","LetterSound/i.ogg","LetterSound/j.ogg", "LetterSound/k.ogg","LetterSound/l.ogg","LetterSound/m.ogg","LetterSound/n.ogg","LetterSound/o.ogg","LetterSound/p.ogg","LetterSound/q.ogg","LetterSound/r.ogg", "LetterSound/s.ogg","LetterSound/t.ogg", "LetterSound/u.ogg","LetterSound/v.ogg", "LetterSound/w.ogg","LetterSound/x.ogg","LetterSound/y.ogg","LetterSound/z.ogg")
	
	InB =("Badger","Bear","Beaver","Bee","Bison","Blackbird","Bull")	
	InBDesc =("bDesc/badger.ogg","bDesc/bear.ogg","bDesc/beaver.ogg","bDesc/bee.ogg","bDesc/bison.ogg","bDesc/blackbird.ogg","bDesc/bull.ogg")
	InBImage =("bImage/badger.png","bImage/bear.png","bImage/beaver.png","bImage/bee.png","bImage/bison.png","bImage/blackbird.png","bImage/bull.png")
	InBSound =("bSound/badger.ogg","bSound/bear.ogg","bSound/beaver.ogg","bSound/bee.ogg","bSound/bison.ogg","bSound/blackbird.ogg","bSound/bull.ogg")
	
	InC =("Camel","Chimp","Cow","Crow","Cuckoo")
	InCDesc =("cDesc/camel.ogg","cDesc/chimp.ogg","cDesc/cow.ogg","cDesc/crow.ogg","cDesc/cuckoo.ogg")
	InCImage=("cImage/camel.png","cImage/chimp.png","cImage/cow.png","cImage/crow.png","cImage/cuckoo.png")
	InCSound =("cSound/camel.ogg","cSound/chimp.ogg","cSound/cow.ogg","cSound/crow.ogg","cSound/cuckoo.ogg")
	
	InD = ("Deer","Dog","Dolphin","Donkey","Dromedary","Duck")
	InDDesc =("dDesc/deer.ogg", "dDesc/dog.ogg","dDesc/dolphin.ogg","dDesc/donkey.ogg","dDesc/dromedary.ogg","dDesc/duck.ogg"      ) 
	InDImage= ("dImage/deer.png","dImage/dog.png","dImage/dolphin.png","dImage/donkey.png","dImage/dromedary.png","dImage/duck.png")
	InDSound = ("dSound/deer.ogg","dSound/dog.ogg","dSound/dolphin.ogg","dSound/donkey.ogg","dSound/dromdary.ogg","dSound/duck.ogg")
	
	InF = ("Ferret","Fly","Fox","Frog")
	InFDesc = ("fDesc/ferret.ogg","fDesc/fly.ogg","fDesc/fox.ogg","fDesc/frog.ogg")
	InFImage = ("fImage/ferret.png","fImage/fly.png","fImage/fox.png","fImage/frog.png")
	InFSound =("fSound/ferret.ogg","fSound/fly.ogg","fSound/fox.ogg","fSound/frog.ogg")
	
	InG =("Gander","Giraffe","Goat","Gorilla","Grasshopper")
	InGDesc =("gDesc/gander.ogg","gDesc/giraffe.ogg","gDesc/goat.ogg","gDesc/gorilla.ogg","gDesc/grasshopper.ogg")
	InGImage =("gImage/gander.png","gImage/giraffe.png","gImage/goat.png","gImage/gorilla.png","gImage/grasshopper.png")
	InGSound = ("gSound/gander.ogg","gSound/giraffe.ogg","gSound/goat.ogg","gSound/gorilla.ogg","gSound/grasshopper.ogg")
	
	InH =("Hen","Hippopotamus","Hornet","Horse")
	InHDesc =("hDesc/hen.ogg","hDesc/hippopotamus.ogg","hDesc/hornet.ogg","hDesc/horse.ogg")
	InHImage =("hImage/hen.png","hImage/hippopotamus.png","hImage/hornet.png","hImage/horse.png")
	InHSound =("hSound/hen.ogg","hSound/hippopotamus.ogg","hSound/hornet.ogg","hSound/horse.ogg")
	
	InL =  ("Lark","Lion")
	InLDesc = ("lDesc/lark.ogg","lDesc/lion.ogg")
	InLImage = ("lImage/lark.png","lImage/lion.png")
	InLSound = ("lSound/lark.ogg","lSound/lion.ogg")
		
	InM =   ("Mountaingoat","Mouse")
	InMDesc = ("mDesc/mountaingoat.ogg","mDesc/mouse.ogg")
	InMImage = ("mImage/mountaingoat.png","mImage/mouse.png")
	InMSound =("mSound/mountaingoat.ogg","mSound/mouse.ogg")
	
	InO =     ("Orca","Otter","Owl")
	InODesc = ("oDesc/orca.ogg","oDesc/otter.ogg","oDesc/owl.ogg")
	InOImage = ("oImage/orca.png","oImage/otter.png","oImage/owl.png")
	InOSound =("oSound/orca.ogg", "oSound/otter.ogg","oSound/owl.ogg"     )
	
	
	InP =("Peacock","Penguin","Pig","Pidgeon")		
	InPImage =("pImage/peacock.png","pImage/penguin.png","pImage/pig.png","pImage/pigeon.png")
	InPSound =("pSound/peacock.ogg","pSound/penguin.ogg","pSound/pig.ogg","pSound/pigeon.ogg")
	InPDesc = ("pDesc/peacock.ogg","pDesc/penguin.ogg","pDesc/pig.ogg","pDesc/pigeon.ogg")
		
	InT = ("Tiger","Tucan","Turkey")
	InTDesc =  ("tDesc/tiger.ogg","tDesc/tucan.ogg","tDesc/turkey.ogg")
	InTImage = ("tImage/tiger.png","tImage/tucan.png","tImage/turkey.png")
	InTSound =  ("tSound/tiger.ogg","tSound/tucan.ogg","tSound/turkey.ogg")
	
	InW   =  ("Whale","Wolf")
	InWDesc  = ("wDesc/whale.ogg","wDesc/wolf.ogg")
	InWImage = ("wImage/whale.png","wImage/wolf.png")
	InWSound  = ("wSound/whale.ogg","wSound/wolf.ogg")
		
	InAnimal = ("Ant","b","c","d","Elepant","f","g","h","Iguana","Jay","Koala","l","m","Nandou","o","p","Quetzal","Rooster","Seagull","t","Urchin","Vulture","w","Xanthia","Yak","Zebra")
	InAnimalDesc = ("animDesc/ant.ogg","blank.ogg","blank.ogg","blank.ogg","animDesc/elephant.ogg","blank.ogg","blank.ogg","blank.ogg","animDesc/iguana.ogg","animDesc/jay.ogg","animDesc/koala.ogg","l.ogg","m.ogg","animDesc/nandou.ogg","o.ogg","p.ogg","animDesc/quetzal.ogg","animDesc/rooster.ogg","animDesc/seagull.ogg","t.ogg","animDesc/urchin.ogg","animDesc/vulture.ogg","w.ogg","animDesc/xanthia.ogg","animDesc/yak.ogg","animDesc/zebra.ogg")
	InAnimalImage= ("animImages/ant.png","b","c","d","animImages/elephant.png","f","g","h","animImages/iguana.png", "animImages/jay.png", "animImages/koala.png","l","m", "animImages/nandou.png","O","P", "animImages/quetzal.png", "animImages/rooster.png", "animImages/seagull.png","T", "animImages/urchin.png", "animImages/vulture.png", "w","animImages/xanthia.png", "animImages/yak.png", "animImages/zebra.png" )	
	InAnimalSound =  ("animSound/ant.ogg","blank.ogg","blank.ogg","blank.ogg","animSound/elephant.ogg","blank.ogg","blank.ogg","blank.ogg","animSound/iguana.ogg","animSound/jay.ogg","animSound/koala.ogg","blank.ogg","blank.ogg","animSound/nandou.ogg","blank.ogg","blank.ogg","animSound/quetzal.ogg","animSound/rooster.ogg","animSound/seagull.ogg","blank.ogg","animSound/urchin.ogg","animSound/vulture.ogg","blank.ogg","animSound/xanthia.ogg","animSound/yak.ogg","animSound/zebra.ogg")
	
	'''
	a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
	0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15  16 17 18 19 20 21 22 23 24 25

	'''	
	#remember white text will disappear ifabove used!
	red = [1,0,0,1]
	green = [0,1,0,1]
	blue =  [0,0,1,1]
	purple = [1,0,1,1]
	alphaLetter = ObjectProperty()
	animalName = ObjectProperty()
	rect_source= StringProperty('backgroundFirst.png')
	
	def __init__(self,**kwargs):
		super(Andy,self).__init__(**kwargs)
		self.source='background.png' 
		self.alphaLetter.text = "[color=5253e2]"+ 'LearnABC'
		self.animalName.text =  "[color=000000]"+ 'Duck'
		
	
	def update(self):
		
		self.count = self.count+1
		
		if self.count >= 26:
			self.count = 0  
			#above makes sure count doesnt go above lenth of alphabet
		if (self.sound1.state =='play'):
			self.sound1.stop()	
		if (self.sound2.state =='play'):
			self.sound2.stop()	
		if (self.sound3.state =='play'):
			self.sound3.stop()	
		#did above because if user clicks through to new card , then second & third sound of old card may still be playing  
		
		#whatever count is we need to get aplahpabet letter & sound of letter
		# this will be the same for every case 
		
		self.alphaLetter.text = "[color=000000]"+self.getLetter(self.count)
		#above deals with showing letter of Aplhabet this is independent of animal
		self.theSound = self.getLetterSound(self.count)
		self.sound1 =  SoundLoader.load(self.theSound)
		self.sound1.play()
		#deals with audio of letter of alphabet,again independent of animal
		
		
		
		#now for specific animal details dependig on whether there are options
		
		
		if self.count == 1: #B
			self.subcount = randint(0,6)
			#7 possible animals in B inventery
			
			self.tempAnimImage = self.InBImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InBSound
			
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InBDesc
			self.tempAnimNoun = self.InB
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		elif self.count == 2: #C
			self.subcount = randint(0,4)
			#5 possible animals in c inventery
			self.tempAnimImage = self.InCImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InCSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InCDesc
			self.tempAnimNoun = self.InC
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
			
			
		elif self.count == 3: #D
			self.subcount = randint(0,5)
			# possible animals in  inventery
			self.tempAnimImage = self.InDImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InDSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InDDesc
			self.tempAnimNoun = self.InD
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
			
		
		elif self.count == 5: #F
			self.subcount = randint(0,3)
			# possible animals in  inventery
			self.tempAnimImage = self.InFImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InFSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InFDesc
			self.tempAnimNoun = self.InF
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
			
		
		elif self.count == 6: #G
			self.subcount = randint(0,4)
			# possible animals in  inventery
			self.tempAnimImage = self.InGImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InGSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InGDesc
			self.tempAnimNoun = self.InG
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		elif self.count == 7: #H
			self.subcount = randint(0,3)
			# possible animals in  inventery
			self.tempAnimImage = self.InHImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InHSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InHDesc
			self.tempAnimNoun = self.InH
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		
		elif self.count == 11: #L
			self.subcount = randint(0,1)
			# possible animals in  inventery
			self.tempAnimImage = self.InLImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InLSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InLDesc
			self.tempAnimNoun = self.InL
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		elif self.count == 12: #M
			self.subcount = randint(0,1)
			# possible animals in  inventery
			self.tempAnimImage = self.InMImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InMSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InMDesc
			self.tempAnimNoun = self.InM
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		elif self.count == 14: #O
			self.subcount = randint(0,2)
			# possible animals in  inventery
			self.tempAnimImage = self.InOImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InOSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InODesc
			self.tempAnimNoun = self.InO
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		
		elif self.count == 15: #P
			self.subcount = randint(0,3)
			# possible animals in  inventery
			self.tempAnimImage = self.InPImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InPSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InPDesc
			self.tempAnimNoun = self.InP
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		
		elif self.count == 19: #T
			self.subcount = randint(0,2)
			# possible animals in  inventery
			self.tempAnimImage = self.InTImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InTSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InTDesc
			self.tempAnimNoun = self.InT
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		
		elif self.count == 22: #W
			self.subcount = randint(0,1)
			# possible animals in  inventery
			self.tempAnimImage = self.InWImage
			self.rect_source = self.allImages()
			self.tempAnimSound = self.InWSound
			self.sound1.bind (on_stop  = self.allAnimalNoise)
			self.tempAnimDesc = self.InWDesc
			self.tempAnimNoun = self.InW
			self.animalName.text = "[color=df00ff]"+self.allAnimNoun(self.subcount)
		
		
		else:
			self.rect_source = self.remainderImages(self.count) 
			self.animalName.text = "[color=df00ff]"+self.InAnimal[self.count]
			self.sound1.bind (on_stop  = self.remainderNoise)
			self.subcount = 0
		
		
		
	def getLetter(self,x):
		self.y= x
		self.letter= self.InAlphabet[self.y]
		return self.letter 
	
	def getLetterSound(self,x):
		self.y = x
		self.letterSound = self.InventeryLs[self.y]
		return  self.letterSound   
		
	
	
	
	def getAnimalDesc(self,instance):
		self.getAnDesc = self.InPDesc[self.subcount]
		self.sound2 = SoundLoader.load(self.getAnDesc) 
		self.sound2.play()
	
	def animalN(self,x):
		self.y = x
		self.getAnimalName = self.InAnimName[self.y]
		return self.getAnimalName 
	
	def allImages(self):
		self.theImage = self.tempAnimImage[self.subcount]
		return self.theImage
		
	def allAnimalNoise(self,instance):
		self.beastNoise = self.tempAnimSound[self.subcount]
		self.sound2= SoundLoader.load(self.beastNoise)
		self.sound2.play()
		self.sound2.bind (on_stop  = self.allAnimalDesc)
		
		
	def allAnimalDesc(self,instance):
		self.beastDesc = self.tempAnimDesc[self.subcount]	
		self.sound3 = SoundLoader.load(self.beastDesc)
		self.sound3.play()
	
	
		
	def allAnimNoun(self,x):
		self.y = x
		self.beastNoun = self.tempAnimNoun[self.y]
		return self.beastNoun
	
	
	def remainderImages(self,x):
		self.y = x
		
		self.beastyImage = self.InAnimalImage[self.y]
		return self.beastyImage
		
	
	def remainderNoise(self,instance):
		 
		self.beastNoise = self.InAnimalSound[self.count]
		self.sound2= SoundLoader.load(self.beastNoise)
		self.sound2.play()
		self.sound2.bind (on_stop  = self.remainderDesc)

	def remainderDesc(self,instance):
		self.beastyN = self.InAnimalDesc[self.count]
		self.sound3 = SoundLoader.load(self.beastyN)
		self.sound3.play()
	




class LearnABC(App):
	def build(self):
		return Andy()
		
		
		
		


if __name__ == '__main__':
		LearnABC().run() 
 
