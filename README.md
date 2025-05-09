"# Language Translation Chatbot" 
# Language Translation Chatbot

This is a **Language Translation Chatbot** built using AWS services. It allows users to input text and receive translated output in real-time. The solution leverages several AWS services such as **AWS Lambda**, **API Gateway**, **Amazon Translate**, and **S3** to provide a seamless, serverless experience.

## Features
- **Real-time translation**: Instant translation of text from one language to another.
- **Multi-language support**: Supports translation between multiple languages.
- **Simple user interface**: A straightforward web-based UI for ease of use.
- **Serverless architecture**: Built using AWS Lambda for backend logic, ensuring scalability and low costs.
- **Secure API access**: Utilizes IAM roles to provide secure access to backend resources.

## Architecture

The system uses a **serverless architecture** powered by AWS services:
- **Frontend**:
  - A static website is hosted on **Amazon S3**. It contains an input box for the text to be translated, a language selection dropdown, and a translate button.
  - The frontend is built with HTML, CSS, and JavaScript.
  
- **Backend**:
  - **AWS Lambda** functions handle the backend logic, processing the translation request.
  - **Amazon Translate** is used to perform the actual text translation.
  - **API Gateway** is configured to expose the Lambda function as a RESTful API.
  
- **Permissions**:
  - **IAM roles** are used to manage access and permissions securely across AWS services.

## Installation

### Prerequisites
- AWS account
- AWS CLI configured
