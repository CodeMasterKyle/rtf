import requests
import time

def update_file():
    url = "https://api-online.readytofight.ru/rtfall"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        total_value = data.get("total")
        
        with open("online.txt", "w") as file:
            file.write(str(total_value))
        print(f"Updated online.txt with value: {total_value}")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == "__main__":
    while True:
        update_file()
        time.sleep(600)  # 10 минут
