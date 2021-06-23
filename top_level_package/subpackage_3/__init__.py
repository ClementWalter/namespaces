print(__file__)
globals()["prev"] = "prev"
import sys

print(sys.modules)
import top_level_package.subpackage_3.foo
print(sys.modules)

globals()["next"] = "next"
print(f"end of {__file__}")
