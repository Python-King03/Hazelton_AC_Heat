import os
import boto3


AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
SES_FROM = os.environ["SES_FROM"]   # e.g. leads@mail.hazeltonhvac.com
SES_TO = os.environ["SES_TO"]       # e.g. info@hazeltonhvac.com


def send_lead_email(subject: str, body_text: str, reply_to: str | None = None) -> None:
    client = boto3.client(
        "ses",
        region_name=AWS_REGION,
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    )

    payload = {
        "Source": SES_FROM,
        "Destination": {"ToAddresses": [SES_TO]},
        "Message": {
            "Subject": {"Data": subject, "Charset": "UTF-8"},
            "Body": {"Text": {"Data": body_text, "Charset": "UTF-8"}},
        },
    }

    if reply_to:
        payload["ReplyToAddresses"] = [reply_to]

    client.send_email(**payload)

