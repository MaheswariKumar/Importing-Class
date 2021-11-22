#Storing a function in module
#import a entire module
#module name.function name()
import mine
mine.mine("maheswari", "kumar", location="salem", country="india", age=23)

#import a specific function
#from module import function name
from mine import mine
mine("maheswari", "kumar", location="salem", country="india", age=23)

#Use as for giving function name an alias
#from module import function name as fn
from mine import mine as m
m("maheswari", "kumar", location="salem", country="india", age=23)

#Use as for giving module an alias
#import module name as mn
import mine as m
m.mine("maheswari", "kumar", location="salem", country="india", age=23)

#importing all functions in module
#from module name import *
from mine import *