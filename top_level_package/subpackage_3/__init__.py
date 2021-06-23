print(__file__)
globals()["prev"] = "prev"
import top_level_package.subpackage_3.foo

globals()["next"] = "next"
print(f"end of {__file__}")
