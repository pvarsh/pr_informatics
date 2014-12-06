import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import csv
from datetime import datetime
import timeit

def readData_noParse():
    fileIn = "311_Service_Requests_from_2010_to_Present.csv"
    train = pd.read_csv(fileIn, usecols = ["Created Date"])
    return train
def readData_parseIn():
    fileIn = "311_Service_Requests_from_2010_to_Present.csv"
    train = pd.read_csv(fileIn, parse_dates = ['Created Date'],  usecols = ["Created Date"])
    return train
def readData_parseOut():
    fileIn = "311_Service_Requests_from_2010_to_Present.csv"
    train = pd.read_csv(fileIn, usecols = ["Created Date"])
    train['Created Date']= train['Created Date'].apply(lambda d: datetime.strptime(d, '%Y-%m-%d %H:%M:%S'))
    return train

print timeit.repeat(readData_parseIn, repeat = 3, number = 10)
print timeit.repeat(readData_noParse, repeat = 3, number = 10)
print timeit.repeat(readData_parseOut, repeat = 3, number = 10)
