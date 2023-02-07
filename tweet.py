import requests
import os
import json
from matplotlib import pyplot as plt
import numpy as np
# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token ="AAAAAAAAAAAAAAAAAAAAAAM3WgEAAAAAQMAz17pZ1yYoDAidmxXPtOmaaWo%3D1liP0Ppcjd73leetCw8tC5PlUxCCia2n0QfVicBcWlVhJjeVSy"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():                     
    json_response = connect_to_endpoint(search_url, query_params)
    list1=['sadden','unhappy','mournful','melancholy','down','doleful','downcast','gloom','glum','forlorn','heartsick','pensive','heavy','blue','gloomy','sorrowful','dejected','desolate','downhearted','depressed','tragic','disconsolate','dreary',
    'lonesome','tragedy','sorry','lugubrious','lonely','sadness','asily','const','Builder','wistful','sadly','lachrymose','heavyhearted','depress','plaintive','howl','dusky','dismal','somber','moody','tearjerker','inconsolable','crestfallen','regret','joyless',
    'sorrow','plangent','down','depression','woebegone','woeful','tearful','miss','elegy','heartbroken','yowl','low-spirited','dolorous','melancholic','comfort','atrabilious','soberly','solace','longface','grieve','mope','sombre','sepulchral',
    'blues','sadassed','dark','hangdog','despondent','embitter','low','lighten','discomfortable','mesto','overshadow','homesick','black','dumpish','groanful','mourn','light','console','fado','upset','wan','griefstricken','sobstory',
    'grim','droop','deject','cheerless','Next', 'a' 'Query'] 
    list2=['Laughter','happiness','love','happy','joy','tools','been','laughter','happiness','love','laughed','laugh','laughing','excellent','laughs','joy','successful','win','rainbow','smile','won','pleasure','smiled','rainbows','winning',
    'celebration','enjoyed','healthy','music','celebrating','congratulations','easily','const','Builder','toruct','query','weekend','celebrate','comedy','jokes','rich','victory','christmas','free','friendship','fun','holidays','loved','loves','loving','beach','hahaha','kissing','sunshine',
    'beautiful','delicious','friends','funny','outstanding','paradise','sweetest','vacation','butterflies','freedom','rule','search','Tweets','using','flower','great','sunlight','sweetheart','sweetness','award','chocolate','hahahaha','heaven','peace','splendid','success','enjoying','kissed','attraction','celebrated','hero','hugs','positive','sun','birthday','blessed','fantastic','winner','delight','beauty','butterfly','entertainment','funniest','honesty','sky','smiles','succeed','v2','search','streaming','endpoints','wonderful','glorious','kisses','promotion','family','gift','humour','romantic','cupcakes','festival','hahahahaha','honour','relax','weekends']
    print(json.dumps(json_response, indent=4, sort_keys=True))
    #print(json_response['data'][0]["text"])
    tweet_list=json_response['data']
    listfinal=[]
    for x in range(len(tweet_list)):
     string=tweet_list[x]['text']
     textoftweet=string.split()
     listOfIntersection1 = []
     for i in textoftweet:
      for j in list1:
         if (i==j):
             listOfIntersection1.append(i)

     positive=0    
     for element in listOfIntersection1:
      positive += 1
     listOfIntersection2 = []
     for k in textoftweet:
          for m in list2:
            if (k==m):
             listOfIntersection2.append(i)

     negetive=0    
     for element2 in listOfIntersection2:
      negetive -= 1 
     #neutral=0
     #if negetive==0 and positive==0:
        # neutral += 1
     emotion=(positive+negetive)*10
     listfinal.append(emotion)

    for t in range(len(listfinal)):
        print(listfinal[t]),

    plot=[]    

    for f in range(len(tweet_list)):
         plot.append(f)
          
    plt.plot(listfinal, plot) 
    plt.xlabel('sentiments')
    plt.ylabel('tweets')
    plt.title('analysis graph')
    plt.show()    

 
    
 #print(textoftweet)
  #return positive

 #if emotion>10
#list1=['black','depressed','low','sad','unhappy','have']
#list2=['Laughter','happiness','love','happy','joy','tools','been']
#a=main()
 #print(a)
#list3 = set(a)&set(list1)

#ist4 = sorted(list3, key = lambda k : list1.index(k))
#list5 = set(a)&set(list2)
#list6 = sorted(list5, key = lambda k : list2.index(k))
#for x in range(len(list4)):
    #print(list4[x]),
 
#for x in range(len(list6)):
    #print(list6[x]),

#def get_number_of_elements(list):
    #count = 0
    #for element in list:
        #count += 1
    #return count

#positive=get_number_of_elements(list4)
#print(positive*10) 

#negetive=get_number_of_elements(list6)
#print(negetive*10)

# Creating dataset
#emotions = ['POSITIVE', 'NEGETIVE', 'NEUTRAL']
 
#data = [positive, negetive, 35]
 
# Creating plot
#fig = plt.figure(figsize =(10, 7))
#plt.pie(data, labels = emotions)
 
# show plot
#plt.show()



if __name__ == "__main__":
    main()