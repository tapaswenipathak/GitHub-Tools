

#Fetch Data
username = raw_input ("Enter Username : ")
url = 'https://github.com/users/' + username + '/contributions.json' 
response = urllib2.urlopen (url)

data = json.load (response)

#Calculate Current Streak
def calc_curr_streak () :
	curr_streak = 0
	for i in range (len (data) - 1) :
		if data[i][1] > 0 :
			curr_streak += 1
		elif data[i][1] == 0 :
			curr_streak = 0
	
	if data[365][1] > 0 :
		curr_streak += 1
	return curr_streak

#Caculate Longest Streak
def calc_longest_streak () :
	final_max = 0
	max_till_now = 0
	for i in range (366) :
		if data[i][1] > 0 :
			max_till_now += 1
		if final_max < max_till_now :
			final_max = max_till_now
		if data[i][1] == 0 :
			max_till_now = 0
	return final_max

#Call and print the data
print "Username : " + username
print "Current Streak : " + str (calc_curr_streak ())
print "Longest Streak : " + str (calc_longest_streak ())

