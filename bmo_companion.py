from IPython.display import Markdown, display
import time
import random

class BMO:
    def __init__(self):
        self.emotes = ["(◕‿◕✿)", "(◠‿◠✿)", "(⌒‿⌒)", "(✿◠‿◠)"]
        self.sounds = ["*beep boop*", "*happy whirr*", "*excited beeping*", "*screen glows*"]
    
    def say(self, message, delay=0.5):
        """Display BMO's message with characteristic style"""
        sound = random.choice(self.sounds)
        emote = random.choice(self.emotes)
        
        # Format the message with BMO's style
        bmo_message = f"""
{sound}

{message}

{emote}
"""
        # Add a small delay for effect
        time.sleep(delay)
        # Display using Markdown for better formatting
        display(Markdown(bmo_message))
    
    def ask(self, question, delay=0.5):
        """Ask a question and wait for input"""
        self.say(question, delay)
        return input("Your response: ")

# Usage example:
bmo = BMO()
# bmo.say("Hello friend! I'm BMO, your learning companion!")
# response = bmo.ask("What would you like to learn today?")