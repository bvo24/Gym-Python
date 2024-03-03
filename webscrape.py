from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.strengthlog.com/exercise-directory/#Muscle_Directory_Complete_List_of_All_Exercises"
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
chest = []

#12/25/2023
#chestExercises = doc.find_all('ol')[0]

bodyPart = doc.find_all('h3')
exercises = doc.find_all('ol')
#indExercise = doc.find_all('ol').find_all('li')
workout = []




for z in range(0, (len(bodyPart) - 11)):
    #print("\nBODY: " + bodyPart[z].text.upper())
    body = bodyPart[z].text.upper()
    work = exercises[z].find_all('li')
    #workout.append(body)
    for y in range(0, len(work)):
        #print(work[y].text)
        exercise = work[y].text
        workout.append([body, exercise])




n = len(bodyPart)-1
df = pd.DataFrame(workout, columns=['Body part', 'Exercise'])
df.to_csv('workoutlist3.csv')




#maybe a create a double foor loop???? not sure
#or i create a loop for the headers then append them to a list
#which then serves as the column


#in this case I should do a loop for each ol instead and have the same logic here
#ok this is good i am able to separate each work out

#12/25/2023
#what we did here was make a  double loop instead
#for li in chestExercises.find_all('li'):
    #print(li.text)
    #chest.append(li.text)

#print(chest)

#in theory everything is set up once i create all this data it might be fucked up because it will be a row of chest exercises so instead we should transpose this.

#the problem that comes next is trying to create a randomizer??? because we would iterate through columns instead now, which make take up more time maybe we reverse transpose the data then go by row ????
