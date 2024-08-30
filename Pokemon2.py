from tabulate import tabulate 

import random, time 


class pokemon:
  def __init__(self):
    self.Name=None
    self.Type=None
    self.Lvl=1
    self.MaxXP=10
    self.Exp=0
    self.MaxHP=0
    self.HP=0
    self.Atk=0
    self.Def=0
    self.Rarity=None
    self.randomHP=None
    self.randomAtk=None
    self.randomDef=None


  def LevelUp(self):
    print()
    print(f"| Your pokemon {self.Name} just leveled up to level {self.Lvl+1}! |")
    input()
    print(f"Level : {self.Lvl} + 1")
    time.sleep(0.1)
    print(f"MaxHP : {self.MaxHP} +", round(0.5*(self.Lvl+10)))
    time.sleep(0.1)
    print(f"MaxExp: {self.MaxXP} +", 2*self.Lvl+10)
    time.sleep(0.1)
    print(f"ATK   : {self.Atk} +", round(0.15*(self.Lvl+10)))
    time.sleep(0.1)
    print(f"DEF   : {self.Def} +", round(0.1*(self.Lvl+5)))
    input()
    self.Exp=self.Exp-self.MaxXP
    self.MaxHP=self.MaxHP+round(0.5*(self.Lvl+10))
    self.MaxXP=self.MaxXP+round(2*self.Lvl+10)
    self.HP=self.MaxHP
    self.Atk=self.Atk+round(0.15*(self.Lvl+10))
    self.Def=self.Def+round(0.1*(self.Lvl+5))
    self.Lvl=self.Lvl+1
    if self.checkExp():
      self.LevelUp()
    else:
      print("Here are its new stats:")
      time.sleep(0.5)
      self.ViewStatus()
      input()
      return True


  def GetExp(self,XP):
    self.Exp = self.Exp + XP
    if self.checkExp():
      self.LevelUp()

  def checkExp(self):
    if (self.Exp >= self.MaxXP):
      return True

  def StartingView(self):
    print("Here is its stats: ")
    time.sleep(0.5)
    print(self.Name)
    time.sleep(0.05)
    print(f"Type : {self.Type}")
    time.sleep(0.05)
    print(f"HP   : {self.HP} / {self.MaxHP}")
    time.sleep(0.05)
    print(f"ATK  : {self.Atk}")
    time.sleep(0.05)
    print(f"DEF  : {self.Def}")


  def ViewStatus(self):
    print(f":: {self.Name} ::",)
    time.sleep(0.05)
    print(f"Type : {self.Type}")
    time.sleep(0.05)
    print(f"Level: {self.Lvl}")
    time.sleep(0.05)
    print(f"HP   : {self.HP} / {self.MaxHP}")
    time.sleep(0.05)
    print(f"Exp  : {self.Exp} / {self.MaxXP}")
    time.sleep(0.05)
    print(f"ATK  : {self.Atk}")
    time.sleep(0.05)
    print(f"DEF  : {self.Def}")
    

  def BattleView(self): 
    a = 10
    b = a-len(self.Name)
    c = ""
    i = 1
    while i <= b:
      c = c + " "
      i = i+1
    print(f":: {self.Name} ::" + c + "--", end='  ')
    print(f"Type: {self.Type}", end='  ')
    print(f"Level: {self.Lvl}", end='  ')
    print(f"HP: {self.HP} / {self.MaxHP}")

  def randomiser(self):
    self.Atk = eval(self.randomAtk)
    self.Def = eval(self.randomDef)
    self.HP = eval(self.randomHP)
    self.MaxHP = self.HP
    self.Exp = round(self.Def)+round(self.Atk/2)+round(self.HP/2)
    a = 1
    i = 0
    while i <= 200:
      i = i + 7
      if self.Exp <= i:
        self.Lvl = a
        break
      a = a + 1

  def makePokemon(self, pokemon):
    global pokemonNumber
    self.Type = pokemon.Type
    self.Lvl = pokemon.Lvl
    self.HP = pokemon.HP
    self.MaxHP = pokemon.MaxHP
    self.Def = pokemon.Def
    self.Atk = pokemon.Atk
    self.Name = pokemon.Name
    i = 0
    while i < 7:
      try:
        PokemonTable[i].append(pokemonNumber)
        i = i + 1
      except:
        j = 0
        while j < 7:
          PokemonTable.append([])
          j = j + 1
    i = 1
    while i < pokemon.Lvl:
      self.MaxXP = self.MaxXP+round(2*i+10) 
      i = i + 1
    self.Exp = 0






