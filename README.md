
# ShowYourSendingEmail
ShowYourSendingEmail is a Python script that utilizes the Gmail API to check if emails have been sent to specific addresses. It allows users to input a list of email addresses or specify a file containing the addresses and then checks each address against the user's sent emails.



https://github.com/BabylooPro/ShowYourSendingEmail.py/assets/35376790/dc488fa1-17c9-4951-a8a0-de75944a7e59



## Installation and Configuration
### Prerequisites
- Python 3
- Pip (Python package manager)
- Access to a Google Cloud Platform account

### Steps
1. Clone the repository or download the script [ShowYourSendingEmail.py](ShowYourSendingEmail.py).
2. Install the required Python libraries:
   ```
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```
3. Set up a project in Google Cloud Platform and enable the Gmail API. Follow the detailed instructions in the [Configuring Google Cloud Platform for Gmail API](#configuring-google-cloud-platform-for-gmail-api) section.
5. Run the script once to authenticate and create a `token.pickle` file:
   ```
   python ShowYourSendingEmail.py
   ```

## Usage
To run the script:
```
python ShowYourSendingEmail.py
```
Follow the prompts to enter either a list of email addresses separated by commas or the path to a file containing the email addresses.

## Configuring Google Cloud Platform for Gmail API
Before you can use the script, you need to set up the Gmail API through Google Cloud Platform. Follow these steps:

1. **Create a project on Google Cloud Platform**:
   - Log in to [Google Cloud Console](https://console.cloud.google.com/).
   - Click on the navigation menu in the top left corner and select "IAM & Admin" > "Manage Resources".
   - Click on "CREATE PROJECT" and follow the instructions to create a new project.

2. **Activate the Gmail API**:
   - In the project dashboard, go to "API & Services" > "Library".
   - Search for "Gmail API" and select it.
   - Click on "ENABLE" to activate the API for your project.

3. **Create OAuth 2.0 credentials**:
   - Go to "API & Services" > "Credentials".
   - Click on "Create Credentials" and select "OAuth client ID".
   - Configure the OAuth consent screen with the necessary information.
   - For the application type, select "Desktop app" and give it a name.
   - Click on "Create". Your OAuth client credentials will be created.

4. **Download the `credentials.json` file**:
   - Once the credentials are created, click on the "Download JSON" button next to the OAuth credentials you just created.
   - Save this file as `credentials.json` in the same folder as your `ShowYourSendingEmail.py` script.

## Contributions
Contributions to the project are welcome. Please follow standard pull request procedures and ensure code quality and security best practices.

## License
This project is under the MIT License. See the [LICENSE](LICENSE) file for more details.
