from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="c7f7fc0490074243888cc544008bff3e" )
all_articles = newsapi.get_everything(q='bitcoin', sources='BBC-NEWS', domains='bbc.co.uk', language='en', page=2, from_parameter='2018-02-02',to = '2018-06-09')