import pexpect.popen_spawn as pspawn
import time

# 実行したいOSコマンド
command = "ssh -L port:IP:port -R port:IP:port -o ExitOnForwardFailure=yes -o ServerAliveInterval=60 example@exmaple.com"
reset_command = "pkill -U user"
password = ""


def execute_os_command():
    while True:
        try:
            # コマンドの実行 (PopenSpawnを使用)
            child = pspawn.PopenSpawn(command)

            # "assword"の入力待ち
            index = child.expect([r'.*assword.*', r'.*ogin.*', pexpect.EOF, pexpect.TIMEOUT])
            
            if index == 0:
                # パスワードの入力
                child.sendline(password)

                # "ogin"の文字列を受け取った場合、pkillを実行
                index2 = child.expect([r'.*ogin.*', pexpect.EOF, pexpect.TIMEOUT])
                if index2 == 0:
                    child.sendline(reset_command)
                    time.sleep(5)
                    continue

            elif index == 1:
                # "ogin"が表示された場合の処理
                child.sendline("pkill -U user")
                time.sleep(5)

            # 再度コマンドを実行
            child = pspawn.PopenSpawn(command)
            index = child.expect([r'.*assword.*', r'Connection.*closed', pexpect.EOF, pexpect.TIMEOUT])

            if index == 0:
                # パスワードの入力
                child.sendline(password)

            elif index == 1:
                # Connection closedが表示された場合、最初からやり直し
                print("Connection closed detected. Restarting the process...")
                continue

            child.interact()  # コマンドが完了するまで対話を続ける

        except pexpect.exceptions.EOF:
            print("EOF received, restarting...")
            continue
        except pexpect.exceptions.TIMEOUT:
            print("Timeout, restarting...")
            continue

if __name__ == "__main__":
    execute_os_command()
