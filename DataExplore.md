# StackExchange Data Engineering Data Explore and Insights

This document gives a summary of the insights found after performing a data exploration.
The exploration is performed on data dump files related to one domain/subject area.

## Columns/Tags available in each xml file

Comments.xml : {'CreationDate', 'PostId', 'UserDisplayName', 'Score', 'Text', 'ContentLicense', 'UserId', 'Id'}
Users.xml : {'Reputation', 'CreationDate', 'Location', 'AccountId', 'DisplayName', 'Views', 'DownVotes', 'UpVotes', 'ProfileImageUrl', 'AboutMe', 'WebsiteUrl', 'Id', 'LastAccessDate'}
Votes.xml : {'CreationDate', 'PostId', 'BountyAmount', 'UserId', 'Id', 'VoteTypeId'}
Tags.xml : {'ExcerptPostId', 'TagName', 'Count', 'WikiPostId', 'Id'}
PostHistory.xml : {'CreationDate', 'PostId', 'PostHistoryTypeId', 'UserDisplayName', 'Text', 'Comment', 'ContentLicense', 'UserId', 'Id', 'RevisionGUID'}
PostLinks.xml : {'CreationDate', 'LinkTypeId', 'PostId', 'RelatedPostId', 'Id'}
Posts.xml : {'LastEditorUserId', 'OwnerDisplayName', 'Title', 'ParentId', 'CreationDate', 'ViewCount', 'Body', 'AnswerCount', 'Score', 'LastEditDate', 'ContentLicense', 'LastActivityDate', 'OwnerUserId', 'CommentCount', 'LastEditorDisplayName', 'CommunityOwnedDate', 'AcceptedAnswerId', 'Id', 'ClosedDate', 'Tags', 'FavoriteCount', 'PostTypeId'}
Badges.xml : {'Class', 'Name', 'UserId', 'Id', 'Date', 'TagBased'}

The tags are not consistent in each record. This means there can be NULL's for some fields. 

Used Python re.compile and regular expression, it is observed that there are non-printable and extended ascii chars.
These may need to be handled by making sure there is no data loss or corruption.

Example related 'coffee' and 'conlang' related data dump:

------ Comments.xml -------
«the more exotic stuff like espressos» I believe this strongly depends on where you live. In my country, whatever is not espresso is not considered worth enough to be called coffee. ;)
♦ Fair enough :)
“Powdered” as for Turkish coffee? Are you familiar with that process? And: Welcome!
------ Users.xml -------
ʇolɐǝz ǝɥʇ qoq
Łukasz Grabowski
рüффп
ŽaMan
İstanbul, Turkey
Москва
Маргарита Лебедева
студент001
Бостон
κατερινα Σαραντοπουλου
Люблю компьютеры и их ремонт :-)

skype rooter51
icq 278414020
中国Shanghai Shi
中国北京市Beijing Shi
Île-de-France, France
İstanbul, Türkiye
豬小妹
Киев, город Киев, Украина
İzmir, Turkey
Кировск, Ленинградская область, Россия
İstanbul, Türkiye
Катерина
象嘉道
興怡
Žygimantas RGB Tauras
Москва, Россия
刘哲诚
Żubrówka
Антон Сергунов
英范瓊
Кристиян Кацаров
노종환
Óscar Andreu
Мікалас Кaрыбутоў
日本Tōkyō-to
대한민국 Seoul
بني بوييري الجبل
موقع بني بويري الجبل24IBM
مرتضى عرقي الذبحاوي
حيدر العلي
ماجد العنزي
Анастасия Сюзана
Санкт-Петербург
کسری کوهستانی
Мирдов Крон
سامي الشهراني
كيان السعبري
İstanbul, Türkiye
コンスタンティン
نور

------ PostHistory.xml -------
İ want to design Turkish coffee, but I keep finding that the taste is widely affected by the person who brewes the coffee and the temperature at which he does it.


## Possible data corrections/ consideration

1. space vs empty fields
2. Most of the differences are observed in the USERS data set. 
3. Replace other language characters with english or printable characters
4. Removing non-printable characters if any
5. Correcting the typos like hyphens etc in the key fields so that JOINS give right output.
6. Make sure to not alter the data in ways that could result in misrepresentation of data analysis.
