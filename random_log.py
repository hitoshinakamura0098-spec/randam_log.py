import random
from datetime import datetime, timedelta

# デバイス候補
devices = ["sensorA", "sensorB", "motorX", "camera1", "server01"]

# ステータス
levels = ["INFO", "INFO", "INFO", "WARNING", "ERROR"]  # INFO多め

start = datetime(2026, 2, 28, 0, 0, 0)

with open("log.txt", "w", encoding="utf-8") as f:
    current = start

    for i in range(500):  # 500行生成
        # 時間をランダムに進める
        current += timedelta(seconds=random.randint(10, 300))

        level = random.choice(levels)
        device = random.choice(devices)

        if level == "ERROR":
            msg = "failed"
        elif level == "WARNING":
            msg = "slow response"
        else:
            msg = "ok"

        line = f"{current.strftime('%Y-%m-%d %H:%M:%S')} {level} {device} {msg}\n"
        f.write(line)

print("log.txt 作成完了")