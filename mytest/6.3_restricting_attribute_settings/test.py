class NoNewAttrs(object):
  def __setattr__(self, name, value):
      if hasattr(self, name):
        object.__setattr__(self, name, value)
      else:
        raise AttributeError("can't add attribute %r to %s" % (name, self))

  class __metaclass__(type):
    def __setattr__(self, name, value):
      if hasattr(self, name):
        type.__setattr__(self, name, value)
      else:
        raise AttributeError("can't add attribute %r to %s" % (name, self))


class Person(NoNewAttrs):
  firstname = ''
  lastname = ''

  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def __repr__(self):
    return "Person (%r, %r)" % (self.firstname, self.lastname)

me = Person("Michere", "Simionato")
print me
me.firstname = "Michele"
print me
# Person.address = ''
me.address = ''