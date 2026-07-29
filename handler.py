from typing import Any

def process_event(event: dict[str, Any]) -> None:
    """Process an incoming event."""
    event_type = event.get('type')
    if event_type:
        handle_event(event_type, event)


def handle_event(event_type: str, event: dict[str, Any]) -> None:
    """Handle a specific event type."""
    if event_type == 'USER_LOGIN':
        user_login(event)
    elif event_type == 'USER_LOGOUT':
        user_logout(event)
    else:
        print(f'Unknown event type: {event_type}')


def user_login(event: dict[str, Any]) -> None:
    """Handle user login events."""
    user_id = event.get('user_id')
    print(f'User {user_id} has logged in.')


def user_logout(event: dict[str, Any]) -> None:
    """Handle user logout events."""
    user_id = event.get('user_id')
    print(f'User {user_id} has logged out.')
