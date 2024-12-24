# bmo_companion.py
from IPython.display import Markdown, display
import time
import random
from datetime import datetime
import json
import os

class BMO:
    def __init__(self):
        self.emotes = ["(◕‿◕✿)", "(◠‿◠✿)", "(⌒‿⌒)", "(✿◠‿◠)"]
        self.sounds = ["*beep boop*", "*happy whirr*", "*excited beeping*", "*screen glows*"]
    
    def say(self, message, delay=0.5):
        """Display BMO's message with characteristic style"""
        sound = random.choice(self.sounds)
        emote = random.choice(self.emotes)
        bmo_message = f"\n{sound}\n\n{message}\n\n{emote}"
        time.sleep(delay)
        display(Markdown(bmo_message))
    
    def ask(self, question, delay=0.5):
        """Ask a question and wait for input"""
        self.say(question, delay)
        return input("Your response: ")

class LearningJourneyGenerator:
    def __init__(self, bmo):
        self.bmo = bmo
        self.user_info = {}
        self.learning_info = {}
        
    def gather_all_info(self):
        """Run through all information gathering steps"""
        self.gather_user_info()
        self.analyze_learning_preferences()
        
    def gather_user_info(self):
        self.user_info = {
            "name": self.bmo.ask("First things first - what's your name? We're going to be great friends!"),
            "topic": self.bmo.ask("What would you like to learn about?"),
            "time_commitment": self.bmo.ask("How many hours per week can you dedicate to learning?"),
            "experience": self.bmo.ask(f"How familiar are you with {self.user_info.get('topic', 'this topic')}? (beginner/intermediate/advanced):")
        }
    
    def analyze_learning_preferences(self):
        self.learning_info = {
            "style": self.bmo.ask("How do you prefer to learn? (e.g., hands-on practice, reading, videos, mix):"),
            "pace": self.bmo.ask("What learning pace works best for you? (structured, self-paced, mixed):"),
            "project_size": self.bmo.ask("Do you prefer many small projects or one big project?")
        }
        
    def generate_files(self, output_dir="outputs"):
        """Generate both prompt and profile files"""
        os.makedirs(output_dir, exist_ok=True)
        prompt_file = self.generate_prompt_file(output_dir)
        profile_json = self.save_profile_json(output_dir)
        return prompt_file, profile_json
    
    def generate_prompt_file(self, output_dir):
        """Generate a markdown file with the prompt"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/prompt_{timestamp}.md"
        
        template = f"""# Learning Journey Prompt

Hi Claude! I'm {self.user_info['name']} and I'd like to create a gamified learning journey. Here's my context:

<learning_profile>
* Learning topic: {self.user_info['topic']}
* Current level: {self.user_info['experience']}
* Time available: {self.user_info['time_commitment']} hours per week
* Learning style: {self.learning_info['style']}
* Preferred pace: {self.learning_info['pace']}
* Project preference: {self.learning_info['project_size']}
</learning_profile>

Could you help me design a progressive learning path using game mechanics like levels, skills, and boss battles?

<skill_tree_template>
# [Learning Topic] journey
Username: , date: 
objective:
## Level 1: The base camp 🏕️
### Core skills
* [ ] Skill 1
* [ ] Skill 2
* [ ] Skill 3

### Bonus skills
* [ ] Bonus 1
* [ ] Bonus 2

### 🗡️ **BOSS BATTLE: [Topic relevant Title to earn]**
* Victory conditions: [Define success criteria]
* Bonus points: [Extra challenges]
* Ultimate challenge: [Advanced goal]

## Level 2: [Next Stage] ⚔️
[Continue the pattern...]
</skill_tree_template>

<areas_to_explore>
Consider discussing:
1. Required tools or materials
2. Recommended learning resources
3. Practice exercises or projects
4. Ways to measure progress
5. Community resources or mentorship
</areas_to_explore>
"""
        with open(filename, 'w') as f:
            f.write(template)
            
        return filename
    
    def save_profile_json(self, output_dir):
        """Save the complete profile as JSON"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/profile_{timestamp}.json"
        
        profile_data = {
            "user_info": self.user_info,
            "learning_info": self.learning_info,
            "created_at": datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(profile_data, f, indent=2)
            
        return filename
