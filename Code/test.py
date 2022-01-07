print("Hello World!")

"""
NewsFeed = fp.parse('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
entry = NewsFeed.entries[1] # should be i+1, check

print (entry.keys()) # components of a feed item
#items = len(NewsFeed.entries) # how many items in the feed

#print(entry.published)
print(entry.title)
# summary = '' # entry.summary
print(entry.link)
print(entry.summary)
print(entry.author)
print(entry.published)

pub_dt = entry.published
pub_dt = datetime.strptime(pub_dt[5:25], '%d %b %Y %H:%M:%S')
print(pub_dt)
"""

# %%
"""
NewsFeed = fp.parse('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
items = len(NewsFeed.entries) # how many items in the feed
print(items) # delete
get_latest = pd.DataFrame(columns = ['Publish_DT','Title','Summary','Author','Link'])


for i in range(items):
    print(i) #delete
    entry = NewsFeed.entries[i] # should be i+1, check
    
    pub_dt = entry.published
    # pub_dt = datetime.strptime(pub_dt[0:19], '%Y-%m-%dT%H:%M:%S')
    # pub_dt = datetime.strptime(pub_dt[5:25], '%d %b %Y %H:%M:%S')
    # if (datetime.now()-pub_dt).days > 7:
    #     continue
    # pub_dt = pub_dt.strftime("%Y-%m-%d %H:%M:00")

    title = entry.title
    summary = entry.summary
    author = ' ' #entry.author
    link = entry.link
    get_latest.loc[len(get_latest)] = [pub_dt,title,summary,author,link]
"""