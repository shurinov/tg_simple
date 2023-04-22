import requests


class TgMsg():
    
    def __init__(self, api_token:str, chat_id:str=None) -> None:
        self.api_token = api_token
        self.default_chat_id = chat_id
        pass
    
    
    def send_text(self, text:str, chat_id:str=None, html:bool=False) -> bool:
        url = f"https://api.telegram.org/bot{self.api_token}/sendMessage"
        if chat_id == None:
            chat_id = self.default_chat_id
        data = {
            'chat_id' : chat_id,
            'text': text
        }
        if html:
            data['parse_mode'] = 'HTML'
        x = requests.post(url, data)
        # 
        if x.json().get("ok") == True:
            return True
        else:
            return False

