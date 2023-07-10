class StackLimitException(Exception):
    """Stack is empty."""
    pass


class DequeTopLimitException(Exception):
    """Get deque upper limit"""
    pass


class DequeLowLimitException(Exception):
    """get deque low limit"""
