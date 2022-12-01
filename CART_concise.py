import pandas as pd
import datetime
import holidays
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import DriverRecognition

model=0
class CART:
    def __init__(self):
        df_encoded=pd.read_csv('Key_fob_encoded.csv')
        df_encoded=pd.DataFrame(data=df_encoded.iloc[:,1:8].values,columns=["Distance","Hour","Minute","Day","Day_type","SpclOccasions","Target"])
        # plt.figure(figsize=(11,4))
        # sns.heatmap(df_encoded[["Distance","Date","Time","Day","Day_type","SpclOccasions","Target"]].corr(),annot=True)
        # plt.show()
        x=df_encoded.iloc[:,0:6]
        y=df_encoded.iloc[:,6]

        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
        global model
        model=tree.DecisionTreeClassifier(criterion="gini")
        model.fit(x_train.values,y_train.values)
        model.score(x_test,y_test)*100

    def CART(self,distance):
        le=LabelEncoder()
        print("Distance =",distance)
        date=datetime.date.today()
        day=datetime.datetime.strftime(date,"%A")
        date=datetime.datetime.strftime(date,"%Y-%m-%d")
        uk_holidays = holidays.UnitedKingdom()
        SpclOccasions=uk_holidays.get(date)
        if SpclOccasions==None:
            SpclOccasions="NULL"

        if day=="Sunday" or day=="Saturday" or SpclOccasions!="Null":
            dayType=0
            # Holiday
        else:
            dayType=1
            # Working day

        now=datetime.datetime.now()
        time=now.strftime("%H:%M:00")
        hour,minute,_=map(int,str(time).split(":"))
        hour=23
        minute=15
        
        print(distance,hour,minute,day,dayType,SpclOccasions)
        dayT=le.fit_transform([day])
        SpclOccasionsT=le.fit_transform([SpclOccasions])
        allIn=[distance,hour,minute,dayT[0],dayType,SpclOccasionsT[0]]
        print(allIn)
        target=model.predict([allIn])
        if target==0:
            print("Prediction: UNLOCK")
        else:
            print("Prediction: LOCK")
        return target
        