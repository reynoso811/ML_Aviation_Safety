


#Create a function within many Machine Learning Models
def models(X_train,Y_train, X_test, y_test):

  #Using Logistic Regression Algorithm to the Training Set
  
  log = LogisticRegression(random_state = 0, max_iter=50000)
  log.fit(X_train,Y_train, X_test, y_test)

  #Using KNeighborsClassifier Method of neighbors class to use Nearest Neighbor algorithm
  
  knn = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
  knn.fit(X_train,Y_train, X_test, y_test)

  #Using SVC method of svm class to use Support Vector Machine Algorithm
  
  svc_lin = SVC(kernel = 'linear', random_state = 0)
  svc_lin.fit(X_train,Y_train, X_test, y_test)

  #Using SVC method of svm class to use Kernel SVM Algorithm
  
  svc_rbf = SVC(kernel = 'rbf', random_state = 0)
  svc_rbf.fit(X_train,Y_train, X_test, y_test)

  #Using GaussianNB method of naïve_bayes class to use Naïve Bayes Algorithm
  
  gauss = GaussianNB()
  gauss.fit(X_train,Y_train, X_test, y_test)

  #Using DecisionTreeClassifier of tree class to use Decision Tree Algorithm
  
  tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
  tree.fit(X_train,Y_train, X_test, y_test)

  #Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
  
  forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
  forest.fit(X_train,Y_train, X_test, y_test)

  #print model accuracy on the training data.
  print('[0]Logistic Regression Training Accuracy:', log.score(X_train,Y_train, X_test, y_test))
  print('[1]K Nearest Neighbor Training Accuracy:', knn.score(X_train,Y_train, X_test, y_test))
  print('[2]Support Vector Machine (Linear Classifier) Training Accuracy:', svc_lin.score(X_train,Y_train, X_test, y_test))
  print('[3]Support Vector Machine (RBF Classifier) Training Accuracy:', svc_rbf.score(X_train,Y_train, X_test, y_test))
  print('[4]Gaussian Naive Bayes Training Accuracy:', gauss.score(X_train,Y_train, X_test, y_test))
  print('[5]Decision Tree Classifier Training Accuracy:', tree.score(X_train,Y_train, X_test, y_test))
  print('[6]Random Forest Classifier Training Accuracy:', forest.score(X_train,Y_train, X_test, y_test))

  return 