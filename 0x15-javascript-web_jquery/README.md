# 0x15. JavaScript - Web jQuery

This project is a demonstration of fetching and displaying translations of the word "Hello" in different languages using JavaScript and the jQuery library.

## Overview

The project consists of the following files:

- **102-main.html**: HTML file containing the user interface for entering language codes and displaying translations.
- **102-script.js**: JavaScript file containing the logic to fetch translations from the API and update the UI.
- **README.md**: This file, providing an overview and instructions for the project.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine using `git clone`.
2. Open the `102-main.html` file in a web browser.
3. Enter a language code (e.g., `es`, `fr`, `en`) into the input field labeled "Language code".
4. Click the "Translate" button or press the Enter key to fetch and display the translation of "Hello" in the language specified.

## Dependencies

- jQuery library (included via CDN): Used for making AJAX requests and manipulating the DOM.

## Troubleshooting

If the translations are not displayed correctly or the application is not functioning as expected, consider the following troubleshooting steps:

- Check your network connection to ensure you can access the internet.
- Verify that the API service (`https://www.fourtonfish.com/hellosalut/hello/`) is accessible and returns the expected JSON response.
- Review the browser console for any error messages or warnings.
- Ensure that the project files (`102-main.html` and `102-script.js`) are located in the same directory and properly linked.
- Test the project in a different web browser to see if the issue is browser-specific.

## Credits

- API service: [Fourtonfish - Hello Salut](https://www.fourtonfish.com/hellosalut/)

## License

This project is licensed under the [MIT License](LICENSE).
