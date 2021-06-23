#%% Check current symbol tables
dir()
globals()
locals()

import sys
from pprint import pprint
pprint(sys.path)
pprint(globals())

#%% Import module
import from_imports
dir()
dir(from_imports)
from_imports.__file__
from_imports.__package__

#%% Import and add to namespace
from from_imports import a
dir()
from from_imports import *
dir()

#%% Import and rename
import from_imports as from_
dir()

#%% Import package
import top_level_package
dir()
dir(top_level_package)
top_level_package.__file__
top_level_package.__path__
top_level_package.__package__

#%% Import module in package
import top_level_package.baz
dir()
dir(top_level_package)

from top_level_package import baz
dir()

#%% Import module in folder
import top_level_package.subfolder as subfolder
dir()
dir(subfolder)
subfolder.foo
# AttributeError: module 'top_level_package.subfolder' has no attribute 'foo'
from top_level_package.subfolder import foo
import top_level_package.subfolder.foo as foo

#%% Import module in package with empty init
import top_level_package.subpackage as subpackage
dir()
dir(subpackage)
subpackage.foo
# AttributeError: module 'top_level_package.subpackage' has no attribute 'foo'
from top_level_package.subpackage import foo
import top_level_package.subpackage.foo as foo

#%% Import module in package with init https://docs.python.org/3/reference/import.html#submodules
import top_level_package.subpackage_2 as subpackage_2
dir()
dir(subpackage_2)
subpackage_2.foo
from top_level_package.subpackage_2 import foo
import top_level_package.subpackage_2.foo as foo

#%% Import module in package with init and __all__
import top_level_package.subpackage_3 as subpackage_3
dir()
dir(subpackage_3)
subpackage_3.foo
subpackage_3.fun
from top_level_package.subpackage_3 import *
dir()

#%% Namespace packages
import sys
sys.path.extend(["cal-ds", "cal-db"])
import cal
cal.__path__

#%% Export


class A:

    a = 1


class B(A):
    pass


A.__dict__
B.__dict__
hasattr(B, 'a')
