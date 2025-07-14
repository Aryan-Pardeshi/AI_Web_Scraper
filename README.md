# AI Web Scraper

This project is a Python-based web scraper that uses Selenium to extract content from a website and then leverages the Gemini AI to parse that content based on user-provided instructions.

## Features

  * **Web Scraping**: Utilizes Selenium to scrape the full DOM content of a given URL.
  * **Content Parsing**: Employs the Gemini Large Language Model to parse and extract specific information from the scraped content.
  * **Streamlit Interface**: Provides a simple web-based user interface using Streamlit to input the URL and the parsing instructions.
  * **Proxy Support**: Includes a commented-out implementation for using proxies to avoid getting blocked.

## Project Structure

```
.
├── main.py               # The main streamlit application
├── scrape.py             # Contains functions for scraping websites using Selenium
├── parse.py              # Contains functions for parsing content with Gemini AI
├── requirements.txt      # Lists the Python dependencies for the project
[cite_start]├── proxies.txt           # A list of proxy servers [cite: 1]
[cite_start]├── .gitignore            # Specifies files to be ignored by Git [cite: 2]
└── .env                  # For storing environment variables (you need to create this)
```

## How to Set Up and Run the Project

### 1\. **Clone the Repository**

First, clone this repository to your local machine.

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2\. **Install Dependencies**

[cite\_start]Install all the necessary Python libraries using the `requirements.txt` file[cite: 3].

```bash
pip install -r requirements.txt
```

### 3\. **Set Up the `.env` File**

You will need a `.env` file to store your Gemini API key.

1.  Create a new file named `.env` in the root of the project directory.
2.  Add your Gemini API key to this file as shown below:

<!-- end list -->

```
GEMINI_API_KEY="your_gemini_api_key_here"
```

### 4\. **Download ChromeDriver**

This project uses Selenium with Chrome, so you need to have the Chrome browser and the corresponding ChromeDriver installed. You can download ChromeDriver from the official website. Make sure the version of ChromeDriver matches your version of Chrome.

Place the `chromedriver.exe` (or `chromedriver` for Linux/Mac) in the root directory of the project, or provide the correct path to it in `scrape.py`.

### 5\. **Run the Application**

Once you have completed the setup, you can run the Streamlit application with the following command:

```bash
streamlit run main.py
```

## How to Use the Application

1.  Run the application, and it will open in your web browser.
2.  Enter the full URL of the website you want to scrape (including `https://`).
3.  Click the **Scrape Site** button.
4.  Once the content is scraped, a text area will appear where you can describe what information you want to extract from the page.
5.  Click the **Parse Content** button to get the desired information.

## Credits

This project was inspired by and built with the help of resources from [googleusercontent.com/youtube.com/0](https://youtu.be/Oo8-nEuDBkk?si=xYM18PX9mjhGgC8E).