

# # SIMPLE RECOMMENDATION SYSTEM
# 


from matplotlib import pyplot as plt
from operator import itemgetter
'''
Step1: 
We create a dictionary(a nested dictionary) that contains the names of users and movies they have watched with  
their corresponding ratings:

'''
dataSet = {
    'Ronald West':{'Jurassic World Fallen Kingdom':2.5,'Blockers':4.5,'Deadpool 2':4.5,'Hold the Dark':2.5,'Roma':5.0,'The Guilty':3.5,'Mission Impossible Fallout':4.0,'Roma':1.5,'Avengers Infinity War':5.0,'Black Panther':4.5,'Overlord':4.5},
    'Kevin Kane':{'Blockers':3.5,'Thoroughbreds':2.0,'Den of Thieves':4.0,'The Guilty':2.0,'RBG':4.5,'The Tale':4.0,'Overlord':4.0,'Aquaman':4.5,'Bumblebee':2.5,'Rampage':4.5,},
    'Tabitha Amina':{'Thoroughbreds':3.0,'Black Panther':4.0,'Aquaman':3.0,'Bird Box':2.5,'Deadpool 2':5.0,'Avengers Infinity War':4.5,'The Guilty':2.0,'RBG':2.5,'Blockers':4.0,'Jurassic World Fallen Kingdom':4.5,'The Tale':4.5},
    'Bradford':{'Black Panther':4.0,'Hold the Dark':4.0,'The Guilty':3.5,'Bumblebee':4.0,'Rampage':3.5,'Den of Thieves':3.5,'Nostalgia':3.0,'Bird Box':4.0,'Thoroughbreds':3.5,'Blockers':4.5},
    'Juma Bradley':{'Jurassic World Fallen Kingdom':4.0,'Aquaman':3.5,'Bird Box':3.5,'Deadpool 2':4.5,'Avengers Infinity War':4.5,'Black Panther':4.0,'The Guilty':3.0,'RBG':3.0,'Overlord':4.0,'Hold the Dark':3.5},
    'Kane Mark':{'Jurassic World Fallen Kingdom':4.0,'The Guilty':3.0,'The Tale':3.5,'Avengers Infinity War':3.5,'Blockers':3.5,'Roma':4.5,'Nostalgia':3.5,'RBG':4.5},
    'Kean Kai':{'Blockers':2.0,'Deadpool 2':5.0,'Hold the Dark':3.0,'The Guilty':1.5,'Roma':2.5,'Overlord':3.0,'Black Panther':3.5,'Bumblebee':3.0,'RBG':2.0,'Rampage':2.5,'Mission Impossible Fallout':5.0},
    'James Shawn':{'Thoroughbreds':4.0,'Hold the Dark':5.0,'Bumblebee':3.5,'Deadpool 2':3.5,'The Guilty':3.0,'Den of Thieves':4.0,'Jurassic World Fallen Kingdom':2.5,'Blockers':4.0},
    'Sharon Heartfun':{'Black Panther':3.0,'Jurassic World Fallen Kingdom':3.0,'The Tale':5.0,'The Guilty':4.0,'Roma':4.5,'Den of Thieves':3.0,'Blockers':4.5,'Deadpool 2':5.0,'Mission Impossible Fallout':3.0},
}

'''
We have to get familiar with how nested dictionaries work so we try printing out some values set the output
Try:
    print(dataSet['Bradford']) - This returns a dictionary of a list of movies he has watched and rated
    print(dataset['Bradford']['Black Panther']) - This return the rating of the particular movie requested 
    
'''
#calculating similarity between users

def Similarity(dataSet,person1,person2):
    #collect the movies they have in common
    common_movies = []
    for item in dataSet[person1]:
        if item in dataSet[person2]:
            common_movies.append(item)
    
    no_of_common_movies = len(common_movies)
    if(no_of_common_movies==0):return 0
    
    
    sumXscore = sum([dataSet[person1][movie] for movie in common_movies])
    sumYscore = sum([dataSet[person2][movie] for movie in common_movies])
    
    sumsqX = sum([pow((dataSet[person1][movie]),2) for movie in common_movies])
    sumsqY = sum([pow((dataSet[person2][movie]),2) for movie in common_movies])
    
    pSum = sum([(dataSet[person1][movie]*dataSet[person2][movie]) for movie in common_movies])
    
    num = pSum-((sumXscore*sumYscore)/no_of_common_movies)
    
    den = sqrt((sumsqX - (pow(sumXscore,2)/no_of_common_movies)) *((sumsqY - pow(sumYscore,2)/no_of_common_movies)))

    if den==0:return 0
    return (num/den)
                                                                   
                                                                  
'''
This method plots the data between two people
'''
def plot(data,p1,p2):
    common = [movie for movie in data[p1] if movie in data[p2]]
    plt.plot([data[p1][item] for item in common],[data[p2][item] for item in common],'ro')
    plt.xlabel(p1)
    plt.ylabel(p2)
    plt.axis([0,6,0,6])
    plt.show()


'''
Recommending items to users 
'''

def getRecommendations(data,person,sim = Similarity,n = 3):
    totals = {}
    simSum = {}
    similarity = 0
    for other in data:
        if other != person:
            similarity = sim(data,person,other)
        if(similarity<=0):
            continue
        for item in data[other]:
            if item not in data[person] or data[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=data[other][item]*similarity
                
                simSum.setdefault(item,0)
                simSum[item]+=similarity
                
    rankings = [(item,totals/simSum[item]) for item,totals in totals.items()]
    
    rankings.sort(reverse = True,key = itemgetter(1))
    
    return rankings[0:n]
                

for person in dataSet:
    print(person,getRecommendations(dataSet,person))




