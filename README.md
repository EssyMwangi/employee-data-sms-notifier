# Twilio SMS Employee Notifier

This Python script uses the Twilio API to send SMS notifications with the count of employees from a CSV file.

## Features

- Reads employee data from a CSV file.
- Counts the number of employees.
- Sends an SMS notification with the employee count using the Twilio service.

## Getting Started

### Prerequisites

- Python 3.x
- [Create a Twilio account](https://www.twilio.com/try-twilio)
- Obtain your Twilio Account SID, Auth Token, Twilio phone number, and destination phone number.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/EssyMwangi/employee-data-sms-notifier.git

2. Navigate to the project directory:

    ```bash
    cd employee-data-sms-notifier

3. Create a virtual environment:

    ```bash
    python -m venv venv

4. Activate the virtual environment:

    On Windows:

        ```bash
        .\venv\Scripts\activate
 
    On Unix or MacOS:

        ```bash
        source venv/bin/activate

5. Install dependencies:

    ```bash
    pip install -r requirements.txt

6. Create a .env file in the project directory and add your Twilio credentials:

    ```bash
    TWILIO_ACCOUNT_SID=your_account_sid
    TWILIO_AUTH_TOKEN=your_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    DESTINATION_PHONE_NUMBER=destination_phone_number

### Usage 

    Run the script

### Contributing

    Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

### License

    This project is licensed under the MIT License - see the LICENSE file for details.

    ```bash
    
    This Markdown code provides the structure for your README, including headers, bullet points, code snippets, and links. Feel free to further customize it based on your specific project details.






