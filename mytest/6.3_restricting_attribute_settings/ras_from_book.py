def no_new_attributes(wrapped_setattr):
  def __setattr__(self, name, value):
      if hasattr(self, name):
        wrapped_setattr(self, name, value)
      else:
        raise AttributeError("can't add attribute %r to %s" % (name, self))
  return __setattr__


class NoNewAttrs(object):
  __setattr__ = no_new_attributes(object.__setattr__) 

  class __metaclass__(type):
    __setattr__ = no_new_attributes(type.__setattr__)


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
# me.address = ''