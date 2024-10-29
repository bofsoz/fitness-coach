import random

# Sample exercise database
exercises = {
    'strength': ['Push-ups', 'Squats', 'Lunges', 'Deadlifts', 'Bench Press'],
    'cardio': ['Running', 'Cycling', 'Jump Rope', 'Burpees', 'High Knees'],
    'flexibility': ['Yoga', 'Stretching', 'Pilates']
}

def generate_workout_plan(goal, fitness_level):
    workout_plan = []
    
    if goal == 'muscle gain':
        workout_plan += random.sample(exercises['strength'], 3)
    elif goal == 'weight loss':
        workout_plan += random.sample(exercises['cardio'], 3)
    elif goal == 'endurance':
        workout_plan += random.sample(exercises['cardio'], 2) + random.sample(exercises['strength'], 1)
    
    # Adjust plan based on fitness level
    if fitness_level == 'beginner':
        workout_plan = [exercise + ' (3 sets of 10 reps)' for exercise in workout_plan]
    elif fitness_level == 'intermediate':
        workout_plan = [exercise + ' (4 sets of 12 reps)' for exercise in workout_plan]
    else:  # advanced
        workout_plan = [exercise + ' (5 sets of 15 reps)' for exercise in workout_plan]
    
    return workout_plan

# Example usage
user_goal = 'muscle gain'
user_fitness_level = 'beginner'
workout_plan = generate_workout_plan(user_goal, user_fitness_level)
print("Your personalized workout plan:", workout_plan)
