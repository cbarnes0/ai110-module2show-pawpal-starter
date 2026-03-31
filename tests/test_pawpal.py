import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import Task, Pet


def make_task(name="Morning Walk"):
    return Task(
        name=name,
        task_type="walk",
        duration_minutes=30,
        priority="high",
        recurrence="daily",
        time_of_day="morning"
    )


def test_task_completion_and_clear():
    task = make_task()

    assert task.completed is False, "Task should start incomplete"

    task.mark_complete()
    assert task.completed is True, "Task should be complete after mark_complete()"

    task.clear_completion()
    assert task.completed is False, "Task should be incomplete after clear_completion()"


def test_add_task_to_pet():
    pet = Pet(name="Buddy", species="Dog")
    task = make_task()

    assert len(pet.get_tasks()) == 0, "Pet should start with no tasks"

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1, "Pet should have one task after add_task()"
    assert pet.get_tasks()[0] is task, "The added task should be retrievable"
    assert task.pet_name == "Buddy", "Task should have pet_name set after being added"
