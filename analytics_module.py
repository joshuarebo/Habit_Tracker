from datetime import datetime  # Import the datetime module

class AnalyticsModule:
    def analyze_habits(self, user):
        """Analyze habits for a specific user."""
        try:
            all_habits = [habit.name for habit in user.habits]
            habits_by_periodicity = {}
            for periodicity in ["daily", "weekly", "monthly"]:
                habits_by_periodicity[periodicity] = [habit.name for habit in user.get_habits_by_periodicity(periodicity)]
            longest_streak = self.get_longest_streak(user)
            return {
                "all_habits": all_habits,
                "habits_by_periodicity": habits_by_periodicity,
                "longest_streak": longest_streak
            }
        except Exception as e:
            return f"Error analyzing habits: {e}"


    def get_longest_streak(self, user):
        """Get the longest streak of all defined habits."""
        try:
            longest_streak = 0
            for habit in user.habits:
                streak = habit.get_longest_streak()
                if streak > longest_streak:
                    longest_streak = streak
            return longest_streak
        except Exception as e:
            return f"Error calculating longest streak: {e}"


if __name__ == "__main__":
    from user import User

    # Create a user and add some habits
    user = User("test_user")
    user.create_habit("Exercise", "daily", 30)
    user.create_habit("Read", "weekly", 4)
    user.create_habit("Meditate", "daily", 30)

    # Mark habits as complete for testing longest streak calculation
    user.mark_habit_complete("Exercise", datetime(2024, 1, 1))  # Marking Exercise habit as complete on January 1, 2024
    user.mark_habit_complete("Exercise", datetime(2024, 1, 2))  # Marking Exercise habit as complete on January 2, 2024
    user.mark_habit_complete("Exercise", datetime(2024, 1, 3))  # Marking Exercise habit as complete on January 3, 2024

    user.mark_habit_complete("Read", datetime(2024, 1, 5))  # Marking Read habit as complete on January 5, 2024
    user.mark_habit_complete("Read", datetime(2024, 1, 12))  # Marking Read habit as complete on January 12, 2024

    user.mark_habit_complete("Meditate", datetime(2024, 1, 1))  # Marking Meditate habit as complete on January 1, 2024
    user.mark_habit_complete("Meditate", datetime(2024, 1, 2))  # Marking Meditate habit as complete on January 2, 2024
    user.mark_habit_complete("Meditate", datetime(2024, 1, 3))  # Marking Meditate habit as complete on January 3, 2024



    # Analyze habits
    analytics_module = AnalyticsModule()
    analysis_result = analytics_module.analyze_habits(user)
    print("Analysis Result:")
    print(analysis_result)
