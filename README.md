# Recommendation-system_in-Flask-app

This is a Flask-based movie recommendation system that suggests similar movies based on user input. It utilizes cosine similarity between movie titles and images using TF-IDF vectors.

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/Mohanraj2622/movie-recommendation.git
   ```

2. Navigate to the project directory:
   ```
   cd movie-recommendation
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Make sure you have the `Western Wear.csv` file containing movie data in the project directory.

## Usage

To run the movie recommendation system, execute the following command:
```
python app.py
```
Then, open your web browser and navigate to `http://127.0.0.1:5000/`.

1. Enter the name of a movie in the input field on the homepage.
2. Click on the "Recommend" button.
3. The system will display a list of recommended movies based on your input.

## Files Structure

- `app.py`: Contains the Flask application code.
- `index.html`: HTML template for the homepage.
- `recommendations.html`: HTML template to display recommended movies.
- `not_found.html`: HTML template for the case when the input movie is not found.
- `Western Wear.csv`: CSV file containing movie data.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request. Make sure to follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

