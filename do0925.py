import sys
sys.path.append('D:/Applications/Python3/Data')
from Data import Postgresql
sys.path.append('D:/Applications/Python3/dataFileHelper')
sys.path.append('D:/Applications/Python3/GeneralFunction')
import time
from GeneralFunction import ReHelper

def GetTimestr():
    timeCur = time.localtime(time.time())
    timeStr = time.strftime('%Y-%m-%d %H:%M:%S',timeCur)
    return timeStr

def DFInsertNews():
    pass

def reviseC(data):
    if data < 10:
        return '000'+str(data)
    elif data < 100:
        return '00'+str(data)
    elif data < 1000:
        return '0'+str(data)
    else:
        return str(data)

postgresql = Postgresql()
# zz = xx()
strSQL = 'select id,title,content,"publishDate",category,"visitCnt" from base_news order by id'
listRecords = postgresql.Query(strSQL)
#listRecords = listRecords[:1]
#listRecords = postgresql.Query('base_news','id','title','content','"publishDate"','category''"visitCnt"')

# Record = listRecords[0]

for Record in listRecords:
    id = Record[0]
    title = Record[1]
    content = Record[2]
    publishDate = Record[3]
    category = Record[4]
    visitCnt = Record[5]
    print ("the Record tile is %s" % title)
    listSeq = postgresql.Query("select path from wagtailcore_page where path like '000100010001%'")
    countSeq = len(listSeq)
    #1.insert record to wagtailcore_page
    slug = ReHelper.subString(title,"[^\w\u3007\u4E00-\u9FCB\uE815-\uE864]|[/]","")
    print("the slug is %s" % slug)
    listFields = ['id','path','depth','numchild','title','slug',\
                  'live','has_unpublished_changes','url_path','seo_title','show_in_menus',\
                  'search_description','go_live_at','expire_at','expired','content_type_id',\
                  'owner_id','locked','latest_revision_created_at','first_published_at','live_revision_id',\
                  'last_published_at','draft_title']
    listValues = [id+10,'000100010001'+reviseC(countSeq),4,0,title,slug,\
                  True,False,'/home/news-list/%s/' % (slug),'\'\'',False, \
                  '\'\'','NULL','NULL',False,92,\
                  1,False,GetTimestr(),GetTimestr(),'NULL',\
                  GetTimestr(),title]
    dictFV = dict(zip(listFields,listValues))
    print (dictFV['path'])
    strSQL= "insert into wagtailcore_page(id,path,depth,numchild,title,slug,live,has_unpublished_changes,url_path,seo_title,show_in_menus,search_description,go_live_at,expire_at,expired,content_type_id,owner_id,locked,latest_revision_created_at,first_published_at,live_revision_id,last_published_at,draft_title)\
    values(%d,'%s',%d,%d,'%s','%s',\
    %s,%s,'%s','%s',%s,\
    '%s',%s,%s,%s,%d,\
    %d,%s,'%s','%s',%s, \
    '%s','%s')" % (dictFV['id'],dictFV['path'],dictFV['depth'],dictFV['numchild'],dictFV['title'],dictFV['slug'],dictFV[ 'live'],dictFV['has_unpublished_changes'],dictFV['url_path'],dictFV['seo_title'],dictFV['show_in_menus'],dictFV[ 'search_description'],dictFV['go_live_at'],dictFV['expire_at'],dictFV['expired'],dictFV['content_type_id'],dictFV[ 'owner_id'],dictFV['locked'],dictFV['latest_revision_created_at'],dictFV['first_published_at'],dictFV['live_revision_id'],dictFV[ 'last_published_at'],dictFV['draft_title'])
    strSQL = ReHelper.subString(strSQL, "\'\'\'\'", "\'\'\'\'\'\'")
    postgresql.Insert(strSQL)
    #2.insert to news_newspage
    strSQL = "select id from wagtailcore_page where title = '%s' order by id" % dictFV['title']
    listResults = postgresql.GetoneList(strSQL,0)
    # the key is sequence
    valueID = listResults[len(listResults)-1]
    print ("the insert record valueID is %s" % valueID)
    content = ReHelper.subString(content, "\'", "\'\'")
    strSQL = "insert into news_newspage(page_ptr_id,publish_date,intro,body,visit_count) values(%d,'%s','%s','%s','%d')" % (valueID,publishDate,title,content,visitCnt)
    postgresql.Insert(strSQL)
    #insert the cvategories
    strSQL = "insert into news_newspage_categories(newspage_id,newscategory_id) values(%s, %s)" %(valueID,category)
    postgresql.Insert(strSQL)
    #updata
    strSQL = "select numchild from wagtailcore_page where slug = 'news-list'"
    numChild = postgresql.GetoneList(strSQL,0)[0] + 1
    print (numChild)
    strSQL = "update wagtailcore_page set numchild = %s where slug = 'news-list'" % str(numChild)
    postgresql.Update(strSQL)
postgresql.Close()
print("OK")

