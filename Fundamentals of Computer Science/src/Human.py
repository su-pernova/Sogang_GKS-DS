class Human:
   species = 'x'

   def __init__(self, spec='x'):
      self.species = spec

   def lang(self, item='native language'):
      self.language = 'native language'
      return self.language

if __name__ == "__main__":
   a_human = Human('Korean')
   print(a_human.species)
   a_human.species = 'Global citizen'
   print(a_human.species)
