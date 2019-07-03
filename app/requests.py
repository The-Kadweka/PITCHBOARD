# import urllib.request,json
# from .models import Pitch
#
# def get_quote():
#     '''
#     Function to get random quote
#     '''
#     with urllib.request.urlopen(quote_url) as url:
#         quote_data = url.read()
#         quote_response = json.loads(quote_data)
#
#         quote_result = None
#
#         if quote_response:
#             author = quote_response.get('author')
#             quote = quote_response.get('quote')
#             permalink = quote_response.get('permalink')
#
#             quote_result = Quote(author, quote, permalink)
#
#         return quote_result
