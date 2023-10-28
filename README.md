# Clash of Clans API Web Application

This is a Python web application that utilizes the Clash of Clans API to fetch information about clans and display it to users.
The application consists of several components, including the main Python script and three HTML templates for different pages.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3
- Flask
- Requests library

You can install Flask and Requests using pip:

```bash
pip install flask
pip install requests
Components
```
# Components

## `main.py`

`main.py` is the core of the application. It uses the Flask web framework to handle routing and interactions with the Clash of Clans API. The key functions in `main.py` include:

- Fetching data from the Clash of Clans API using an API key.
- Handling routes for the home page, search result page, and detailed clan page.
- Running the Flask application.

## `templates/index.html`

`index.html` is the template for the home page of the application. It provides a user interface for searching for clans. Key features include:

- A search form that takes a clan name as input.
- Bootstrap styling for a clean and responsive design.
- A navigation bar with the title "COC API."

## `templates/SResult.html`

`SResult.html` is the template for the search result page. It displays information about clans based on the search query. Key features include:

- Displaying clan information in a card format.
- Information such as clan badge, name, tag, trophy count, type, and the number of members.
- Links to view detailed clan information.

## `templates/clan.html`

`clan.html` is the template for the detailed clan information page. It displays comprehensive information about a specific clan, including its badge, name, tag, description, and member list. Key features include:

- Clan information displayed within a card element.
- A table displaying member information, including rank, name, experience level, trophies, and donations.

## API Key

To use the Clash of Clans API, you need to provide your API key. Replace the key variable in `main.py` with your own key.

```python
key = "your-api-key-here"
```

## Usage

1. Clone this repository to your local computer using:
```
git clone <repository url>
```

2. Run the Flask application using:
```python
python3 main.py
```
The application will start running on http://localhost:5000/.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Clash of Clans API](https://developer.clashofclans.com/)
- [Bootstrap](https://getbootstrap.com/) for providing a responsive and visually appealing framework for web styling.
