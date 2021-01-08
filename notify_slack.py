import slackweb
import os


class Notify_Slack:

    def __init__(self):
        self.webhook = os.getenv('SLACK_WEBHOOK')
        self.attachments = ""

    def notify(self, text):
        self.attachments = [
            {
                "color": "#32cd32",
                "author_name": "【正常終了メッセージ通知】",
                "text": text
            }
        ]

        slack = slackweb.Slack(url=self.webhook)
        slack.notify(attachments=self.attachments)

    def failed(self, text):
        self.attachments = [
            {
                "color": "#ff6347",
                "author_name": "【異常終了メッセージ通知】",
                "text": text
            }
        ]

        slack = slackweb.Slack(url=self.webhook)
        slack.notify(attachments=self.attachments)
