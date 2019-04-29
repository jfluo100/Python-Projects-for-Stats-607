import pandas as pd

def get_US_crime():
	"""This function creates a list of lists with the data in crime"""
	crimeDF = pd.read_csv('crime.csv') # Creates a Pandas Dataframe
	crimeList = crimeDF.values.tolist() # Convert it to list
	return crimeList

def get_US_crime_rates():
    """This function creates a list of lists with the data in crimeRates"""
    crimeRatesDF = pd.read_csv('crimeRates.csv') # Creates a Pandas Dataframe
    crimeRatesList = crimeRatesDF.values.tolist() # Convert it to list
    return crimeRatesList
