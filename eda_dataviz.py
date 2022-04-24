import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv')

sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()

#TASK 1
sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Launch Site",fontsize=20)
plt.show()
#TASK 2
# Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value
sns.catplot(x="PayloadMass", y="LaunchSite", hue="Class", data=df, aspect = 5)
plt.ylabel("Launch Site",fontsize=20)
plt.xlabel("Pay load Mass (kg)",fontsize=20)
plt.show()
#TASK 3
orbit_succ = df.groupby(['Orbit']).mean()["Class"].reset_index()
sns.barplot(data=orbit_succ, x="Class", y="Orbit")
#TASK 4
sns.catplot(x="FlightNumber", y="Orbit", hue="Class", data=df, aspect = 5)
#TASK 5
sns.catplot(x="PayloadMass", y="Orbit", hue="Class", data=df, aspect = 5)
#TASK 6
year=[]
for i in df["Date"]:
     year.append(i.split("-")[0])
df["year"] = year
year_succ = df.groupby(['year']).mean()["Class"].reset_index()
plt.plot(year_succ['year'],year_succ['Class'])
plt.show()
# Features Engineering
features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
#TASK 7
features_one_hot = pd.get_dummies(features[["Orbit", "LaunchSite", "LandingPad", "Serial"]])
features.drop(columns=["Orbit", "LaunchSite", "LandingPad", "Serial"],inplace =True)
features = pd.concat([features, features_one_hot], axis=1)
features.head(2)
#TASK 8
features = features.astype("float64")