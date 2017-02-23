from model import Model
from firstAlgo import firstAlgo

fileDesc = open('../inputs/kittens.in')
model = Model(fileDesc)

print(firstAlgo(model))
