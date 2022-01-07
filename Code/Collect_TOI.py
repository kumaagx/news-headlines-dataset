import pandas as pd
import feedparser as fp
from datetime import datetime


def get_content(feed_name, feed_link):
  NewsFeed = fp.parse(feed_link)
  items = len(NewsFeed.entries)
  get_latest = pd.DataFrame(
    columns=['Feed', 'Publish_DT', 'Title', 'Summary', 'Author', 'Link'])

  for i in range(items):
    entry = NewsFeed.entries[i]

    pub_dt = entry.published
    # pub_dt = datetime.strptime(pub_dt[0:19], '%Y-%m-%dT%H:%M:%S')
    pub_dt = datetime.strptime(pub_dt[5:25], '%d %b %Y %H:%M:%S')
    if (datetime.now() - pub_dt).days > 14:
      continue
    pub_dt = pub_dt.strftime("%Y-%m-%d %H:%M:00")
    title = entry.title
    summary = ' '  # entry.summary
    author = ' '  # entry.author
    link = entry.link

    get_latest.loc[len(get_latest)] = [feed_name, pub_dt, title, summary, author, link]

  return get_latest


table_sources = pd.read_csv("Input/Sources.csv")
latest_content = pd.DataFrame()

print("==== Starting data fetch for TOI ====")

for index, row in table_sources.iterrows():

  if row['Source'] == 'TOI':
    feed_name = row['Feed']
    feed_link = row['Link']
  else:
    continue

  print("Fetching data for TOI: " + feed_name)

  try:
    latest_content = latest_content.append(get_content(feed_name, feed_link), sort=False, ignore_index=True)
  except:
    print(feed_name, " has error, skipped")
    continue

table_content = pd.read_csv("Output/TOI.csv")
# Backup data file
# table_content.to_csv("../Data/Backup/Table_Content_"+datetime.now().strftime('%Y%m%d_%H%M')+".csv", index=False)
# Append to previous data
table_content = table_content.append(latest_content, sort=False, ignore_index=True)
# Remove duplicates (by link)
table_content.drop_duplicates(subset=['Link'], keep='last', inplace=True)
# Sort all data
table_content.sort_values("Publish_DT", inplace=True)
# Write to CSV
table_content.to_csv("Output/TOI.csv", index=False)

print("==== Ending data fetch for TOI ====")
