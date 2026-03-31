# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

We want to start with the most important things. The main things is making sure your pet is getting walked, fed, and taking any medicine they need. They need to be able to schedule all of these. Obviously they will also need to be able to add their pets and ad these tasks per pet. They need to be able to see the tasks for the day in a simple format. 

We ended up making classes for Task, Owner, Pet, and DailyPlan. This will allow for all of the basic things I identified as necessary for an MVP.
Task is simply a class for the things associated for the task you must do with your pet. Owner is a profile of sorts that we created to assign pets to and then assign tasks via the pet. DailyPlan allows for a view of all of the tasks, kind of like a dashboard. 

**b. Design changes**

- Did your design change during implementation?

Summary of suggested additions:

Where:	     What to add:
Task	    pet: Pet back-reference (or pet_name: str)
Task	    due_days: list[str] for weekly recurrence
DailyPlan	tie-breaking rule doc/comment on generate()
DailyPlan	consider total_duration_minutes as @property

- If yes, describe at least one change and why you made it.

Yes. In the initial UML, `Task` had no reference to the pet it belonged to. During review we realized that when `DailyPlan.generate()` collects tasks from all pets and flattens them into a single list, the pet context is lost — you could no longer display something like "Walk Buddy." We added a `pet_name` attribute to `Task` that gets set automatically when a task is added to a `Pet`, so the plan can display each task with its pet's name without needing to trace back through the object graph.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
