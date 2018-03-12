class Chainmap(object):
  def __init__(self, *mappings):
    self._mappings = mappings
    # print self._mappings

  def __getitem__(self, key):
    print "__getitem__", key
    for mapping in self._mappings:
      try:
        return mapping[key]
      except KeyError:
        pass
    raise KeyError(key)

  def get(self, key, default=None):
    # print "get", key
    try:
      return self[key]
    except KeyError:
      return default

  def __contains__(self, key):
    # print "contain"
    try:
      self[key]
      return True
    except KeyError:
      return False

