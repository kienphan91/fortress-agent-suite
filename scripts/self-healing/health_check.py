import os, subprocess, pathlib, urllib.parse

def send_telegram(msg):
    cfg_path = pathlib.Path('/root/.openclaw/telegram_config')
    if not cfg_path.exists(): return
    cfg = {}
    for line in cfg_path.read_text().splitlines():
        if '=' in line:
            k,v = line.split('=',1)
            cfg[k.strip()] = v.strip()
    token, chat_id = cfg.get('BOT_TOKEN'), cfg.get('CHAT_ID')
    if token and chat_id:
        os.system(f"curl -s 'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={urllib.parse.quote_plus(msg)}' > /dev/null")

def check():
    try:
        subprocess.check_call(['openclaw', 'gateway', 'status'], timeout=5)
    except:
        msg = "Meo meo! Hệ thống Gateway bị down. Đào đang tự động restore và restart!"
        send_telegram(msg)
        import restore
        restore.run_restore()
        send_telegram("Hệ thống đã phục hồi thành công.")

if __name__ == "__main__": check()
