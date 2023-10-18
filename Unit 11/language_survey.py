from survey import AnonymousSurvey

question = "what language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question() # 打印显示问题
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response) # 存储答案

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results() # 显示结果
