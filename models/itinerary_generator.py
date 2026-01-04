from transformers import pipeline

generator = pipeline(
    task="text-generation",
    model="google/flan-t5-large"
)

def generate_itinerary(destination, days, budget, travel_type):
    prompt = f"""
    Create a detailed {days}-day travel itinerary for {destination}.
    Budget: {budget}
    Travel type: {travel_type}
    Include places to visit, food suggestions, and travel tips.
    """
    result = generator(prompt, max_length=500)
    return result[0]["generated_text"]
