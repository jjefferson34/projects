import billionaires
list_of_billionaire = billionaires.get_billionaires()
import matplotlib.pyplot as plt


for dictionary in list_of_billionaire:
    info = dictionary["wealth"]
    print(info["how"])

for dictionary in list_of_billionaire:
    info = dictionary["demographics"]
    print(info["gender"])
    print(info["age"])

for dictionary in list_of_billionaire:
    info = dictionary["location"]
    print(info["region"])


# The slices will be ordered and plotted counter-clockwise.
labels = 'was founder', 'emerging markets', 'inherited', 'not inherited'
sizes = [24,32,20,24]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0, 0, 0)  # explode a slice if required

plt.title('How each Person Became a Billionaire')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%.1f%%', shadow=True)

#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()

# The slices will be ordered and plotted counter-clockwise.
labels = 'male' , 'female'
sizes = [85,15]
colors = ['lightskyblue', 'lightcoral']
explode = (0, 0)  # explode a slice if required

plt.title('Male vs. Female Billionaires')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%.1f%%', shadow=True)

#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()


# The slices will be ordered and plotted counter-clockwise.
labels = 'greater than 50 yrs' , 'less than 49 yrs'
sizes = [80,20]
colors = ['lightskyblue', 'lightcoral']
explode = (0, 0)  # explode a slice if required

plt.title('Billionaire Ages')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True)

#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()


# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()


# The slices will be ordered and plotted counter-clockwise.
labels = 'North Amercia', 'Europe','East Asia', 'Latin America','North Africa','Sub-Saharan Africa','Middle East','South Asia'
sizes = [42,26,16,4,4,2,2,2]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0, 0, 0, 0, 0, 0, 0)  # explode a slice if required

plt.title('Billionaire Origins')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True)

#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()
