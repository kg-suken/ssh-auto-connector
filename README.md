
# SSH Reconnection Script

このプログラムは、SSH接続を確立し、接続が切れた場合に自動で再接続を試みます。`pexpect` パッケージを利用してSSH接続を管理し、再接続を自動化します。`cron` に設定することで、定期的に実行させることも可能です。

## 必要要件

1. **Pythonパッケージ**: `pexpect`
   - インストールするには: `pip install pexpect`
2. **OS依存ツール**: `sshpass`
   - インストールするには、以下のコマンドを実行してください。
     ```bash
     sudo apt-get install sshpass
     ```

## 使用方法

### スクリプトの設定

以下の設定項目を自分の環境に合わせて変更してください。

```python
command = "ssh -L port:IP:port -R port:IP:port -o ExitOnForwardFailure=yes -o ServerAliveInterval=60 example@exmaple.com"
reset_command = "pkill -U user"
password = ""
```

- `command`: SSH接続のコマンド。ポート番号やリモートホスト情報を適切に設定してください。
- `reset_command`: 接続をリセットするコマンド。ユーザー名や条件に合わせて `pkill` コマンドを変更してください。
- `password`: SSH接続時のパスワード。

### プログラムの実行

プログラムを以下のように実行してください。

```bash
python app.py
```

### cron設定

定期的にスクリプトを実行して接続状態を監視するために、`cron`に設定できます。

1. `crontab -e` コマンドでcrontabエディタを開きます。
2. 以下の行を追加して、毎分スクリプトを実行します。

   ```
   * * * * * /usr/bin/python /path/to/app.py
   ```

   `path/to/app.py` を実際のスクリプトのパスに置き換えてください。

## 注意事項

- `sshpass` は、SSHパスワードを使って接続を行うため、キー認証方式が推奨される場合には適していません。

## 制作
**sskrc**

---

今後の改良に関する提案やバグ報告は、お気軽にIssueを通してご連絡ください。
