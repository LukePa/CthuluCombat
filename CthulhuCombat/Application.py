from Domain import *
from Infrastructure import *

repo = Repository()

thing = repo.populate("1")

print(thing)
print(thing.Value)