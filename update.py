from arraydata import getCrimes
import pandas as pd

# def dara(city):
#   data = getCrimes()
#   # print(data)
#   dataframe = pd.DataFrame(data,columns=["Incident","Time","Area"])
#   dataframe = dataframe.dropna()
#   city = city.upper()
# #   print(city)
# #   print(dataframe)
#   dataframe = dataframe[dataframe['Area'].str.contains(city)]
# #   print(dataframe)
#   return dataframe


# data = dara("Kitchener")
# # print(data)
# # print(data["Area"])
# print(data["Area"].iloc[0])

dataframe = pd.DataFrame(getCrimes() ,columns=["Incident","Time","Area"])
dataframe.to_csv('data.csv', index=False)