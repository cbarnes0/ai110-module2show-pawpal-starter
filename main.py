from pawpal_system import Owner, Pet, Task, DailyPlan

# Create owner
alex = Owner(name="Alex", available_hours_per_day=2.0)

# Create pets
buddy = Pet(name="Buddy", species="Dog")
whiskers = Pet(name="Whiskers", species="Cat")

# Add tasks to Buddy
buddy.add_task(Task("Morning Walk",  task_type="walk",        duration_minutes=30, priority="high",   recurrence="daily",  time_of_day="morning"))
buddy.add_task(Task("Breakfast",     task_type="feeding",     duration_minutes=10, priority="high",   recurrence="daily",  time_of_day="morning"))
buddy.add_task(Task("Flea Medicine", task_type="medication",  duration_minutes=5,  priority="medium", recurrence="weekly", time_of_day="evening", due_days=["Monday", "Thursday"]))
buddy.add_task(Task("Fetch / Play",  task_type="enrichment",  duration_minutes=20, priority="low",    recurrence="daily",  time_of_day="afternoon"))

# Add tasks to Whiskers
whiskers.add_task(Task("Breakfast",  task_type="feeding",     duration_minutes=5,  priority="high",   recurrence="daily",  time_of_day="morning"))
whiskers.add_task(Task("Brushing",   task_type="grooming",    duration_minutes=15, priority="medium", recurrence="weekly", time_of_day="afternoon", due_days=["Wednesday", "Saturday"]))
whiskers.add_task(Task("Laser Toy",  task_type="enrichment",  duration_minutes=10, priority="low",    recurrence="daily",  time_of_day="evening"))

# Register pets with owner
alex.add_pet(buddy)
alex.add_pet(whiskers)

# Generate and display today's plan
plan = DailyPlan(owner=alex)
plan.generate()
print(plan.display())
