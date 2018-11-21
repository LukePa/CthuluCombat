class Stats:
    def __init__(self, abilities, szint, edu):
        self.Abilities = abilities
        self.SzInt = szint
        self.Edu = edu


class Abilities:
    def __init__(self, str, con, dex, pow, app):
        self.Str = str
        self.Con = con
        self.Dex = dex
        self.Pow = pow
        self.App = app

# Something that is non-sentient like a tree or a wall, or a build.
class Thing:
  def __init__(self, id):
    self.Id = id


class Position:
  def __init__(self, ew, ns):
    self.EW = ew
    self.NS = ns
    self.Alt = 0
    
    def DistanceTo(position):
        return Sqrt(Sqr(self.EW - position.ew) + Sqr(self.NS - position.ns)) 


# Something that is sentient
class Entity(Thing):
  def __init__(self, id, position, size):
    super.__init__(self, id)
    self.Position = position
    self.Size = size


class SzInt:
    def __init__(self, sz, int):
        self.Sz = sz
        self.Int = int

class Edu:
    def __init__(self, value):
        self.Value = value

# Something that could be created through character creation
class Character(Entity):
    def __init__(self, id, position, size, friendlyname, stats, szint, edu):
        super.__init__(self, id, position, size)
        self.FriendlyName = friendlyname
        self.Stats = stats
        self.SzInt = szint
        self.Edu = edu

# Something that cannot be created by a player creation
class NonPlayerCharacter(Entity):
    def __init__(self, id, position, size, friendlyname):
        super.__init__(self, id, position, size)
        self.FriendlyName = friendlyname


