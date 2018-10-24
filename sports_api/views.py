from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status as status_http
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from search_task import settings

import tweepy
from datetime import datetime
from .models import Tweet
from .serializers import TweetSerializer
from django.core import serializers

# Create your views here.

class SearchResultView(APIView):
    template_name = 'index.html'

    def post(self, request):
        data = Tweet.objects.filter(text__icontains=request.POST.get('text'))
        # data = serializers.serialize('json', latest_tweets, ensure_ascii=False)
        return render(request,self.template_name,data)
    
    def get(self,request):
        api = twitter_setup()
        latest_tweets = []
        try:
            last_tweet_id = Tweet.objects.order_by("-id_str")[0].id_str
            tweets = tweepy.Cursor(api.user_timeline,
                                    screen_name='@Yallakoranow',since_id = last_tweet_id
                                    ).items()
        except Exception:
            tweets = tweepy.Cursor(api.user_timeline,
                                    screen_name='@Yallakoranow',since = datetime.today().strftime('%Y-%m-%d')
                                    ).items(1)
        for status in tweets:
            tweet = {'text': status._json['text'],
                     'id_str': status._json['id_str'],
                     'created_at': status._json['created_at'],'links':[]}
            if 'media' in status._json['entities'].keys():
                for curr_media in status._json['entities']['media'] :
                    tweet['links'].append({'link_url':curr_media['media_url_https']})

            latest_tweets.append(tweet)

        if latest_tweets:
            Tweet.objects.mongo_insert_many(latest_tweets)
    
        return render(request,self.template_name)            

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