class trainer:
  def __init__(self):
    self.Name = None
    self.Money = 0
    self.Pokemon = pokemonlist
    self.current = pokemon()


  def ViewStatus(self):
    print()
    print("===PlayerStats===")
    print("PlayerName:", self.Name)
    print("Money     : ₽" + str(self.Money))
    print("===========Pokemon==========")
    self.ViewPokemon()
    

  def ViewPokemon(self):
    global pokemonNumber
    i = 0
    while i < pokemonNumber:
      PokemonTable[0][i] = f"  :: {self.Pokemon[i].Name} :: "
      PokemonTable[1][i] = f"Type: {self.Pokemon[i].Type}"
      PokemonTable[2][i] = f"Lvl : {self.Pokemon[i].Lvl}"
      PokemonTable[3][i] = f"HP  : {self.Pokemon[i].HP} / {self.Pokemon[i].MaxHP}"
      PokemonTable[4][i] = f"Exp : {self.Pokemon[i].Exp} / {self.Pokemon[i].MaxXP}"
      PokemonTable[5][i] = f"Atk : {self.Pokemon[i].Atk}"
      PokemonTable[6][i] = f"Def : {self.Pokemon[i].Def}"
      i = i + 1
    print(tabulate(PokemonTable, headers="firstrow"))

  def checkLvl(self,GymLvl):
    global pokemonNumber
    i = 0
    while i < pokemonNumber: 
      if self.Pokemon[i].Lvl >= GymLvl:
        return True
      i = i + 1
    else:
      return False

  def checkPokemon(self):
    global pokemonNumber
    i = 0
    while i < pokemonNumber: 
      if self.Pokemon[i].HP > 0:
        return True
      i = i + 1
    else:
      return False
  

  def setPokemon(self,pokemon):
    global pokemonNumber
    pokemonNumber = pokemonNumber + 1
    self.Pokemon[pokemonNumber-1].makePokemon(pokemon)


  def changePokemon(self, choosen, Faint):
    global pokemonNumber
    print()
    try:
      print("===Pokemons===")
      a = 0
      while a < pokemonNumber:
        print(f"|{a+1}| {self.Pokemon[a].Name}")
        a = a + 1
      print("==============")
      player.ViewPokemon()
      print()
      try:
        b = int(input("Which pokemon to change to? "))
      except:
        changePokemon(self, choosen, Faint)
      if Faint == True:
        if self.Pokemon[b-1].HP == 0:
          print("This pokemon has fainted")
          time.sleep(1)
          self.changePokemon(choosen, Faint)
          pass
        else:
          self.current = self.Pokemon[b-1]
          print(f"Pokemon changed to {self.current.Name} ")
          print()
      elif Faint == False:
        if self.current == self.Pokemon[b-1]:
          pass
        else:
          self.current = self.Pokemon[b-1]
          print(f"Pokemon changed to {self.current.Name} ")
          time.sleep(1)
          print()
          checkType(choosen)
          EnemyAttack(choosen)
    except:
      ("No choice was taken.")

  def Heal(self, condition):
    global pokemonNumber
    a = False
    i = 0
    while i < pokemonNumber:
      if self.Pokemon[i].HP == self.Pokemon[i].MaxHP:
        i = i + 1
        continue
      elif self.Pokemon[i].HP != self.Pokemon[i].MaxHP:
        print(f"Healing {self.Pokemon[i].Name}... ")
        time.sleep(1)
        self.Pokemon[i].HP = self.Pokemon[i].MaxHP
        a = True
      i = i + 1
    print()
    if a == True:
      print("All of your pokemons are now fully healed!")
    if a == False:
      print("All of your pokemons are already full HP")
      pass 
    time.sleep(1)
    if condition == True:
      player.current = player.Pokemon[0]
      Pokecenter(condition)
 

  def Bag(self):
    global Healpotion, pokeBall, rareBall, epicBall
    print("=====Player Bag=====")
    print(f"|1| Heal potion  : {Healpotion}x")
    print(f"|2| Pokeball     : {pokeBall}x")
    print(f"|3| Rare pokeball: {rareBall}x")
    print(f"|4| Epic pokeball: {epicBall}x")
    input()

  def useable(self, world):
    global Healpotion, pokeBall, rareBall, epicBall
    Healpotion = Healpotion
    i = True
    while i == True:
      print("=====Player Bag=====")
      print(f"|1| Heal potion  : {Healpotion}x")
      print(f"|2| Pokeball     : {pokeBall}x")
      print(f"|3| Rare pokeball: {rareBall}x")
      print(f"|4| Epic pokeball: {epicBall}x")
      print()
      a = input("Which item do you want to use? ")
      try:
        if a == "1":
          if Healpotion == 0:
            print("You don't have any Healpotion.")
            time.sleep(1)
            break
          else:
            b = "Healpotion"
        elif a == "2":
          if pokeBall == 0:
            print("You don't have any Pokeball.")
            time.sleep(1)
            break
          else:
            b = "Pokeball"
        elif a == "3":
          if rareBall == 0:
            print("You don't have any Rare Pokeball.")
            time.sleep(1)
            break
          else:
            b = "Rare Pokeball"
        elif a == "4":
          if epicBall == 0:
            print("You don't have any Epic Ball.")
            time.sleep(1)
            break
          else:
            b = "Epic Pokeball" 
        if pokemonNumber == 3:
          print("You have max number of pokemons already.")
          break
        c = input(f"Are you sure you want to use {b}? ")
        a = int(a)
        if c in  ("Yes", "y", "yes","Y"):
          print(f"Using {b}...")
          time.sleep(1)
          if a == 1:
            player.current.HP = player.current.MaxHP
            Healpotion = Healpotion - 1
            print(f"Your pokemon HP {player.current.Name} has been restored.")
            time.sleep(1)
            break
          else:
            if pokemonNumber == 3:
              print("Cannot use Pokeball [Pokemon List Full")
              time.sleep(1)
            else:
              world.catchChance(b)
              break
        elif c in ("No", "n", "no"):
          pass
        else:
          break
      except:
        break





class worldChance:
  def __init__(self):
    self.chance1=None
    self.chance2=None
    self.chance3=None
    self.chance4=None
    self.chance5=None
    self.chance6=None
    self.choosen=pokemon()
    self.pokemon=[]
    self.Name=None
  

  def appearPokemon(self):
    i = eval("random.randint(0, 100)")
    if i  <= self.chance6:
      self.choosen = self.pokemon[5]
    elif i <= self.chance5:
      self.choosen = self.pokemon[4]
    elif i <= self.chance4:
      self.choosen = self.pokemon[3]
    elif i <= self.chance3:
      self.choosen = self.pokemon[2]
    elif i <= self.chance2:
      self.choosen = self.pokemon[1]
    elif i <= self.chance1:
      self.choosen = self.pokemon[0]
    self.choosen.randomiser()
    Battle(self, self.choosen)

  def catchChance(self, BallType):
    global pokeBall, rareBall, epicBall, catched
    a = 0
    if BallType == "Pokeball":
      a = 100
      pokeBall = pokeBall - 1
    elif BallType == "Rare Pokeball":
      a = 115
      rareBall = rareBall - 1
    elif BallType == "Epic Pokeball":
      a = 130
      epicBall = epicBall - 1
    if self.choosen.Rarity == "Common":
      a = a - 20
    elif self.choosen.Rarity == "Uncommon":
      a = a - 30
    elif self.choosen.Rarity == "Rare":
      a = a - 40
    elif self.choosen.Rarity == "Very Rare":
      a = a - 50
    elif self.choosen.Rarity == "Super Rare":
      a = a - 70
    elif self.choosen.Rarity == "Epic":
      a = a - 90
    b = eval("random.randint(0, 100)")
    if b <= a:
      print("Pokemon successfully catched!")
      player.setPokemon(self.choosen)
      time.sleep(1)
      i = True
      j = True
      while i == True:
        a = input("What do you wish to call your new pokemon? ")
        while j == True:
          player.Pokemon[pokemonNumber-1].Name = a
          print("Pokemon name " + player.Pokemon[pokemonNumber-1].Name + "? (Yes/No) ", end='')
          b = input() 
          if b in  ("Yes", "y", "yes","Y"):
            i = False
            print()
            break
          elif b in ("No", "n", "no"):
            j = False 
      catched = True
    else:
      print("Pokemon failed to be catched!")
      print()
      time.sleep(1)
      checkType(self, self.choosen)
      EnemyAttack(self, self.choosen)
    print()





