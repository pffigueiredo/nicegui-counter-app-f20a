from nicegui.testing import User
from nicegui import ui
import pytest


async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    await user.should_see('0')
    await user.should_see('Simple Counter')


async def test_counter_increment(user: User) -> None:
    """Test incrementing the counter"""
    await user.open('/')
    
    # Click the increment button using marker
    user.find(marker='increment-btn').click()
    await user.should_see('1')


async def test_counter_decrement(user: User) -> None:
    """Test decrementing the counter"""
    await user.open('/')
    
    # Increment first to have a positive number
    user.find(marker='increment-btn').click()
    await user.should_see('1')
    
    # Then decrement
    user.find(marker='decrement-btn').click()
    await user.should_see('0')


async def test_counter_multiple_operations(user: User) -> None:
    """Test multiple increment and decrement operations"""
    await user.open('/')
    
    # Increment 3 times
    for _ in range(3):
        user.find(marker='increment-btn').click()
    await user.should_see('3')
    
    # Decrement 2 times
    for _ in range(2):
        user.find(marker='decrement-btn').click()
    await user.should_see('1')


async def test_counter_negative_values(user: User) -> None:
    """Test that counter can go negative"""
    await user.open('/')
    
    # Decrement to go negative
    user.find(marker='decrement-btn').click()
    await user.should_see('-1')
    
    # Decrement again
    user.find(marker='decrement-btn').click()
    await user.should_see('-2')


async def test_counter_ui_elements(user: User) -> None:
    """Test that all UI elements are present"""
    await user.open('/')
    
    # Check for title
    await user.should_see('Simple Counter')
    
    # Check for buttons using markers
    await user.should_see(marker='increment-btn')
    await user.should_see(marker='decrement-btn')
    await user.should_see(marker='counter-display')
    
    # Check for counter display (should start at 0)
    await user.should_see('0')


async def test_counter_display_updates(user: User) -> None:
    """Test that the counter display updates correctly"""
    await user.open('/')
    
    # Verify initial display
    await user.should_see('0')
    
    # Increment and check
    user.find(marker='increment-btn').click()
    await user.should_see('1')
    
    # Decrement twice and check
    user.find(marker='decrement-btn').click()
    user.find(marker='decrement-btn').click()
    await user.should_see('-1')