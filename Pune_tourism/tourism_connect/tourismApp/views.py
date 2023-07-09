from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix
import joblib
import pandas as pd
import numpy as np

# Create your views here.
def home(request):
    return render(request, "home.html")

def religious(request):
    return render(request,'religious.html')

def hillStation(request):
    return render(request,'hillStation.html')

def historical(request):
    return render(request,'historical.html')

def others(request):
    return render(request,'others.html')

def prediction(request):
    input1 = request.POST.get("option1")
    input2 = request.POST.get("option2")
    print(input1)
    print(input2)

    dataset = pd.read_csv(r"C:\Users\palla\Dropbox\My PC (LAPTOP-MEMQ4MVO)\Documents\Pune_tourism\tourism_connect\tourism_data.csv")


    #Splitting data into X and y
    X = dataset.drop('Place',axis=1).dropna()
    

    Y = dataset['Place']

    #Splitting dataset into training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
    

    #Building classifier
    classifier = RandomForestClassifier()
    print(classifier)
    classifier.fit(X_train.values, Y_train)

    #Prediction
    prediction = classifier.predict(X_test)
    print("The testing dataset output:")
    print(prediction)

    print("The accuracy of the prediction:")
    print(classifier.score(X_test, Y_test))

    ans = classifier.predict([[input1,input2]])
    return render(request,"home.html",{'error': True,'message':ans})