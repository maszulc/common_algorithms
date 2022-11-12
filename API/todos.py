import requests


class TodosConfig:
    TODOS_URL = "https://jsonplaceholder.typicode.com/todos"
    DONE_STR = 'completed'
    USER_STR = 'userId'


def get_keys_with_top_values(dictionary):
    max_value = max(dictionary.values())
    return [key for key, value in dictionary.items() if value == max_value]


def count_tasks_api():
    try:
        response = requests.get(TodosConfig.TODOS_URL)
    except:
        print('Unable to fetch data from server')
        return None
    else:
        completed_tasks = {}  # userID: amountOfCompletedTasks
        for task in response.json():
            if task[TodosConfig.DONE_STR]:
                key = task[TodosConfig.USER_STR]
                completed_tasks[key] = completed_tasks.get(key, 0) + 1
        return get_keys_with_top_values(completed_tasks)


if __name__ == "__main__":
    print(count_tasks_api())
