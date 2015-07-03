
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.encoding import smart_str
 
class GeoRedirectMiddleware(object):
 
    def __init__(self):
        # Pull in and grab our conf for this from various settings files
        # (could probably drop the if/elses here)
        try:
            self.DEBUG_IP = settings.DEBUG_IP
        except AttributeError:
            self.DEBUG_IP = False

    def get_city_from_ip(self, request):
        if self.DEBUG_IP:
            inbound_ip = self.DEBUG_IP
        else:
            inbound_ip = request.META['REMOTE_ADDR']
         
        print inbound_ip

        from django.contrib.gis.geoip import GeoIP

        gip = GeoIP()
        info = gip.city(inbound_ip)
        if not info:
            info = {}
        info['ip'] = inbound_ip
        return info


    # def process_request(self, request):
    #     """
    #     This middleware lets you match a specific url and redirect the request to a
    #     new url.

    #     You keep a tuple of url regex pattern/url redirect tuples on your site
    #     settings, example:

    #     URL_REDIRECTS = (
    #         (r'www\.example\.com/hello/$', 'http://hello.example.com/'),
    #         (r'www\.example2\.com/$', 'http://www.example.com/example2/'),
    #     )

    #     """        
    #     host = request.META['HTTP_HOST'] + request.META['PATH_INFO']
    #     for url_pattern, redirect_url in settings.URL_REDIRECTS:
    #         regex = re.compile(url_pattern)
    #         if regex.match(host):
    #             return HttpResponsePermanentRedirect(redirect_url)            
 
 
    def process_response(self, request, response):
        info = self.get_city_from_ip(request)
        
        allow_list = ['Toronto']

        try:
            if info['city'] not in allow_list:
                inject_data = render_to_string('search/region_error.html', info)
         
                if '/admin' not in request.path and inject_data: 
                    response.content = smart_str(inject_data)                
                return response

        except KeyError:
            info['city'] = ''
 
        inject_data = """
            <p>IP: %s <br />
            City: %s
            </p>        
        """ % (info['ip'], info['city'])
        response.content +=  smart_str(inject_data)
        return response
 