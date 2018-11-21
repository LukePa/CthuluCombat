import json
from Domain import *

#class EntityRepository():
#  def __init__():
#  
#  def Populate(entityid):
#      # Access the datastore...#
#
#    return Entity(entityid, Position(0, 0), 1)

class Repository():
  def __init__(self):
    self.__data = {
            "entities" : [
               {
                  "type" : "character",
                  "id" : "1",
                  "detail" :
                    {
                        "id" : "1",
                        "friendlyname" : "Shifty Steve",
                        "stats" :
                            {
                                "str" : "10",
                                "dex" : "10",
                                "con" : "10",
                                "pow" : "10",
                                "app" : "10"
                            },
                        "sz" : "10",
                        "int" : "10",
                        "edu" : "10"
                    }
               },
               {
                  "type" : "character",
                  "id" : "2",
                  "detail" :
                    {
                    }
               }
               ]
            }



  def populate(self, entityid):
      entities = self.__data.get("entities")
      entity = [x for x in entities if x['id'] == entityid)]
    
      print(entity)

      print(entity.index("type"))

      #if entity['id']['id'] == entityid:
      if entity["type"][0].lower() == "character":
          return CreateCharacterFromDictionary(entity)
      elif entityAsDictionary["type"].lower() == "nonplayercharacter":
          return CreateNonPlayerCharacterFromDictionary(entity)
      else:
          return CreateEntityFromDictionary(entity)

      entityFound = False;

      return

  def CreateCharacterFromDictionary(entity):
      print("Character")
      return Character()
  def CreateNonPlayerCharacterFromDictionary(entity):
      print("NonPlayerCharacter")
      return NonPlayerCharacter()
  def CreateEntityFromDictionary(entity):
      print("Entity")
      return Entity()


