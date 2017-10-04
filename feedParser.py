import feedparser

print("Enter you choice: ")
print("1. BBC")
print("2. Times Of india")
choice = int(input())

if choice == 1:
    parseData = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml")
    offlineData = []

    for i in range(20):
        offlineData.append(parseData.entries[i])

    for data in offlineData:
        print('\n')
        print('Title: ' + data['title'])
        print('Dated: ' + data['published'])
        print('Summary ' + data['summary'])
        print('Link: ' + data['link'])
elif choice == 2:
    parseData = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
    offlineData = []

    for i in range(20):
        offlineData.append(parseData.entries[i])

    for data in offlineData:
        print('\n')
        print('Title: ' + data['title'])
        print('Dated: ' + data['published'])
        print('Summary ' + data['summary'])
        print('Link: ' + data['link'])
else:
    print('Wrong choice')
