import readline
import asyncio
import subprocess
import re
import openai
import logging
from colorama import Fore, Style

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# OpenAI API key configuration
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Regular expression for input validation
COMMAND_REGEX = re.compile(r'^[a-zA-Z0-9_\- ]+$')

async def get_gpt3_response(prompt):
    try:
        response = await openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        logging.error(f"Error fetching GPT-3 response: {e}")
        return "Sorry, I couldn't process that request."

async def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Command execution failed: {e}")
        return e.stderr

async def handle_input(user_input):
    if not COMMAND_REGEX.match(user_input):
        return f"{Fore.RED}Invalid input. Only alphanumeric characters, hyphens, and underscores are allowed.{Style.RESET_ALL}"

    gpt3_response = await get_gpt3_response(user_input)
    logging.info(f"GPT-3 response: {gpt3_response}")

    if gpt3_response.lower().startswith("execute"):
        command = gpt3_response[len("execute"):].strip()
        logging.info(f"Executing command: {command}")
        execution_result = await execute_command(command)
        return execution_result
    else:
        return gpt3_response

async def main():
    print(f"{Fore.GREEN}Welcome to ZANA! Type your commands below:{Style.RESET_ALL}")
    while True:
        user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}")
        response = await handle_input(user_input)
        print(f"{Fore.YELLOW}ZANA: {response}{Style.RESET_ALL}")

if __name__ == "__main__":
    asyncio.run(main())