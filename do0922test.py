
if __name__ == '__main__':
    str = '''"gallery_images": [], "show_in_menus": false, "url_path": "/home/news-list/\u4fee\u6539\u7248\u672c\u6d4b\u8bd5/", "last_published_at": null, "owner": 1, "search_description": "", "intro": "li", "first_published_at": null, "go_live_at": null, "title": "\u4fee\u6539\u7248\u672c\u6d4b\u8bd5", "publish_date": "2017-09-22", "seo_title": "", "content_type": 92, "visit_count": 5, "path": "0001000100010004", "categories": [1], "latest_revision_created_at": null, "slug": "\u4fee\u6539\u7248\u672c\u6d4b\u8bd5", "locked": false, "has_unpublished_changes": false, "live": true, "expired": false, "live_revision": null, "expire_at": null, "depth": 4, "body": "<p>5875</p>", "draft_title": "\u4fee\u6539\u7248\u672c\u6d4b\u8bd5", "numchild": 0, "pk": 11'''
    list = str.split(',')
    for item in list:
        print (item)
    print(2)