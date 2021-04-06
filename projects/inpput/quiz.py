import pyinputplus as pyip, random, time

no_of_questions=10
score=0

print('\tWelcome to the game of mathematics\n')
print('Rule 1: You will be given 2 choices to submit the correct answer')
print('Rule 2: You will be given 8 sec to answer one question')
input('Press any key to start the game!')

for question in range(no_of_questions):
	num1=random.randint(0,9)
	num2=random.randint(0,9)
	param='#%s: %s x %s: ' %(question+1, num1, num2)
	try:
		pyip.inputStr(param, allowRegexes=['^%s$' %(num1*num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=2)
	except pyip.TimeoutException:
		print('OOPS! Out of time')
	except pyip.RetryLimitException:
		print('OOPS! Out of tries')
	else:
		print('Correct Answer')
		score += 1

print('\nCalculating your score...')
time.sleep(2)
print(f'Your score is {score} / {no_of_questions}')


