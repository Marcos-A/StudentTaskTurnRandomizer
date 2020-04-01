# StudentTaskTurnRandomizer
Random assignment of tasks and turns for students

To assign tasks and turns randomly, run from folder as:
    ```
    python StudentTaskRandomizer.py
    ```

Alternatively you can add 'task' or 'turn' when running to limit the assignment, e.g:

a) To assign only tasks, run:
    ```
    python StudentTaskRandomizer.py task
    ```

b) To define number of tasks, run (number 4 is just an example):
    ```
    python StudentTaskRandomizer.py task 4
    ```
    or
    ```
    python StudentTaskRandomizer.py 4 task
    ```

c) To assign only turns, run:
    ```
        python StudentTaskRandomizer.py turn
    ```

Number of options per task and students per turn ratio can be changed from the constants in the code itself.
Same for the list of students.
