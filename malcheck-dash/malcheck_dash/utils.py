import requests
from datetime import datetime
from malcheck_dash.logging import logger
from malcheck_dash.config import BOT_TOKEN, CHAT_ID


def dash_send_telegram(text):
    try:
        token = BOT_TOKEN
        chat_id = CHAT_ID
        tm_now = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        text = f"{tm_now}, MalCheck, {text}"
        api_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text=`{text}`"
        response = requests.get(api_url)
    except Exception as ex:
        logger.warning(str(ex))
    else:
        return response.json()
