class SomeName(object):
  pass


anInstance = SomeName()
another = SomeName()

anInstance.someNumber = 23 * 45
# print anInstance.someNumber


class Behave(object):
    def __init__(self, name):
      self.name = name

    def once(self):
      print "Hello,", self.name

    def rename(self, newName):
      self.name = newName

    def repeat(self, N):
      for i in range(N):
        self.once()

beehive = Behave("Queen Bee")
# beehive.repeat(3)
# beehive.rename("Stinger")
# beehive.once()
# print beehive.name
# beehive.name = "steve"
# beehive.repeat(2)


class Repeater(object):
  def repeat(self, N):
    print N * "*-*"

# aMix = beehive, Behave("John"), Repeater(), Behave("world")
# for whatever in aMix: 
#   whatever.repeat(3)


class Subclass(Behave):
  def once(self): 
    print "(%s)" % self.name

subInstance = Subclass("Queen Bee")
# subInstance.repeat(3)


class OneMore(Behave):
  def repeat(self, N):
    super.repeat(self, N + 1)

zealant = OneMore("Worker Bee")
zealant.repeat(3)