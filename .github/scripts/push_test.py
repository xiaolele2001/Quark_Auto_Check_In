"""发送一条测试推送，用于确认微信预览标题的渲染效果。"""

import json
import os
import urllib.parse
import urllib.request

key = os.environ["SENDKEY"]
title = "✅ 夸克签到 2/2 +40MB"
desp = "\n".join([
    "🙍🏻‍♂️ 第 1 个账号",
    "普通用户 夸父3539",
    "💾 网盘总容量：10.82 GB，签到累计容量：840.00 MB",
    "✅ 签到成功 +20.00 MB，连签进度（3/7）",
    "",
    "🙍🏻‍♂️ 第 2 个账号",
    "普通用户 Starry sky",
    "💾 网盘总容量：10.96 GB，签到累计容量：980.00 MB",
    "✅ 签到成功 +20.00 MB，连签进度（3/7）",
    "",
    "—— 测试推送，可忽略",
])
data = urllib.parse.urlencode({"title": title, "desp": desp}).encode()
req = urllib.request.Request(f"https://sctapi.ftqq.com/{key}.send", data=data)
with urllib.request.urlopen(req, timeout=20) as resp:
    payload = json.loads(resp.read().decode("utf-8"))
print("code:", payload.get("code"), payload.get("message"))
