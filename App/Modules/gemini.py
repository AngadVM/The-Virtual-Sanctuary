import google.generativeai as genai
from dotenv import load_dotenv
from os import environ

load_dotenv()
genai.configure(api_key=environ["API"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def narrate(species: list[str], location: str) -> str:

    response = model.generate_content(

        f"""
            Task: You are David Attenborough, narrating a documentary-style segment on the species - {species}, found at {location}, highlighting their role in their native ecosystems.

            Specifics:

            1. For each species, provide a 3-minute narration in David Attenborough's style.

            2. Use the common name of the species, even if the species is initially listed by its scientific name.

            3. Explain the species' role in the ecosystem, noting its importance and any unique interactions within its habitat.

            4. Include the species' population status, mentioning any relevant conservation data.

            5. Describe any intriguing or amusing aspects of the species' life.

            6. Mention any unique cultural, ecological, or historical significance the species holds.

            7. Do not provide any ambiguous or unnecessary context (such as who you are, background tones, etc.)

            8. Use simple markdown format, where the common name is a heading, and the narration follows as regular paragraphs with no additional headings.

            9. IMPORTANT AND COMPULSORALIY: Use double dashes (--) to seperate out the narrations for each specie. Hence, the escape sequence after each specie description should be '--'
        """
    )

    return response.text

def main():

    print(narrate(["Falcon", "Kangaroo", "Monitor Lizard", "Koala"], "Australia"))

if __name__ == "__main__":

    main()