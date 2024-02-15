from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, periodicity, duration):
        self.name = name
        self.periodicity = periodicity
        self.duration = duration
        self.completions = []  # List to store completion dates

    def mark_complete(self, completion_date=None):
        """Mark the habit as complete on the given date or current date if not provided."""
        if completion_date is None:
            completion_date = datetime.now().date()
        self.completions.append(completion_date)

    def longest_streak(self):
        """Calculate the longest streak for the habit."""
        if not self.completions:
            return 0

        self.completions.sort()  # Sort completions chronologically
        current_streak = 1
        longest_streak = 1
        prev_completion_date = self.completions[0]

        for completion_date in self.completions[1:]:
            if completion_date - prev_completion_date == timedelta(days=1):
                current_streak += 1
            else:
                current_streak = 1
            if current_streak > longest_streak:
                longest_streak = current_streak
            prev_completion_date = completion_date

        return longest_streak

    def get_longest_streak(self):
        """Calculate the longest streak for the habit."""
        if not self.completions:
            return 0

        self.completions.sort()  # Sort completions chronologically
        current_streak = 1
        longest_streak = 1
        prev_completion_date = self.completions[0]

        for completion_date in self.completions[1:]:
            if completion_date - prev_completion_date == timedelta(days=1):
                current_streak += 1
            else:
                current_streak = 1
            if current_streak > longest_streak:
                longest_streak = current_streak
            prev_completion_date = completion_date

        return longest_streak

class Challenge:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.participation_dates = []  # List to store participation dates

    def participate(self, participation_date=None):
        """Mark participation in the challenge on the given date or current date if not provided."""
        if participation_date is None:
            participation_date = datetime.now().date()
        self.participation_dates.append(participation_date)

    def longest_streak(self):
        """Calculate the longest streak for the challenge."""
        if not self.participation_dates:
            return 0

        self.participation_dates.sort()  # Sort participation dates chronologically
        current_streak = 1
        longest_streak = 1
        prev_participation_date = self.participation_dates[0]

        for participation_date in self.participation_dates[1:]:
            if participation_date - prev_participation_date == timedelta(days=1):
                current_streak += 1
            else:
                current_streak = 1
            if current_streak > longest_streak:
                longest_streak = current_streak
            prev_participation_date = participation_date

        return longest_streak

class User:
    def __init__(self, username):
        self.username = username
        self.habits = []  # List to store user's habits
        self.challenges = []  # List to store user's challenges

    def create_habit(self, name, periodicity, duration):
        """Create a new habit."""
        habit = Habit(name, periodicity, duration)
        self.habits.append(habit)

    def create_challenge(self, name, duration):
        """Create a new challenge."""
        challenge = Challenge(name, duration)
        self.challenges.append(challenge)

    def mark_habit_complete(self, habit_name, completion_date=None):
        """Mark a habit as complete."""
        habit = self.find_habit(habit_name)
        if habit:
            habit.mark_complete(completion_date)
        else:
            print("Habit not found.")

    def participate_in_challenge(self, challenge_name, participation_date=None):
        """Participate in a challenge."""
        challenge = self.find_challenge(challenge_name)
        if challenge:
            challenge.participate(participation_date)
        else:
            print("Challenge not found.")

    def find_habit(self, habit_name):
        """Find a habit by name."""
        for habit in self.habits:
            if habit.name == habit_name:
                return habit
        return None

    def find_challenge(self, challenge_name):
        """Find a challenge by name."""
        for challenge in self.challenges:
            if challenge.name == challenge_name:
                return challenge
        return None

    def get_all_habits(self):
        """Get a list of all user's habits."""
        return [habit.name for habit in self.habits]

    def get_habits_by_periodicity(self, periodicity):
        """Get a list of habits with a specific periodicity."""
        return [habit for habit in self.habits if habit.periodicity == periodicity]

# Testing the implementation
if __name__ == "__main__":
    user = User("test_user")
    user.create_habit("Working out", "daily", 30)
    user.create_habit("Taking water", "daily", 30)
    user.create_challenge("30-Day Challenge", 30)

    user.mark_habit_complete("Working out", datetime(2024, 1, 1))
    user.participate_in_challenge("30-Day Challenge", datetime(2024, 1, 1))
    print(user.get_all_habits())