#pokemon related
pokemon1 = pokemon()
pokemon2 = pokemon()
pokemon3 = pokemon()
pokemonlist = [pokemon1, pokemon2, pokemon3]
starting = []
pokemon1.MaxExp = 10
PokemonTable = []
BattlePlayer = [1,2,3,4,5]
BattleEnemy  = [1,2,3,4,5]
textplayer = ""
textenemy = ""
pAttack = 0
eAttack = 0
Healpotion = 0
pokeBall = 0
rareBall = 0
epicBall = 0
pokemonNumber = 0
catched = False
"""
BattleTable = [[1,2],[1,2],[1,2],
              [1,2],[1,2],[1,2]] """

#starting
bulbasaur = pokemon()
bulbasaur.Name = "Bulbasaur"
bulbasaur.Type = "Grass"
bulbasaur.Rarity = "Very Rare"
bulbasaur.randomHP = "random.randint(18, 24)"
bulbasaur.randomAtk = "random.randint(8, 12)"
bulbasaur.randomDef = "random.randint(3, 5)"

squirtle = pokemon()
squirtle.Name = "Squirtle"
squirtle.Type = "Water"
squirtle.Rarity = "Common"
squirtle.randomHP = "random.randint(20, 28)"
squirtle.randomAtk = "random.randint(14, 16)"
squirtle.randomDef = "random.randint(0, 1)"

charmander = pokemon()
charmander.Name = "Charmander"
charmander.Type = "Fire"
charmander.Rarity = "Uncommon"
charmander.randomHP = "random.randint(15, 18)"
charmander.randomAtk = "random.randint(18, 24)"
charmander.randomDef = "random.randint(1, 3)"


#Viridianforest
oddish = pokemon()
oddish.Name = "Oddish"
oddish.Type = "Grass"
oddish.Rarity = "Common"
oddish.randomHP = "random.randint(10, 15)"
oddish.randomAtk = "random.randint(6, 10)"
oddish.randomDef = "random.randint(1, 3)"

paras = pokemon()
paras.Name = "Paras"
paras.Type = "Grass"
paras.Rarity = "Uncommon"
paras.randomHP = "random.randint(12, 20)"
paras.randomAtk = "random.randint(12, 15)"
paras.randomDef = "random.randint(0, 1)"

bellsprout = pokemon()
bellsprout.Name = "Bellsprout"
bellsprout.Type = "Grass"
bellsprout.Rarity = "Rare"
bellsprout.randomHP = "random.randint(15, 22)"
bellsprout.randomAtk = "random.randint(14, 16)"
bellsprout.randomDef = "random.randint(1, 2)"

tangela = pokemon()
tangela.Name = "Tangela"
tangela.Type = "Grass"
tangela.Rarity = "Super Rare"
tangela.randomHP = "random.randint(25, 30)"
tangela.randomAtk = "random.randint(8, 12)"
tangela.randomDef = "random.randint(3, 5)"

exeggutor = pokemon()
exeggutor.Name = "Exeggutor"
exeggutor.Type = "Grass"
exeggutor.Rarity = "Epic"
exeggutor.randomHP = "random.randint(35, 50)"
exeggutor.randomAtk = "random.randint(15, 24)"
exeggutor.randomDef = "random.randint(2, 4)"

viridian = worldChance()
viridian.chance1 = 100
viridian.chance2 = 80
viridian.chance3 = 65
viridian.chance4 = 40
viridian.chance5 = 25
viridian.chance6 = 10
viridian.pokemon = [oddish, paras, bellsprout, bulbasaur, tangela, exeggutor]
viridian.Name = "Forest"


#Mt. DeepGreen 
growlithe = pokemon()
growlithe.Name = "Growlithe"
growlithe.Type = "Fire"
growlithe.Rarity = "Common"
growlithe.randomHP = "random.randint(13, 15)"
growlithe.randomAtk = "random.randint(8, 12)"
growlithe.randomDef = "random.randint(2, 4)"

magmar = pokemon()
magmar.Name = "Magmar"
magmar.Type = "Fire"
magmar.Rarity = "Rare"
magmar.randomHP = "random.randint(15, 20)"
magmar.randomAtk = "random.randint(15, 20)"
magmar.randomDef = "random.randint(0, 3)"

flareon = pokemon()
flareon.Name = "Flareon"
flareon.Type = "Fire"
flareon.Rarity = "Very Rare"
flareon.randomHP = "random.randint(35, 42)"
flareon.randomAtk = "random.randint(11, 14)"
flareon.randomDef = "random.randint(6, 8)"

ponytha = pokemon()
ponytha.Name = "Ponytha"
ponytha.Type = "Fire"
ponytha.Rarity = "Super Rare"
ponytha.randomHP = "random.randint(40, 50)"
ponytha.randomAtk = "random.randint(16, 21)"
ponytha.randomDef = "random.randint(3, 5)"

vulpix = pokemon()
vulpix.Name = "Vulpix"
vulpix.Type = "Fire"
vulpix.Rarity = "Epic"
vulpix.randomHP = "random.randint(60, 70)"
vulpix.randomAtk = "random.randint(28, 32)"
vulpix.randomDef = "random.randint(4, 6)"

