import openai
import readline
import asyncio
import colorama
import subprocess
import re
import logging

# Initialize colorama
colorama.init()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    print(colorama.Fore.GREEN + "Welcome to ZANA, your terminal-based chat assistant!" + colorama.Style.RESET_ALL)
    
    while True:
        try:
            user_input = input(colorama.Fore.CYAN + "You: " + colorama.Style.RESET_ALL)
            
            # Validate input to prevent command injection
            if not re.match(r'^[a-zA-Z0-9\s]+$', user_input):
                print(colorama.Fore.RED + "Invalid input. Please enter a valid command." + colorama.Style.RESET_ALL)
                continue
            
            # Process the input with OpenAI GPT-3.5 Turbo
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=150
            )
            
            command = response.choices[0].text.strip()
            
            # Execute the command
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(colorama.Fore.GREEN + result.stdout + colorama.Style.RESET_ALL)
            else:
                print(colorama.Fore.RED + result.stderr + colorama.Style.RESET_ALL)
        
        except (EOFError, KeyboardInterrupt):
            print(colorama.Fore.YELLOW + "\nGoodbye!" + colorama.Style.RESET_ALL)
            break

if __name__ == "__main__":
    asyncio.run(main())