import requests

def extract_news(api_key):
    # URL of the NewsAPI endpoint
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

    # Send a GET request to the NewsAPI endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and display the headlines
        articles = data.get('articles', [])
        for idx, article in enumerate(articles, start=1):
            title = article.get('title', '')
            print(f"{idx}. {title}")
    else:
        print("Failed to retrieve news. Status code:", response.status_code)

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    extract_news(api_key)
