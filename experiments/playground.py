from ecg import schiller_parser as data
from visualise import drawecg

dataset = data.open_diverse_1D_dataset()
print (len(dataset))

ecgleads = dataset[34:51]
drawecg.draw12leads(ecgleads, start=10, end=3000)
