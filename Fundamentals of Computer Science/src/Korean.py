from Human import Human

class Korean(Human):
   def lang(self, item = 'Korean'):
      self.language = 'Korean'
      return self.language
   
   def alcohol(self, drink = 'soju'):
      self.drink = 'Soju'
      return self.drink

   def haircolor(self, color = 'Black or Brown'):
      self.haircolor = 'Balck or Brown hair'
      return self.haircolor

   def food(self, food = 'rice'):
      self.food = 'Rice'
      return self.food
   
   def alphabet(self, alphabet = 'Hangul'):
      self.alphabet = 'Hangul'
      return self.alphabet 

if __name__ == "__main__":
   print("< About a_human >")
   a_human = Korean('Korean')
   print(a_human.species)
   a_human.species = 'Asian'
   print(a_human.species)
   print(a_human.lang())
   print(a_human.alcohol())
   print(a_human.drink)
   print(a_human.haircolor())
   print(a_human.food())
   print(a_human.alphabet())
