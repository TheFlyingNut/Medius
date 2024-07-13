import os
import django
from django.core.mail import EmailMessage
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# Email configuration
subject = "Python (Selenium) Assignment - Kartik Dubey"
message = "This is my official submission of the assignment for the internship assignment for web scraping. To fill the google form I used selenium web drivers which you will find worked using the attached screenshot. To send the email I created a simple Django app and used the send mail() function after setting up the environment. I look forward to your reply."
recipient_list = ["tech@themedius.ai", "hr@themedius.ai"]
image_path = r"C:\Users\karti\OneDrive\Pictures\Screenshots\Screenshot (80).png"  # Replace with the actual path to your image

# Send email
email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)

# Attach the image
with open(image_path, 'rb') as f:
    email.attach('image.png', f.read(), 'image/png')

# Send the email
email.send(fail_silently=False)
print("Email sent successfully!")