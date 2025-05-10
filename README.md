# 🌐 Language Translation Chatbot using AWS

![Chatbot Preview](https://your-screenshot-url.com/preview.png)
<!-- Replace the above URL with an actual screenshot of your chatbot interface -->

[![AWS](https://img.shields.io/badge/AWS-Translate-orange?logo=amazon-aws)](https://aws.amazon.com/translate/)
[![S3 Hosted](https://img.shields.io/badge/S3-Static_Hosting-blue?logo=amazon-s3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
[![Lambda](https://img.shields.io/badge/Lambda-Backend-yellow?logo=aws-lambda)](https://aws.amazon.com/lambda/)
[![API Gateway](https://img.shields.io/badge/API-Gateway-red?logo=amazon-api-gateway)](https://aws.amazon.com/api-gateway/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📽️ Live Demo

👉 [Try the chatbot here](https://language-translation-chandu.s3.us-east-1.amazonaws.com/index.html)

---

## 🚀 Features

- 🌍 Translate text into multiple languages using Amazon Translate.
- 💬 User-friendly chatbot interface for seamless interaction.
- ⚡ Serverless backend powered by AWS Lambda.
- 🔗 Secure and scalable API integration via Amazon API Gateway.
- ☁️ Static website hosting using Amazon S3.

---

## 🧰 Tech Stack

| Component      | Technology Used              |
|----------------|------------------------------|
| Frontend       | HTML, CSS, JavaScript        |
| Backend        | AWS Lambda (Python)          |
| Translation    | Amazon Translate             |
| API Layer      | Amazon API Gateway           |
| Hosting        | Amazon S3 Static Hosting     |

---

## 📁 Project Structure

language-translation-chatbot/
├── index.html # Main UI
├── styles.css # Styling for chatbot
├── script.js # JavaScript logic to handle input/output and API call
├── lambda_function.py # AWS Lambda function code

---

## 🛠️ Setup Instructions

### 1. Frontend Setup (S3 Hosting)

1. **Create an S3 Bucket:**
   - Enable **Static Website Hosting**.
   - Set permissions to allow public read access to these files.

2. **Upload Files:**
   - `index.html`, `styles.css`, and `script.js`.

3. **Note the Static Website Endpoint:**
   - This will be your frontend URL.

### 2. Lambda Function (Backend)

1. **Create a Lambda Function:**
   - Runtime: Python 3.x.

2. **Add the Following Code:**
   ```python
   import boto3
   import json

   def lambda_handler(event, context):
       body = json.loads(event['body'])
       text = body['text']
       target_lang = body['targetLang']

       translate = boto3.client('translate')
       result = translate.translate_text(
           Text=text,
           SourceLanguageCode='auto',
           TargetLanguageCode=target_lang
       )

       return {
           'statusCode': 200,
           'headers': { "Access-Control-Allow-Origin": "*" },
           'body': json.dumps({ 'translatedText': result['TranslatedText'] })
       }
Set Permissions:

Ensure the Lambda function has permissions to use Amazon Translate.

3. API Gateway (Trigger Lambda)
Create a REST API:

Add a POST method and integrate it with your Lambda function.

Enable CORS:

To allow cross-origin requests from your frontend.

Deploy the API:

Note the Invoke URL.

4. Connect Frontend to API
In your script.js, replace the API URL placeholder with your deployed API Gateway invoke URL:
const API_URL = ''; #Replace with your API URL

💬 Example Usage
Input: Hello, how are you?

Select Language: French

Click Translate

Output: Bonjour, comment ça va ?

🔒 Security Notes
Ensure no secret keys are exposed in frontend code.

Use IAM roles and resource-based policies for secure Lambda and API access.

Consider adding throttling or usage limits in API Gateway for public-facing APIs.

📌 Future Enhancements
Add language detection and selection dynamically.

Integrate Amazon Polly for voice output.

Add chatbot flow using Amazon Lex.