deepgreen = worldChance()
deepgreen.chance1 = 100
deepgreen.chance2 = 90
deepgreen.chance3 = 70
deepgreen.chance4 = 50
deepgreen.chance5 = 35
deepgreen.chance6 = 15
deepgreen.pokemon = [growlithe, charmander, magmar, flareon, ponytha, vulpix]
deepgreen.Name = "Mountain"


#Cinnabar Island
tentacool = pokemon()
tentacool.Name = "Tentacool"
tentacool.Rarity = "Uncommon"
tentacool.Type = "Water"
tentacool.randomHP = "random.randint(43, 50)"
tentacool.randomAtk = "random.randint(12, 15)"
tentacool.randomDef = "random.randint(5, 7)"

slowpoke = pokemon()
slowpoke.Name = "Slowpoke"
slowpoke.Rarity = "Rare"
slowpoke.Type = "Water"
slowpoke.randomHP = "random.randint(56, 64)"
slowpoke.randomAtk = "random.randint(17, 20)"
slowpoke.randomDef = "random.randint(8, 15)"

psyduck = pokemon()
psyduck.Name = "Psyduck"
psyduck.Rarity = "Very Rare"
psyduck.Type = "Water"
psyduck.randomHP = "random.randint(46, 52)"
psyduck.randomAtk = "random.randint(19, 23)"
psyduck.randomDef = "random.randint(4, 6)"

poliwag = pokemon()
poliwag.Name = "Poliwag"
poliwag.Rarity = "Super Rare"
poliwag.Type = "Water"
poliwag.randomHP = "random.randint(68, 75)"
poliwag.randomAtk = "random.randint(25, 30)"
poliwag.randomDef = "random.randint(6, 8)"

gyarados = pokemon()
gyarados.Name = "Gyarados"
gyarados.Rarity = "Epic"
gyarados.Type = "Water"
gyarados.randomHP = "random.randint(110, 130)"
gyarados.randomAtk = "random.randint(32, 38)"
gyarados.randomDef = "random.randint(15, 18)"

cinnabar = worldChance()
cinnabar.chance1 = 100
cinnabar.chance2 = 90
cinnabar.chance3 = 80
cinnabar.chance4 = 55
cinnabar.chance5 = 30
cinnabar.chance6 = 15
cinnabar.pokemon = [squirtle, tentacool, slowpoke, psyduck, poliwag, gyarados]
cinnabar.Name = "Island"


#Gym pokemon
lapras = pokemon()
lapras.Name = "Lapras"
lapras.Type = "Water"
lapras.randomHP = "random.randint(90, 100)"
lapras.randomAtk = "random.randint(30, 35)"
lapras.randomDef = "random.randint(8, 10)"

rapidash = pokemon()
rapidash.Name = "Rapidash"
rapidash.Type = "Fire"
rapidash.randomHP = "random.randint(80, 84)"
rapidash.randomAtk = "random.randint(40, 45)"
rapidash.randomDef = "random.randint(5, 8)"

vileplume = pokemon()
vileplume.Name = "Vileplume"
vileplume.Type = "Grass"
vileplume.randomHP = "random.randint(88, 94)"
vileplume.randomAtk = "random.randint(34, 38)"
vileplume.randomDef = "random.randint(10, 12)"

Gym = worldChance()
Gym.pokemon = []







