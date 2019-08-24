dict={"country":["Brazil","Russia","India","china","South Africa"],
      "capital":["Brasilia","Mascow","New Dehli","Beijing","Pretoria"],
      "area":[8.5,12.9,17.9,3.5,9.5],
      "population":[200.4,123.6,675.5,879.9,76.9]}
import pandas as pd
brics=pd.DataFrame(dict)
print(brics)





import pandas as pd
ppls=pd.read_csv('ppl.csv')
print(ppls)


import pandas as pd
ppl=pd.read_csv('ppl.csv')
print(ppl)


import random
def lottery():
    for i in range(6):
        yield random.randint(1,40)
        yield random.randint(1,15)
    for random_number in lottery():
        print("And the next number is...%d!"%(random_number))