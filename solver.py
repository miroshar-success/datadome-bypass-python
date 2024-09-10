import requests
import time

api_key = "CAI-CA8F5D78B888FEB049BE5444950CAA9F"  # your api key of capsolver

def capsolver():
    payload = {
        "clientKey": api_key,
        "task": {
            "type": 'DatadomeSliderTask',
            "websiteURL": "https://mygift.giftcardmall.com/",
            "captchaUrl": "https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMA1QGvUmJwyYoAwpyjNg%3D%3D&hash=789361B674144528D0B7EE76B35826&cid=6QAEcL8coBYTi9tYLmjCdyKmNNyHz1xwM2tMHHGVd_Rxr6FsWrb7H~a04csMptCPYfQ25CBDmaOZpdDa4qwAigFnsrzbCkVkoaBIXVAwHsjXJaKYXsTpkBPtqJfLMGN&t=fe&referer=https%3A%2F%2bck.websiteurl.com%2Fclient%2Fregister%2FYM4HJV%3Flang%3Den&s=40070&e=3e531bd3b30650f2e810ac72cd80adb5eaa68d2720e804314d122fa9e84ac25d",
            "proxy": "158.120.100.23:334:user:pass",
		    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        }
    }
    res = requests.post("https://api.capsolver.com/createTask", json=payload)
    resp = res.json()
    task_id = resp.get("taskId")
    if not task_id:
        print("Failed to create task:", res.text)
        return
    print(f"Got taskId: {task_id} / Getting result...")

    while True:
        time.sleep(1)  # delay
        payload = {"clientKey": api_key, "taskId": task_id}
        res = requests.post("https://api.capsolver.com/getTaskResult", json=payload)
        resp = res.json()
        status = resp.get("status")
        if status == "ready":
            return resp.get("solution", {}).get("cookie")
        if status == "failed" or resp.get("errorId"):
            print("Solve failed! response:", res.text)
            return

cookie = capsolver()
print(cookie)
