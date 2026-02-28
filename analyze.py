error_count = 0
warn_count = 0
by_device = {}
hour_count = {}

with open("log.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.split()

        if "ERROR" in line:
            error_count += 1

            # parts の長さを確認してからアクセス
            if len(parts) > 3:
                device = parts[3]
                by_device[device] = by_device.get(device, 0) + 1

            if len(parts) > 1:
                hour = parts[1].split(":")[0]
                hour_count[hour] = hour_count.get(hour, 0) + 1

        if "WARNING" in line:
            warn_count += 1

print("エラー総数:", error_count)
print("警告総数:", warn_count)

print("\nデバイス別エラー")
for d, c in by_device.items():
    print(d, c, "回")

if by_device:
    worst = max(by_device, key=by_device.get)
    print("\n一番エラー多い:", worst, by_device[worst], "回")

print("\n時間帯別エラー")
for h, c in sorted(hour_count.items()):  # 時間順にソート
    print(h, "時:", c, "回")