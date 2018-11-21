from paradigms.verification.classification import naive_bayes, random_forest, svm
from paradigms.verification.regression import logistic_regression

def verify(data):

	print("---------------------------------------------------")
	print("Spliting dataset into train and test")
	print("***************************************************")
	print("Naive Bayes:")
	count, tf_idf = naive_bayes.split_validation(data)
	print("With Count Vector:", count)
	print("with TF-IDF vector:", tf_idf)
	print("###################################################")
	print("Random Forest:")
	count, tf_idf = random_forest.split_validation(data)
	print("With Count Vector:", count)
	print("with TF-IDF vector:", tf_idf)
	print("###################################################")
	print("Support Vector Machine: ")
	count, tf_idf = svm.split_validation(data)
	print("With Count Vector:", count)
	print("with TF-IDF vector:", tf_idf)
	print("###################################################")
	print("Logistic Regression: ")
	count, tf_idf = logistic_regression.split_validation(data)
	print("With Count Vector:", count)
	print("with TF-IDF vector:", tf_idf)
	print("---------------------------------------------------")

	print("---------------------------------------------------")
	print("Cross validation")
	print("***************************************************")
	print("Naive Bayes")
	result_array, result = naive_bayes.cross_verification(data, 10)
	print("Result of cross validation:", result_array)
	print("Average of cross validation:", result)
	print("###################################################")
	print("Random Forest")
	result_array, result = random_forest.cross_verification(data, 10)
	print("Result of cross validation:", result_array)
	print("Average of cross validation:", result)
	print("###################################################")
	print("Support Vector Machine")
	result_array, result = svm.cross_verification(data, 10)
	print("Result of cross validation:", result_array)
	print("Average of cross validation:", result)
	print("###################################################")
	print("Logistic Regression")
	count_result_array, count_result, tf_idf_result_array, tf_idf_result = logistic_regression.cross_verification(data, 10)
	print("Using Count Vector")
	print("Result of cross validation:", count_result_array)
	print("Average of cross validation:", count_result)
	print("Using TF-IDF Vector")
	print("Result of cross validation:", tf_idf_result_array)
	print("Average of cross validation:", tf_idf_result)
	print("---------------------------------------------------")

