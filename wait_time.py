from datetime import datetime, timedelta
from notify_slack import Notify_Slack
import sched
import time
import sys


class Wait_Time:

    def __init__(self):
        self.date = [0]
        self.start = [0]
        self.end = [0]
        self.slack = Notify_Slack()

# 指定時刻の整合性チェック
    def date_check(self, start, end):
        self.start = start
        self.end = end

        # 開始時刻のテスト
        now = datetime.now()
        now = datetime(now.year, now.month, now.day,
                       now.hour, now.minute, now.second)
        comp = datetime(self.start[0], self.start[1],
                        self.start[2], self.start[3], self.start[4], 0)
        diff = comp - now

        if int(diff.days) >= 0:
            print("OK (^ω^)")

        else:
            self.slack.failed("設定時刻を確認してください\nError：開始時刻が現在時刻より過去に設定されています。")
            print("Error：開始時刻が現在時刻より過去に設定されています。")
            sys.exit(1)

        # 終了時刻のテスト
        now = datetime.now()
        now = datetime(now.year, now.month, now.day,
                       now.hour, now.minute, now.second)
        comp = datetime(self.end[0], self.end[1],
                        self.end[2], self.end[3], self.end[4], 0)
        diff = comp - now

        if int(diff.days) >= 0:
            print("OK (^ω^)")

        else:
            self.slack.failed("設定時刻を確認してください\nError：終了時刻が現在時刻より過去に設定されています。")
            print("Error：終了時刻が現在時刻より過去に設定されています。")
            sys.exit(1)

        # 開始と終了のテスト
        now = datetime(self.start[0], self.start[1],
                       self.start[2], self.start[3], self.start[4], 0)
        comp = datetime(self.end[0], self.end[1],
                        self.end[2], self.end[3], self.end[4], 0)
        diff = comp - now

        if int(diff.days) == 0:
            if int(diff.seconds) == 0:
                print("同じ時間やで！！")
                sys.exit(1)
            else:
                print("OK (^ω^)")

        elif int(diff.days) >= 0:
            print("OK (^ω^)")
        else:
            self.slack.failed("設定時刻を確認してください\nError：終了時刻が現在時刻より過去に設定されています。")
            print("Error：終了時刻が現在時刻より過去に設定されています。")
            sys.exit(1)

        # 指定した時間まで待機する

    def wf_stop(self, date):
        self.date = date

        def stdout(output):
            print(output)

        now = datetime.now()
        now = datetime(now.year, now.month, now.day,
                       now.hour, now.minute, now.second)
        comp = datetime(self.date[0], self.date[1],
                        self.date[2], self.date[3], self.date[4], 0)
        diff = comp - now

        if int(diff.days) >= 0:
            scheduler = sched.scheduler(time.time, time.sleep)
            scheduler.enter(diff.seconds, 1, stdout, ("Done!!!", ))
            scheduler.run()
        else:
            print("静観終了終了処理に移行します！")
