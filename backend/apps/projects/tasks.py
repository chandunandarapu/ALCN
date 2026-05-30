from celery import shared_task


@shared_task
def send_project_email():

    print(
        "Project Email Sent Successfully"
    )

    return "Success"