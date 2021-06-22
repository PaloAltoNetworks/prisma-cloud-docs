"""
TwDownloaderMiddleware

  Rewrite request URL: https://stackoverflow.com/questions/34437204/how-to-change-request-url-before-making-request-in-scrapy
  Scrapy Request object: /Users/ian/Documents/Twistlock/Docs/v2.4/scrapy_docs/scrapy-latest/index.html

  HACKED: I should really be using functions like urlparse.urljoin and os.path.join for manipulating paths, instead of using string functions.
  Come back and fix this.

  https://docs.python.org/2/library/urlparse.html
  https://stackoverflow.com/questions/1793261/how-to-join-components-of-a-path-when-you-are-constructing-a-url-in-python
  https://stackoverflow.com/questions/2736144/python-add-trailing-slash-to-directory-string-os-independently

"""

from scrapy.http import Request, Response
from scrapy.exceptions import IgnoreRequest

class TwDownloaderMiddleware(object):

    """
      Rewrite the request URL

      Expected input format:

         https://docs.twistlock.com/docs/latest/welcome/index.html

      Rewritten output format:

         file:///<tw_doc_site_local>/<tw_asciibinder_prefix>/latest/welcome/index.html
         file:///Users/ian/Documents/Twistlock/Docs/v2.4/test-algolia/doc-site/_package/main/latest/welcome/index.html

    """
    def process_request(self, request, spider):

        #DEBUG
        #print("spider.tw_doc_site_url=", spider.tw_doc_site_url)
        #print("spider.tw_doc_site_local=", spider.tw_doc_site_local)
        #print("spider.tw_asciibinder_prefix=", spider.tw_asciibinder_prefix)

        if request.url[:8] == "file:///":
            # Process it.
            #DEBUG
            #print "tw: REQUEST Process the following local file:", request.url
            return None

        # OTHERWISE: Modify the URL, and send it back for processing again.
        # Get the protocol indendent portion of the link.
        # That is, cut out https://docs.twistlock.com/docs.
        # Understanding Python's slice notation: https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation

        # Works - orig
        #print("Request url", request.url)
        #new_url = "file:///Users/ian/Documents/Twistlock/Docs/v2.4/test-algolia/doc-site/_package/main/" + request.url[32:]
        #print("Request new_url: ", new_url)

        char_count = len(spider.tw_doc_site_url)
        if spider.tw_doc_site_url in request.url:
            new_url = "file://" + spider.tw_doc_site_local + spider.tw_asciibinder_prefix + request.url[char_count:]
            #DEBUG
            #print "tw: REQUEST: Rewrite", request.url, "to", new_url
            request = request.replace(url=new_url)
            return request
        else:
            return IgnoreRequest

    """
      Reverse the rewrite because we want the correct URL written to the search index.
    """
    def process_response(self, request, response, spider):

        # Works - orig
        #new_url = "https://docs.twistlock.com/docs" + response.url[83:]
        #print("Response new_url: ", new_url)
        #response = response.replace(url=new_url)
        #return response

        local_url = "file://" + spider.tw_doc_site_local + spider.tw_asciibinder_prefix
        char_count = len(local_url)
        if local_url in response.url:
            if spider.tw_staging:
                new_url = spider.tw_doc_site_staging_url + response.url[char_count:]
            else:
                new_url = spider.tw_doc_site_url + response.url[char_count:]
            new_response = response.replace(url=new_url)
            #DEBUG
            #print "tw: RESPONSE Rewrite URL from:", response.url, "to", new_response.url
            return new_response
        else:
            return response


