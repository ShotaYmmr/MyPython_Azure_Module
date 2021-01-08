import subprocess


class Al_Chenge:
    def __init__(self):
        self.name = ""
        self.rg = ""
        self.bl = ""
        self.al_chg_cmd = ""

    # Azure Monitor Alert Ruleを検索
    def alert_serch(self, name, rg):
        self.name = name
        self.rg = rg

        self.al_src_cmd = subprocess.check_output(
            'az monitor metrics alert show --name ' + self.name + " --resource-group " + self.rg, shell=True)

    # Azure Monitor Alert Ruleのステータスを変更
    def alert_chenge(self, name, rg, bl):
        self.name = name
        self.rg = rg
        self.bl = bl

        self.al_chg_cmd = subprocess.check_output('az monitor metrics alert update --enabled ' + self.bl +
                                                  ' --name ' + self.name + ' --resource-group ' + self.rg, shell=True)
