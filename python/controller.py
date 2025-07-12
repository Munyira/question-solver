from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import socket
import threading
import os
import json


class ChatGPTAutomation:

    def __init__(self, firefox_path, geckodriver_path):
        """
        Automates Firefox to interact with ChatGPT.
        :param firefox_path: path to firefox binary (e.g., C:\\Program Files\\Mozilla Firefox\\firefox.exe)
        :param geckodriver_path: path to geckodriver executable
        """
        self.firefox_path = firefox_path
        self.geckodriver_path = geckodriver_path

        self.url = "https://chatgpt.com"
        self.driver = self.setup_webdriver()

    def setup_webdriver(self):
        options = Options()
        options.binary_location = self.firefox_path
        # Uncomment below to run headless
        # options.add_argument("--headless")

        service = FirefoxService(executable_path=self.geckodriver_path)
        driver = webdriver.Firefox(service=service, options=options)
        driver.get(self.url)

        #print("Waiting for manual login or human verification...")
        #self.wait_for_human_verification()

        return driver

    def send_prompt_to_chatgpt(self, prompt):
        input_box = self.driver.find_element(by=By.XPATH, value='//textarea[contains(@placeholder, "Send a message")]')
        escaped_prompt = json.dumps(prompt)
        self.driver.execute_script(f"arguments[0].value = {escaped_prompt};", input_box)
        input_box.send_keys(Keys.RETURN)
        time.sleep(20)

    def wait_for_manual_check(self):
        while True:
            user_input = input("Press Enter once you’ve completed login or verification: ").strip()
            if user_input == "":
                break

    def wait_for_time_check(self):
        time.sleep(20)

    def return_chatgpt_conversation(self):
        return self.driver.find_elements(by=By.CSS_SELECTOR, value='div.text-base')

    def save_conversation(self, file_name):
        directory_name = "conversations"
        os.makedirs(directory_name, exist_ok=True)

        delimiter = "|^_^|"
        chatgpt_conversation = self.return_chatgpt_conversation()

        with open(os.path.join(directory_name, file_name), "a", encoding="utf-8") as file:
            for i in range(0, len(chatgpt_conversation), 2):
                file.write(
                    f"prompt: {chatgpt_conversation[i].text}\nresponse: {chatgpt_conversation[i + 1].text}\n\n{delimiter}\n\n"
                )

    def return_last_response(self):
        response_elements = self.driver.find_elements(by=By.CSS_SELECTOR, value='div.text-base')
        return response_elements[-1].text if response_elements else ""

    def wait_for_human_verification(self):
        print("You need to complete login or any required verification in the Firefox window.")
        while True:
            user_input = input("Enter 'y' when you're done: ").strip().lower()
            if user_input == "y":
                break

    def quit(self):
        print("Closing the browser...")
        self.driver.quit()
