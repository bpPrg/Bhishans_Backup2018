import numpy as np

col0, col1, col2 = np.genfromtxt("color.txt", skip_header=0, unpack=True,
                                  dtype='str', usecols=(0, 1, 2))

print(col0)
print(col1)
print(col2)


# numpy.genfromtxt(fname, dtype='float',
#                  comments='#',
#                  delimiter=None,
#                  skip_header=0,
#                  skip_footer=0,
#                  converters=None,
#                  missing_values=None,
#                  filling_values=None,
#                  usecols=None,
#                  names=None,
#                  excludelist=None,
#                  deletechars=None,
#                   replace_space='_',
#                   autostrip=False,
#                   case_sensitive=True,
#                    defaultfmt='f%i',
#                    unpack=None,
#                    usemask=False,
#                    loose=True,
#                     invalid_raise=True,
#                     max_rows=None)
