import pprint
import requests

class News_Fetch:
    def fetch_news_from_API(self,secret,query,no_of_results): # Sample query = "self regulation of social media content" 
                                                                # Sample secret key = "964ec43497744754a3e2fc490dca3054"
        # Define the endpoint
        url = 'https://newsapi.org/v2/everything?'

        # Specify the query and number of returns
        parameters = {
            'q': query, # query phrase
            'pageSize': no_of_results,  # maximum is 100
            'apiKey': secret # your own API key
        }

        # Make the request
        response = requests.get(url, params=parameters)

        # Convert the response to JSON format and pretty print it
        response_json = response.json()
        pprint.pprint(response_json)

        #Print only headlines or titles
        for i in response_json['articles']:
            print(i['title'])