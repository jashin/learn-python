def foo(*args, **kwargs):
  for a in args:
    print "args"
    print a

  for b in kwargs:
    print "kwargs"
    print b, kwargs[b]

foo(1, 2, 3, name="a", age=21)

foo(**{'phaseTemplates/0/broadcastTemplate/broadcastContacts/contactIds': 'asdfadsf'
                    })

# def bar(**kwargs):
#   for b in kwargs:
#     print b, kwargs[b]

# bar(name="a", age=21)