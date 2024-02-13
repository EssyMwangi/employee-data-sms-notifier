import csv
from twilio.rest import Client
import os
from dotenv import load_dotenv

class TwilioSMS:
    def __init__(self):
        load_dotenv()

        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
        self.destination_phone_number = os.getenv('DESTINATION_PHONE_NUMBER')

    def read_employee_data(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            # Additional to exempt header
            next(reader, None)
            employee_data = list(reader)
        return employee_data

    def count_employees(self, employee_data):
        return len(employee_data)

    def send_sms(self, employee_count):
        client = Client(self.account_sid, self.auth_token)
        message_body = f"The Number of Employees in EssyOrg is: {employee_count}"
        message = client.messages.create(
            body=message_body,
            from_=self.twilio_phone_number,
            to=self.destination_phone_number
        )
        print(f"SMS sent with SID: {message.sid}")

if __name__ == "__main__":
    twilio_sms = TwilioSMS()
    file_path = 'employee_data.csv'

    try:
        employees = twilio_sms.read_employee_data(file_path)
        employee_count = twilio_sms.count_employees(employees)
        twilio_sms.send_sms(employee_count)
    except Exception as e:
        print(f"An error occurred: {e}")
