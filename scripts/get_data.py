#
#Scrape TopNews from reuters
#Global RSS channel list is here https://www.reuters.com/tools/rss
#

import feedparser, json, os

data_file=os.path.join('data','data.json')

#Pack to the dictionary
#feed_keys - keep only needed feed keys
#entry_keys - keep only needed news keys
def CreateEntryDic(parser_data, feed_keys, entry_keys):
    result={}
    result['entries']=[]
    #Pack feed header
    for fkey in feed_keys:
        result[fkey]=parser_data[fkey]
    #Pack entries data
    for orig_entry in parser_data['entries']:
        entry={}
        for ekey in entry_keys:
            entry[ekey]=orig_entry[ekey]
        result['entries'].append(entry)
    return result

#Limit fields to simplify task    
url='http://feeds.reuters.com/reuters/topNews'
feed_keys=['status','updated','encoding']
entry_keys=['link','title','summary','published','id','feedburner_origlink']

#No RegEx needed for FeedBurner RSS
orig_data = feedparser.parse(url)
pre_data=CreateEntryDic(orig_data,feed_keys,entry_keys)

#Dump to JSON file data/data.json
j=json.dumps(pre_data, ensure_ascii=False).encode('utf8')
with open(data_file, 'w') as outfile:
    json.dump(j, outfile)
