from datetime import datetime, timedelta


class Period:
    def __init__(self, start_date, periodicity):
        if not isinstance(start_date, datetime):
            raise ValueError("start_date must be a datetime object")
        self.start_date = start_date
        self.periodicity = periodicity

    def is_within_period(self, date_to_check):
        """Check if a given date is within the period."""
        if not isinstance(date_to_check, datetime):
            raise ValueError("date_to_check must be a datetime object")

        if self.periodicity == "daily":
            return self.start_date <= date_to_check <= self.start_date + timedelta(days=1)
        elif self.periodicity == "weekly":
            return self.start_date <= date_to_check <= self.start_date + timedelta(weeks=1)
        elif self.periodicity == "monthly":
            next_month = self.start_date.replace(day=1) + timedelta(days=31)
            return self.start_date <= date_to_check <= next_month.replace(day=1)
        elif self.periodicity == "yearly":
            next_year = self.start_date.replace(month=1, day=1) + timedelta(days=365)
            return self.start_date <= date_to_check <= next_year.replace(month=1, day=1)
        else:
            raise ValueError("Invalid periodicity")

    @staticmethod
    def get_current_date():
        """Get the current date."""
        return datetime.now()


# Testing the implementation
if __name__ == "__main__":
    try:
        # Test the Period class
        today = Period.get_current_date()
        daily_period = Period(today, "daily")
        print(daily_period.is_within_period(today))  # Output: True
    except ValueError as e:
        print(f"An error occurred: {e}")
