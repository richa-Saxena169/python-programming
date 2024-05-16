from DatapipeLine import DatapipeLine
from TransformationJob import TransformationJob
#x = DatapipeLine("DEV",'shobhit-singh')
y = TransformationJob("DEV")

#print(y.env)
y.transformer()
#x.apiGetData()
