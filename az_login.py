import os
import sys
import subprocess


class Az_KeyVault_Login:
    def __init__(self):
        # ENV
        # self.client_id = ""
        # self.sec_token = ""
        self.tenant_id = "649b580a-66f6-4d4a-9dc2-f9a3658a9711"
        # self.keyuser = ""
        self.keyvaultname = "test-keyvault-555555"
        # CMD
        self.az_login_cmd = ""
        self.keyvault_id_cmd = 'az keyvault secret show --vault-name ' + \
            self.keyvaultname + ' --name key-test-ids --query value'
        self.keyvault_sec_cmd = 'az keyvault secret show --vault-name ' + \
            self.keyvaultname + ' --name key-test-sec --query value'

    def az_login(self, ids, sec, tenant):
        client_id = ids
        sec_token = sec
        tenant_id = tenant

        try:
            self.az_login_cmd = subprocess.check_output(
                'az login --service-principal -u ' + client_id + ' -p ' + sec_token + ' --tenant ' + tenant_id, shell=True).decode('UTF-8')
            # print(self.az_login_cmd) #Debug
        except:
            print("Azureへのログインに失敗しました。")
            sys.exit(1)

        print("Azureへのログインに成功しました。")

    def keyvault_login(self,):
        login = Az_KeyVault_Login()

        self.keyvault_id_cmd = subprocess.check_output(
            self.keyvault_id_cmd, shell=True).decode('UTF-8')
        ids = str(self.keyvault_id_cmd.strip())
        # print(ids) # Debug

        self.keyvault_sec_cmd = subprocess.check_output(
            self.keyvault_sec_cmd, shell=True).decode('UTF-8')
        sec = str(self.keyvault_sec_cmd.strip())
        # print(sec) # Debug
        login.az_login(ids, sec, self.tenant_id)
