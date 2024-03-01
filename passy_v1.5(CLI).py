import pyfiglet
import dill

print(pyfiglet.figlet_format("P a $ $ y V 1 . 5"))

model=dill.load(open("xgb_classifier.pkl","rb"))
vectorizer=dill.load(open("vectorizer.pkl","rb"))

print("Enter Your Password")
password=input()

password=vectorizer.transform([password])
result = model.predict(password)
probab=model.predict_proba(password)

if(result<=0):
    print("Already Cracked Somewhere Choose Strong One")   
elif(result==1):
        print("Strong Password But Watch Out")
        
