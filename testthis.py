from handler.chatgpt_selenium_automation import ChatGPTAutomation

# Define the path where the chrome driver is installed on your computer
# Typically, if you've installed it globally, it might be accessible without the full path. 
# Otherwise, specify the full path to your chromedriver (e.g., "/Users/your_username/path_to_chromedriver/chromedriver")
chrome_path = "C:/Users/Munyira/MyDrive/Documents/projects/head/chrome/chrome.exe"
chrome_driver_path = "C:/Users/Munyira/MyDrive/Documents/projects/head/drivers/chromedriver.exe"

# Create an instance
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

# Define a prompt and send it to chatgpt
prompt = "What are the benefits of exercise?"
chatgpt.send_prompt_to_chatgpt(prompt)

# Retrieve the last response from ChatGPT
response = chatgpt.return_last_response()
print(response)

# Save the conversation to a text file
file_name = "conversation.txt"
chatgpt.save_conversation(file_name)

# Close the browser and terminate the WebDriver session
chatgpt.quit()