from controller import ChatGPTAutomation
firefox_path = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
geckodriver_path = r"geckodriver.exe"

bot = ChatGPTAutomation(firefox_path, geckodriver_path)
bot.send_prompt_to_chatgpt("Hello, how are you?")
print(bot.return_last_response())
bot.quit()
