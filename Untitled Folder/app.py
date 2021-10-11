from flask import Flask
import json
import numpy as np 
import pandas as pd 
import pymongo
from collections import Counter
import operator
app=Flask(__name__)
from youtube import *
from twitter import *
from reddit import *
from tumblr import *

client=pymongo.MongoClient("mongodb+srv://KokilaReddy:KokilaReddy@cluster0.5nrpf.mongodb.net/Social_media_data?retryWrites=true&w=majority")
db=client['Social_media_data']
class Analytics:
	@app.route('/')
	@app.route('/analytics/<brand>/<duration>')
	def analytics(brand,duration):

		#youtube
		duration=int(duration)
		youtube=YouTube(brand,duration)
		youtube_Hashtags=youtube.getHashTags()
		youtube_InfluencingChannels=youtube.InfluencingChannels()
		youtube_moredisccussions=youtube.ChannelsWithMoreDiscussions()
		youtube_categories=youtube.categoriesOfMentions()



		#twitter
		twitter=Twitter(brand,duration)
		twitter_hashtags=twitter.HashTags()
		twitter_Influencinguser=twitter.findInfluentialUser()



		#Reddit
		reddit=Reddit(brand,duration)
		reddit_hottopicbasedoncomment=reddit.hotTopicBaseOnCc();
		reddit_hottopicbasedonscore=reddit.hotTopicBasedOnScore();



		#tumblr
		tumbulr=Tumblr(brand,duration)
		tumbulr_hashtags=tumbulr.getHashTags();

		Data={
		    "youtube":
			{"hashtags":youtube_Hashtags,"InfluencingChannels":youtube_InfluencingChannels,"ChannelWithMoreDiscussions":youtube_moredisccussions,
			    "categoriesOfMentions":youtube_categories
			    
			},
		    "Twitter":
		    {
			    
			    "hashtags":twitter_hashtags,"InfluencingUser":twitter_Influencinguser

		    },
		    "Reddit":{
			"hottopicbasedoncommentscount":reddit_hottopicbasedoncomment,
			"hottopicbasedonscore":reddit_hottopicbasedonscore,
			


		    },
		    "tumbulr":{
			    "hashtags":tumbulr_hashtags
		    }
		}
		json_data = json.dumps(Data)
		return json_data
	def Text_Analytics(brand,duration):
		pass
	



if(__name__=='__main__'):
    app.run(host='0.0.0.0',debug=True)





