# QuizMaster

QuizMaster is a simple quiz application built using Python and Tkinter. It presents trivia questions to the user and allows them to answer by selecting true or false. The user's score is calculated based on their correct answers, and the application provides immediate feedback with color-coded indicators.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/quizmaster.git`
2. Navigate to the project directory: `cd quizmaster`

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Run the `main.py` file: `python main.py`
3. The QuizMaster application window will open.
4. Read the question displayed on the canvas.
5. Click the "True" button if you think the statement is true, or click the "False" button if you think the statement is false.
6. Receive immediate feedback on your answer with a colored background on the canvas.
7. The score label will be updated accordingly.
8. The next question will be automatically displayed after a brief delay.
9. Continue answering questions until the quiz is complete.
10. The canvas will display "GAME OVER" once all questions have been answered.
11. You can close the application window to exit the program.

## Customization

- You can modify the quiz questions by editing the `data.py` file. The `data` dictionary contains the list of questions and answers.
- You can customize the appearance of the GUI by modifying the styles and properties in the `Gui` class in the `gui.py` file.
- You can add more images for the true and false buttons by placing the image files in the "images" directory and updating the file paths in the `Gui` class.

## Dependencies

This project requires the following dependencies:
- Python 3.x
- tkinter (included with Python)

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


## API Usage

This project utilizes the opentdb.com API for retrieving quiz data. Please note that the usage of the opentdb.com API is subject to their terms of service and licensing agreements. You can find more information about their API and usage guidelines on the [opentdb.com website](https://opentdb.com).

It is your responsibility to ensure compliance with the opentdb.com terms of service and any licensing requirements when using their API in your project.


