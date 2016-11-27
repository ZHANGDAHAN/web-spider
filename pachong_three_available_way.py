url = "http://www.baidu.com"
import urllib2
print "first way"
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())


print "second way"
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())


print "third way"
import cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())

print "print cj of the web"
print cj