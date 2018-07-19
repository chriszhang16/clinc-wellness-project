import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime
import sys

def getClient():
	CLIENT_ID = '22D35M'
	CLIENT_SECRET = 'c3650774498361a6eb297da3f066b581'

	server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
	server.browser_authorize()
	ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
	REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
	auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

	return auth2_client
	

# {u'datasetType': u'second', u'datasetInterval': 1, 
# u'dataset': [{u'value': 67, u'time': u'00:00:02'}, {u'value': 68, u'time': u'00:00:07'}, {u'value': 71, u'time': u'00:00:12'}...]}
def getMax(dataset):
	HR_max = 0
	HR_time = 0

	for timeval in dataset:
		if timeval['value'] > HR_max:
			HR_time = timeval['time']
			HR_max = timeval['value']
	print "max HR:", HR_max
	print "at time:", HR_time

def getMin(dataset):
	HR_min = sys.maxint
	HR_time = 0

	for timeval in dataset:
		if timeval['value'] < HR_min:
			HR_time = timeval['time']
			HR_min = timeval['value']
	print "min HR:", HR_min
	print "at time:", HR_time

def getSleepData(day):
	# yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
	fit_statsSleep = getClient().sleep(date=day)
	sleeptime = []
	sleepvals = []

	# for timeval in fit_statsSleep['sleep'][0]['minuteData']:
		

	# print fit_statsSl



def main():
	yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
	# yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
	today = str(datetime.datetime.now().strftime("%Y-%m-%d"))

	fit_statsHR = getClient().intraday_time_series('activities/heart', base_date=today, detail_level='1sec')

	today_dict = fit_statsHR['activities-heart-intraday']

	# getMax(today_dict['dataset'])
	# getMin(today_dict['dataset'])



	getSleepData(yesterday)



	# Average, min, max, average over different periods of time





if __name__ == "__main__":
	main()
