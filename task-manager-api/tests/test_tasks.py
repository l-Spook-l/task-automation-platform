import pytest
from pydantic import ValidationError

from src.tasks.service import TaskService
from src.tasks.schemas import TaskCreate, TaskUpdate


@pytest.fixture
def service():
    return TaskService()


def test_create_task(service):
    task = service.create_task(TaskCreate(
        title="Test",
        description="Description",
        completed=False
    ))

    assert task.id == 1
    assert task.title == "Test"
    assert len(service.tasks) == 1


def test_create_error(service):
    with pytest.raises(ValidationError) as exc:
        TaskCreate(
            title="Test",
            description="Short",
            completed=False
        )

    errors = exc.value.errors()

    assert errors[0]["type"] == "string_too_short"


def test_get_tasks(service):
    service.create_task(TaskCreate(
        title="Task1",
        description="Description",
        completed=False
    ))

    tasks = service.get_tasks()

    assert len(tasks) == 1
    assert tasks[0].title == "Task1"


def test_update_task(service):
    service.create_task(TaskCreate(
        title="Old",
        description="Description",
        completed=False
    ))

    updated = service.update_task(1, TaskUpdate(title="New"))

    assert updated is not None
    assert updated.title == "New"


def test_update_task_not_found(service):
    result = service.update_task(999, TaskUpdate(title="New"))

    assert result is None


def test_delete_task(service):
    service.create_task(TaskCreate(
        title="To delete",
        description="Description",
        completed=False
    ))

    deleted = service.delete_task(1)

    assert deleted is not None
    assert len(service.tasks) == 0


def test_delete_task_not_found(service):
    result = service.delete_task(999)

    assert result is None
