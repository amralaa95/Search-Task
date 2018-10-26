# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from search_task import settings
import tweepy
from datetime import datetime
from .models import Tweet

class SearchResultView(View):
    template_name = 'index.html'
    
    def get(self,request):
        """
        Function to get first new today tweets from yallakora using Twitter API and
            add new tweets in mongo db in then retrive result form search text from mongo db.
        """
        api = twitter_setup()
        latest_tweets = []
        startDate = datetime( datetime.now().year,datetime.now().month,datetime.now().day,0,0,0)
        try:# there is previous tweets stored in db
            last_tweet_id = Tweet.objects.order_by("-id_str")[0].id_str
            tweets = tweepy.Cursor(api.user_timeline,
                                    screen_name='@Yallakoranow',since_id = last_tweet_id
                                    ).items()
        except:# add tweets to empty db
            tweets = tweepy.Cursor(api.user_timeline,
                                    screen_name='@Yallakoranow').items()

        for status in tweets: # add only today tweets
            if status.created_at < startDate:
                break
            # curr_date = datetime.combine(status.created_at,datetime.min.time())
            tweet = {'text': status.text[0:status.text.index('https')],
                     'id_str': status.id_str,
                     'created_at': status.created_at,
                     'links':[]}
            if 'media' in status.entities.keys():
                for curr_media in status.entities['media'] :
                    tweet['links'].append({'link_url':curr_media['media_url_https']})

            latest_tweets.append(tweet)

        if latest_tweets:
            Tweet.objects.mongo_insert_many(latest_tweets)

        try: # retrive search result from text
            res = Tweet.objects.filter(text__icontains=request.GET.get('text'))
        except:
            res = {}
        return render(request,self.template_name,{'res':res})

def twitter_setup():
    """
    Function to connect to Twitter API.
    """
    
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,
                               settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN,
                          settings.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api
