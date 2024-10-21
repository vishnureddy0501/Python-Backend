# if you are importing form another path then make sure you have empty __init__.py file in that path

# import specific methods
from Modules.LearningImports import Details
from Reusable import Reusable

print(Details())
Reusable()

# import whole module

# import Modules.LearningImports as LearningImports
# print(LearningImports.Details())
# Reusable()