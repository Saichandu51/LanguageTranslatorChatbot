import json
import boto3

translate = boto3.client("translate", region_name="us-east-1")
comprehend = boto3.client("comprehend", region_name="us-east-1")


def lambda_handler(event, context):
    try:
        print("Received Event:", json.dumps(event, indent=2))  # Debugging

        # Check if body exists
        body = json.loads(event["body"]) if "body" in event else event
        text = body.get("text", "").strip()
        target_language = body.get("language", "en")

        if not text:
            return {
                "statusCode": 400,
                "headers": {
                    "X-Content-Type-Options": "nosniff",
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type"
                },
                "body": json.dumps({"error": "No text provided"})
            }

        # Step 1: Detect the Source Language
        detect_response = comprehend.detect_dominant_language(Text=text)
        source_language = detect_response["Languages"][0]["LanguageCode"] if detect_response["Languages"] else "en"

        # Step 2: Translate Text
        translate_response = translate.translate_text(
            Text=text,
            SourceLanguageCode=source_language,
            TargetLanguageCode=target_language
        )

        return {
            "statusCode": 200,
            "headers": {
                "X-Content-Type-Options": "nosniff",
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "translated_text": translate_response["TranslatedText"],
                "detected_language": source_language
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "X-Content-Type-Options": "nosniff",
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"error": str(e)})
        }