#main story
print("\n")
print(r"                                  ,'\ ")
print(r"    _.----.        ____         ,'  _\   ___    ___     ____")
print(r"_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print(r"\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(r" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print(r"   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print(r"    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print(r"     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print(r"      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print(r"       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print(r"       \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print(r"                             `'                            '-._|")
print("\n")

i = True
while i == True:
  name = str(input("What's Your Name? "))
  if len(name) < 3:
    print("Name should be at least 3 letters")
    print()
  else:
    player = trainer()
    player.Name = name
    break
    

def Introduction():
  print()
  print("...: Hello", player.Name)
  time.sleep(1)
  print()
  print("...: My name is Professor Sycamore")
  time.sleep(2.5)
  print()
  print("Professor Sycamore: I am here to bring you towards a new world of pokemons")
  time.sleep(3)
  print()
  print("Professor Sycamore: Today I am going to give you a pokemon!")
  time.sleep(2)


i = True
while i == True:
  a = input("Skip Introduction? (Yes/No) ")
  if a in ("Yes", "y", "yes","Y"):
    print()
    f = False
    break
  elif a in ("No", "n", "no"):
    Introduction()
    f = True
    break


bulbasaur.randomiser()
squirtle.randomiser()
charmander.randomiser()
starting.append(bulbasaur)
starting.append(squirtle)
starting.append(charmander)


i = True
while i == True:
  print()
  print("Professor Sycamore: I have three choices:")
  time.sleep(1)
  print("1. Bulbasaur")
  time.sleep(.1)
  print("2. Squirtle")
  time.sleep(.1)
  print("3. Charmander")
  time.sleep(.5)
  print()

  j = True
  while j == True:
    try:
      b = int(input("Professor Sycamore: Which one do you wish to choose as your first pokemon? "))
      print()
      starting[b - 1].StartingView()
      i = True
      while i == True:
        print("Take " + str(starting[b - 1].Name) + "? (Yes/No) ", end='')
        c = input()
        if c in  ("Yes", "y", "yes","Y"):
          i = False
          j = False
          player.setPokemon(starting[b - 1])
          player.Pokemon[0].Lvl = 1
          player.Pokemon[0].MaxXP = 10
          player.current = player.Pokemon[0]
          print()
          print("Professor Sycamore: " + str(starting[b - 1].Name) + ", A glamourous pick!")
          time.sleep(1)
          break
        elif c in ("No", "n", "no"):
          j = False
          break
    except:
        print("Error")    

i = True
while i == True:
  print()
  player.Pokemon[0].Name = str(input("Professor Sycamore: Now, what should it be called? "))
  j = True
  if len(player.Pokemon[0].Name) < 3:
    print("Name should be at least 3 letters")
  else:
    while j == True:
      print("Pokemon name " + player.Pokemon[0].Name + "? (Yes/No) ", end='')
      a = input()
      if a in  ("Yes", "y", "yes","Y"):
        i = False
        print()
        break
      elif a in ("No", "n", "no"):
        j = False 

    
def Introduction2():
  global Healpotion
  print("Professor Sycamore: " + str(player.Pokemon[0].Name) + "! A nice name.")
  time.sleep(1.5)
  print()
  print("Professor Sycamore: Now before you go, let me tell you something first.")
  time.sleep(1.5)
  print()
  print("Professor Sycamore: You can defeat other pokemons in the wild to gain experience for your pokemon!")
  time.sleep(3)
  print()
  print("Professor Sycamore: You can also try to battle the people in the gym for pokedollars!")
  time.sleep(3)
  print("As you are starting new, I will be giving you a heal potion that will instantly heal a pokemon to its full HP!")
  time.sleep(3)
  Healpotion = Healpotion + 1
  print("Received Heal potion")
  input()
  print()
  print()
  print("Note: you can always type in \"quit\" to exit the game anytime.")
  time.sleep(3)

if f == True:
  Introduction2()

print("Professor Sycamore: Now, you are now ready for the adventure of the pokemon world!")
time.sleep(2)

q = False

#worlds
def ViridianCity():
    global q
    while q == False:
      if player.checkLvl(3):
        mountainLvl = ""
      else:
        mountainLvl = "[Requirement: Level 3 Pokemon]"
      if player.checkLvl(6):
        islandLvl = ""
      else:
        islandLvl = "[Requirement: Level 6 Pokemon]"
      if player.checkLvl(10):
        correctLvl = ""
      else:
        correctLvl = "[Requirement: Level 10 Pokemon]"
      print()
      print(r"                          .|")
      print(r"                          | |")
      print(r"                          |'|            ._____")
      print('                   ___    | |            |.   |\' .---"|')
      print(r"          _    .-'   '-. |  |     .--'|  ||   | _|    |")
      print(r"       .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
      print(r"       |' | |.    |    ||       | |   |  |    ||      |")
      print('       |  \'-\'     \'    ""       \'-\'   \'-.\'    \'`      |')
      print("=================================================================")
      time.sleep(0.05)
      print()
      print("                   You are now in ViridianCity                   ")
      time.sleep(0.05)
      print()
      print("=================================================================")
      time.sleep(0.05)
      print("|1| Go to Viridian Forest")
      time.sleep(0.05)
      print("|2| Go to Mt. DeepGreen  ", mountainLvl)
      time.sleep(0.05)
      print("|3| Go to Cinnabar Island", islandLvl)
      time.sleep(0.05)
      print("|4| Go to the Gym        ", correctLvl)
      time.sleep(0.05)
      print("|5| Go to the Pokecenter")
      time.sleep(0.05)
      print("-----------------------------------------------------------------")
      time.sleep(0.05)
      print("|O| Check Overall Stats")
      time.sleep(0.05)
      print("|I| Check Bag")
      time.sleep(0.05)
      print()
      time.sleep(0.05)
      a = str(input("What should I do? "))
      if a == "1":
        ViridianForest()
      elif a == "2":
        if player.checkLvl(3):
          MountainDeep()
        else:
          print("Your pokemon should be at least level 3 before entering Mt. Deep Green")
          time.sleep(0.5)
      elif a == "3":
        if player.checkLvl(6):
          CinnabarIsland()
        else:
          print("Your pokemon should be at least level 6 before entering the Cinnabar Island")
          time.sleep(0.5)
      elif a == "4":
        if player.checkLvl(10):
          ViridianGym()
        else:
          print("Your pokemon should be at least level 10 before entering the gym")
          time.sleep(0.5)
      elif a == "5":
        Pokecenter(False)
      elif a in ("O","o"):
        player.ViewStatus()
        input()
      elif a in ("I","i"):
        player.Bag()
      elif a == "quit":
        ExitGame()
      else:
        print("No choice was taken.")
      
def ViridianForest():
  global q
  while q == False:
    print()
    print(r"              _-_              _-_              _-_       ")
    print(r"           /       \        /       \        /       \    ")
    print(r"        /            \    /           \    /           \ ")
    print(r"       {               }{               }{               }")
    print(r"        \  _-     -_  /  \  _-     -_  /  \  _-     -_  /")
    print(r"          ~  \\ //  ~      ~  \\ //  ~      ~  \\ //  ~  ")
    print(r"       _- -   | | _- _  _- -   | | _- _  _- -   | | _- _  ")
    print(r"         _ -  | |   -_    _ -  | |   -_    _ -  | |   -_ ")
    print(r"             // \\            // \\            // \\  ")
    print("=================================================================")
    time.sleep(0.05)
    print()
    print("                  You are now in ViridianForest                  ")
    time.sleep(0.05)
    print()
    print("=================================================================")
    time.sleep(0.05)
    print("|1| Search the forest")
    time.sleep(0.05)
    print("|2| Go back")
    time.sleep(0.05)
    print("-----------------------------------------------------------------")
    time.sleep(0.05)
    print("|O| Check Overall Stats")
    time.sleep(0.05)
    print("|I| Check Bag")
    time.sleep(0.05)
    print()
    time.sleep(0.05)
    a = str(input("What should I do? "))
    if a == "1":
      Search(viridian)
    elif a == "2":
      break
    elif a in ("O","o"):
      player.ViewStatus()
      input()
    elif a in ("I","i"):
      player.Bag()
    elif a == "quit":
      ExitGame()
    else:
      print("No choice was taken.")

def MountainDeep():
  global q
  while q == False:
    print()
    print(r"                                   /\ ")
    print(r"                              /\  //\\ ")
    print(r"                       /\    //\\///\\\        /\ ")
    print(r"                      //\\  ///\////\\\\  /\  //\\ ")
    print(r"         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \ ")
    print(r"        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \ ")
    print(r"       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       * ")
    print(r"      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\ ")
    print(r"     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\ ")
    print(r"    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\ ")
    print(r"   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\ ")
    print(r"  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\ ")
    print(r" / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |   ")
    print(r"/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooo")
    print("=================================================================")
    time.sleep(0.05)
    print()
    print("                    You are now in Mt. DeepGreen                 ")
    time.sleep(0.05)
    print()
    print("=================================================================")
    time.sleep(0.05)
    print("|1| Search the mountain")
    time.sleep(0.05)
    print("|2| Go back")
    time.sleep(0.05)
    print("-----------------------------------------------------------------")
    time.sleep(0.05)
    print("|O| Check Overall Stats")
    time.sleep(0.05)
    print("|I| Check Bag")
    time.sleep(0.05)
    print()
    time.sleep(0.05)
    a = str(input("What should I do? "))
    if a == "1":
      Search(deepgreen)
    elif a == "2":
      break
    elif a in ("O","o"):
      player.ViewStatus()
      input()
    elif a in ("I","i"):
      player.Bag()
    elif a == "quit":
      ExitGame()
    else:
      print("No choice was taken.")

def CinnabarIsland():
  global q
  while q == False:
    print(r"                        _")
    print(r"                       ;`',")
    print(r"                       `,  `,")
    print('                        \',   ;   ,,-""==..,')
    print(r"                         \    ','          \ ")
    print('                 ,-""\'-., ;    \'    __.-="-.;')
    print('               ," ,,_    "V      _."')
    print('              ;,\'   \'\'-,          "=--,_')
    print(r"                     ,-''    _  _       `,")
    print(r"                    /   ,.-+(_)(_)´--.,   ;")
    print(r"                   ,'  /   ; (_)       `\ ,")
    print(r"                   ; ,/    ;._.;         ;")
    print(r"                   !,'     ;   ;")
    print(r"                   V'      ;   ;")
    print(r"                           ;._.;")
    print(r"                           ;   ;")
    print(r"                           ;   ;        ~")
    print(r"            ~              ;._.;")
    print(r"                      ~    ;   ;")
    print(r"                          .´   `.                ~")
    print(r"                    __,.--;.___.;--.,___")
    print('              _,,-""      ;     ;       ""-,,_')
    print(r"          .-´´            ;     ;             ``-.")
    print('         ",              ´       `               ,"        ~')
    print('           "-_                                _-"')
    print(r"       ~       ``----..,_          __,,..bmw-´")
    print(r"                         ```''''´´´                  ~")
    print(r"                                     ~")
    print(r"                  ~")
    print("=================================================================")
    time.sleep(0.05)
    print()
    print("                 You are now in CinnabarIsland                   ")
    time.sleep(0.05)
    print()
    print("=================================================================")
    time.sleep(0.05)
    print("|1| Search the island")
    time.sleep(0.05)
    print("|2| Go back")
    time.sleep(0.05)
    print("-----------------------------------------------------------------")
    time.sleep(0.05)
    print("|O| Check Overall Stats")
    time.sleep(0.05)
    print("|I| Check Bag")
    time.sleep(0.05)
    print()
    time.sleep(0.05)
    a = str(input("What should I do? "))
    if a == "1":
      Search(cinnabar)
    elif a == "2":
      break
    elif a in ("O","o"):
      player.ViewStatus()
      input()
    elif a in ("I","i"):
      player.Bag()
    elif a == "quit":
      ExitGame()
    else:
      print("No choice was taken.")


def Search(world):
  a = eval("random.randint(0, 100)")
  print()
  if a <= 15:
    if world.Name == "Forest":
      b = eval("random.randint(25, 30)")
    elif world.Name == "Mountain":
      b = eval("random.randint(35, 40)")
    elif world.Name == "Island":
      b = eval("random.randint(55, 80)")
    print(f"You have found ₽{b} dollars!")
    player.Money = player.Money + b
    time.sleep(0.5)
  else:
    world.appearPokemon()

def Battle(world, choosen):
  global catched
  catched = False
  print(f"A wild {choosen.Name} has appeared!",)
  time.sleep(0.5)
  i = True
  while i == True:
    if catched == True:
      break
    viewBattle(choosen)
    print("Rarity:", choosen.Rarity)
    print()
    print("Actions: ")
    time.sleep(0.05)
    print("|1| Attack")
    time.sleep(0.05)
    print("|2| Change Pokemon")
    time.sleep(0.05)
    print("|3| Open Bag")
    time.sleep(0.05)
    print("|4| Flee")
    time.sleep(0.05)
    print()
    time.sleep(0.05)
    a = str(input(f"What should {player.current.Name} do? "))
    if a == "1":
      checkType(choosen)
      if Attack(choosen) == True:
        print()
        break
      else:
        EnemyAttack(choosen)
    elif a == "2":
      player.changePokemon(choosen, False)
    elif a == "3":
      player.useable(world)
    elif a == "4":
      break
    else:
      print("No choice was taken.")

def viewBattle(choosen):
    """
    i = 0
        BattleTable[0][i] = "======You======"
        BattleTable[1][i] = f":: {player.current.Name} ::"
        BattleTable[2][i] = ""
        BattleTable[3][i] = f"Type  : {player.current.Type}"
        BattleTable[4][i] = f"Lvl   : {player.current.Lvl}"
        BattleTable[5][i] = f"HP    : {player.current.HP} / {player.current.MaxHP}"
      elif i == 1:
        BattleTable[0][i] = "=====Enemy====="
        BattleTable[1][i] = f":: {world.choosen.Name} ::"
        BattleTable[2][i] = f"Rarity: {world.choosen.Rarity}"
        BattleTable[3][i] = f"Type  : {world.choosen.Type}"
        BattleTable[4][i] = f"Lvl   : {world.choosen.Lvl}"
        BattleTable[5][i] = f"HP    : {world.choosen.HP} / {world.choosen.MaxHP}"


    BattlePlayer[0] = f":: {player.current.Name} ::"
    BattlePlayer[1] = ""
    BattlePlayer[2] = f"Type  : {player.current.Type}"
    BattlePlayer[3] = f"Lvl   : {player.current.Lvl}"
    BattlePlayer[4] = f"HP    : {player.current.HP} / {player.current.MaxHP}"
    BattleEnemy[0] = f":: {world.choosen.Name} ::"
    BattleEnemy[1] = f"Rarity: {world.choosen.Rarity}"
    BattleEnemy[2] = f"Type  : {world.choosen.Type}"
    BattleEnemy[3] = f"Lvl   : {world.choosen.Lvl}"
    BattleEnemy[4] = f"HP    : {world.choosen.HP} / {world.choosen.MaxHP}"
    """
    print("======You======")
    player.current.BattleView()
    print("=====Enemy=====")
    choosen.BattleView()

def checkType(choosen):
  global textplayer, textenemy, pAttack, eAttack
  a = "It was not effective"
  b = "It was very effective"
  c = None
  pAtk = player.current.Atk
  eAtk = choosen.Atk
  d = round(choosen.Def/1.5)
  d2 = pAtk-d
  e = round(choosen.Def*1.5)
  e2 = pAtk-e
  f = round(player.current.Def/1.5)
  f2 = eAtk-f
  g = round(player.current.Def*1.5)
  g2 = eAtk-g

  if choosen.Type == player.current.Type:
    textplayer = c
    textenemy = c
    pAttack = player.current.Atk-choosen.Def
    eAttack = choosen.Atk-player.current.Def
    pass

  else:
    if choosen.Type == "Grass":
      if player.current.Type == "Water":
        pAttack = e2
        eAttack = f2
        textplayer = a
        textenemy = b
      if player.current.Type == "Fire":
        pAttack = d2
        eAttack = g2
        textplayer = b
        textenemy = a

    if choosen.Type == "Water":
      if player.current.Type == "Fire":
        pAttack = e2
        eAttack = f2
        textplayer = a
        textenemy = b
      if player.current.Type == "Grass":
        pAttack = d2
        eAttack = g2
        textplayer = b
        textenemy = a

    if choosen.Type == "Fire":
      if player.current.Type == "Grass":
        pAttack = e2
        eAttack = f2
        textplayer = a
        textenemy = b
      if player.current.Type == "Water":
        pAttack = d2
        eAttack = g2
        textplayer = b
        textenemy = a

def Attack(choosen):
  global textplayer, pAttack
  print()
  print(f"{player.current.Name} Attacks!")
  time.sleep(1)
  if pAttack <=0 :
    print(f"No damage was dealt to wild {choosen.Name}!")
    time.sleep(1)
  else:
    choosen.HP = choosen.HP-pAttack
    print(f"{pAttack} damage was dealt to wild {choosen.Name}.")
    time.sleep(1)
  while textplayer != None:
      print(textplayer)
      time.sleep(1)
      break
  if choosen.HP <= 0:
    print(f"Wild {choosen.Name} has fainted!")
    time.sleep(1)
    print(f"Your pokemon {player.current.Name} earned {choosen.Exp} Exp!")
    time.sleep(1)
    player.current.GetExp(choosen.Exp)
    return True
  print()
  return False
  

def EnemyAttack(choosen):
  global textenemy, eAttack
  print(f"{choosen.Name} Attacks!")
  time.sleep(1)
  if eAttack <=0 :
    print(f"No damage was dealt to your pokemon {player.current.Name}!")
    time.sleep(1)
  else:
    player.current.HP = player.current.HP-eAttack
    print(f"{eAttack} damage was dealt to your pokemon {player.current.Name}.")
    time.sleep(1)
  while textenemy != None:
      print(textenemy)
      time.sleep(1)
      break
  print()
  if player.current.HP <= 0:
    print(f"Your pokemon {player.current.Name} has fainted!")
    player.current.HP = 0
    time.sleep(1)
    if player.checkPokemon():
      player.changePokemon(choosen, True)
    else:
      print("All of your pokemon has fainted!")
      time.sleep(1)
      print("But your journey does not end yet.")
      time.sleep(1)
      print("I will bring you to the pokecenter")
      time.sleep(1)
      player.Heal(True)


def ViridianGym():
  print()
  print("Welcome to the Gym!")
  time.sleep(1)
  print("My name is Lionel")
  time.sleep(1)
  print("The one that will be challenging you today")
  time.sleep(1)
  print("I suppose that you are ready to fight the challenge for coming here.")
  time.sleep(2)
  print("Hopefully your pokemons don't faint during the fight.")
  time.sleep(1)
  print("My pokemons can destroy you in one second!")
  time.sleep(1)
  i = 1
  c = 0
  while i < 4:
    b = eval(f"random.randint({c}, 100)")
    if c < 33:
      a = lapras
    elif c < 66:
      a = rapidash
    elif c <= 100:
      a = vileplume
    i = i + 1
    c = c + 33
    Gym.pokemon.append(a)
    a.randomiser()
  faint = False
  a = 0
  while a < 3:
    if faint == True:
      print("You have defeated all of my pokemon.")
      time.sleep(1)
      print("That was quite a fight.")
      time.sleep(1)
      print("I congratulate you with ₽700.")
      time.sleep(1)
      player.Money = player.Money + 700
      print("Received ₽700 dollars!")
      input()
      print("This marks the end of the battle.")
      time.sleep(1)
      a = 5
      break
    else:
      print()
      print(f"Go my pokemon {Gym.pokemon[a].Name}!")
      time.sleep(1)
      i = True
      while i == True:
        if faint == True:
          if a == 2:
            break
          else:
            print(f"You have defeated my pokemon {Gym.pokemon[a].Name}.")
            time.sleep(1)
            print(f"But it is not over yet.")
            time.sleep(1)
            a = a + 1
            faint = False
            break
        else:
          print()
          print("======You======")
          player.current.BattleView()
          print("=====Enemy=====")
          Gym.pokemon[a].BattleView()
          print()
          print("Actions: ")
          time.sleep(0.05)
          print("|1| Attack")
          time.sleep(0.05)
          print("|2| Change Pokemon")
          time.sleep(0.05)
          print()
          time.sleep(0.05)
          j = str(input(f"What should {player.current.Name} do? "))
          if j == "1":
            checkType(Gym.pokemon[a])
            if Attack(Gym.pokemon[a]) == True:
              print()
              faint = True
            else:
              EnemyAttack(Gym.pokemon[a])
          elif j == "2":
            player.changePokemon(Gym.pokemon[a], False)
          else:
            print("No choice was taken.")


def Pokecenter(condition):
  global q
  while q == False:
    print()
    print(r"                  ) )        /\ ")
    print(r"                 =====      /  \ ")
    print(r"                _|___|_____/ __ \____________")
    print(r"               |::::::::::/ |  | \:::::::::::|")
    print(r"               |:::::::::/  ====  \::::::::::|")
    print(r"               |::::::::/__________\:::::::::|")
    print(r"               |_________|  ____  |__________|")
    print(r"                | ______ | / || \ | _______ |")
    print(r"                ||  |   || ====== ||   |   ||")
    print(r"                ||--+---|| |    | ||---+---||")
    print(r"                ||__|___|| |   o| ||___|___||")
    print(r"                |========| |____| |=========|")
    print(r"               (^^-^^^^^-|________|-^^^--^^^)")
    print(r"               (,, , ,, ,/________\,,,, ,, ,)")
    print(r"              ','',,,,' /__________\,,,',',;;")
    print("=================================================================")
    time.sleep(0.05)
    print()
    print("                  You are now in the Pokecenter                  ")
    time.sleep(0.05)
    print()
    print("=================================================================")
    print("Welcome to the Pokecenter!")
    time.sleep(0.5)
    print("How can I help you today?")
    time.sleep(0.5)
    print("-----------------------------------------------------------------")
    time.sleep(0.05)
    print("|1| Heal all pokemons")
    time.sleep(0.05)
    print("|2| Shop for items")
    time.sleep(0.05)
    print("|3| Go back")
    time.sleep(0.05)
    print("|O| Check Overall Stats")
    time.sleep(0.05)
    print("|I| Check Bag")
    time.sleep(0.05)
    print()
    time.sleep(0.05)
    a = str(input("What should I do? "))
    if a == "1":
      player.Heal(False)
    elif a == "2":
      Shop()
    elif a == "3":
      if condition == True:
        ViridianCity()
      else:
        break
    elif a in ("O","o"):
      player.ViewStatus()
      input()
    elif a in ("I","i"):
      player.Bag()
    elif a == "quit":
      ExitGame()
    else:
        print("No choice was taken.")

def Shop():
  global q, Healpotion, pokeBall, rareBall, epicBall
  while q == False:
    print()
    print("==========================================")
    time.sleep(0.05)
    print("     Welcome to the ViridianCity Shop     ")
    time.sleep(0.05)
    print("==========================================")
    time.sleep(0.05)
    print("|1| Heal Potion [₽150]")
    time.sleep(0.05)
    print("|2| Pokeballs [₽30/₽50/₽100]")
    time.sleep(0.05)
    print("|3| Go back")
    time.sleep(0.05)
    print("|I| Check Bag")
    time.sleep(0.05)
    print()
    a = input("What items do you want to buy? ")
    print()
    time.sleep(0.05)
    print(f"Money: ₽{player.Money}")
    time.sleep(0.05)
    if a == "1":
      if player.Money < 150:
        print("You don't have enough money!")
        time.sleep(1)
      else:
        if player.Money < 300:
          a = input("Buy Heal Potion? ")
          if a in ("Yes", "y", "yes","Y"):
            Healpotion = Healpotion + 1
            player.Money = player.Money - 150
            print("You bought 1 Heal potion!")
            time.sleep(1)
            break
          elif a in ("No", "n", "no"):
            pass
        else:
          try:
            i = True
            while i == True:
              print(f"Money: ₽{player.Money}")
              a = int(input("How many heal potion do you wish to buy? "))
              b = input(f"Buy {a} Heal Potion? ")
              if b in ("Yes", "y", "yes","Y"):
                Healpotion = Healpotion + a
                player.Money = player.Money - 150*a
                print(f"You bought {a} Heal potion!")
                time.sleep(1)
                break
              elif b in ("No", "n", "no"):
                pass
              else:
                break
          except:
            print("No number was put") 

    elif a == "2":
      if player.Money < 30:
        print("You don't have enough money!")
        time.sleep(1)
      else:
        print("|1| Pokeball      [₽30]")
        time.sleep(0.05)
        print("|2| Rare Pokeball [₽50]")
        time.sleep(0.05)
        print("|3| Epic Pokeball [₽100]")
        time.sleep(0.05)
        print()
        a = input("Which type of Pokeball do you want to buy? ")
        if a == "1":
          p = "Pokeball"
        if a == "2":
          p = "Rare Pokeball"
        if a == "3":
          p = "Epic Pokeball"
        try:
          i = True
          while i == True:
            print(f"Money: ₽{player.Money}")
            a = int(input(f"How many {p} do you wish to buy? "))
            b = input(f"Buy {a} {p}? ")
            if b in ("Yes", "y", "yes","Y"):
              if p == "Pokeball":
                pokeBall = pokeBall + a
                player.Money = player.Money - 30*a
              if p == "Rare Pokeball":
                rareBall = rareBall + a
                player.Money = player.Money - 50*a
              if p == "Epic Pokeball":
                epicBall = epicBall + a
                player.Money = player.Money - 100*a
              print(f"You bought {a} {p}!")
              time.sleep(1)
              break
            elif b in ("No", "n", "no"):
              pass
            else:
              break
        except:
          print("No number was put") 

    elif a == "3":
      break
    elif a in ("O","o"):
      player.ViewStatus()
      input()
    elif a in ("I","i"):
      player.Bag()
    elif a == "quit":
      ExitGame()
    else:
        print("No choice was taken.")

def ExitGame():
  global q
  a = input("Are you sure you want to quit the game? ")
  if a in  ("Yes", "y", "yes","Y"):
    q = True
    print("See you next time.")
  elif a in ("No", "n", "no"):
    pass

if __name__ == '__main__':
    ViridianCity()
  