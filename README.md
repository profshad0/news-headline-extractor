```markdown
# News Headline Extractor

This Python script fetches the latest news headlines from the NewsAPI and displays them in a formatted manner.

## Getting Started

To use this script, you will need to obtain an API key from NewsAPI.org. You can sign up for a free account to get your API key [here](https://newsapi.org/).

### Prerequisites

- Python 3.x
- requests library
  ```bash
  pip install requests
  ```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rodmutt/news-headline-extractor.git
   ```

2. Navigate to the project directory:

   ```bash
   cd news-headline-extractor
   ```

3. Replace `'YOUR_API_KEY'` in the script with your actual NewsAPI key.

4. Run the script:

   ```bash
   python news_extractor.py
   ```

## Usage

The script fetches the latest news headlines from the NewsAPI and displays them in a formatted manner. Each headline is prefixed with a number indicating its position in the list.

## Example Output

```
1. Headline 1
2. Headline 2
3. Headline 3
...
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [NewsAPI](https://newsapi.org/) for providing the news headlines API.
- Contributors to the [requests](https://github.com/psf/requests) library.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.
```
