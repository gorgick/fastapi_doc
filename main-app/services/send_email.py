from asyncio import sleep
from email.message import EmailMessage

import aiosmtplib

from tables import Deribit


async def send_email(recipient: str, subject: str, body: str):
    admin_email = "admin@site.com"

    message = EmailMessage()
    message["From"] = admin_email
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    await aiosmtplib.send(
        message,
        sender=admin_email,
        recipients=[recipient],
        hostname="192.168.99.100",
        port=1025
    )


async def send_welcome_email(deribit: Deribit):
    await sleep(5)
    await send_email(
        recipient=deribit.email,
        subject="Welcome",
        body=f"Hello {deribit.name}"
    )
