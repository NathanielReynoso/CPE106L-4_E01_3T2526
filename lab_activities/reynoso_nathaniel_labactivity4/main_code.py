# -------------------------------------------
# Steam Wishlist System
# By: Reynoso, Nathaniel Joseph C.
# -------------------------------------------

import unittest

# Class 1 (Wishlist)
class WishlistGames:
    def update(self, game_name: str, message: str):
        raise NotImplementedError("Subclasses should use the update() method.")

# Class 2 (Users) WishlistGames extends
class SteamUser(WishlistGames):
    def __init__(self, username: str):
        self.username = username
        self.notification_inbox = [] 
        
    def update(self, game_name: str, message: str):
        notification = f"[{self.username}'s Inbox] Update for {game_name}: {message}"
        self.notification_inbox.append(notification)
        print(notification)

# Class 3 (Steam Games)
class SteamGame:
    def __init__(self, title: str, status: str, price: float):
        self.title = title
        self.status = status
        self.price = float(price)
        self._subscribers = [] 

    def __str__(self):
        return f"Game: {self.title:<18} | Status: {self.status:<26} | Price: ₱{self.price:.2f}"

    def add_subscriber(self, user: WishlistGames):
        if user not in self._subscribers:
            self._subscribers.append(user)

    def remove_subscriber(self, user: WishlistGames):
        if user in self._subscribers:
            self._subscribers.remove(user)

    def _notify_all(self, message: str):
        for subscriber in self._subscribers:
            subscriber.update(self.title, message)

    def update_status(self, new_status: str):
        self.status = new_status
        self._notify_all(f"Status changed to '{self.status}'.")

    def apply_discount(self, new_price: float):
        self.price = float(new_price)
        self._notify_all(f"Price dropped to ₱{self.price:.2f}!")

# Class 4 (Testing Steam Wishlist)
class TestSteamWishlist(unittest.TestCase):

    def setUp(self):
        self.pragmata = SteamGame("Pragmata", "April 17, 2026", 2999.00)
        self.gta6 = SteamGame("GTA 6", "Fall 2025", 3499.00)
        self.sts2 = SteamGame("Slay the Spire 2", "March 6, 2026", 1200.00)
        
        self.user1 = SteamUser("Warfreak999")
        self.user2 = SteamUser("CapcomFan")
        self.user3 = SteamUser("NeuroSama")
        
        self.pragmata.add_subscriber(self.user1)
        self.pragmata.add_subscriber(self.user2)
        self.gta6.add_subscriber(self.user1)
        self.sts2.add_subscriber(self.user3)

    def test_1_sts2_launch_day(self):
        print("\n[TEST 1] Testing Slay the Spire 2 Launch (March 6)...")
        self.sts2.update_status("Available Now - Launched March 6, 2026!")
        expected_msg = "Update for Slay the Spire 2: Status changed to 'Available Now - Launched March 6, 2026!'."
        self.assertIn(expected_msg, self.user3.notification_inbox[0])
        print(">> Result: PASSED (STS2 Launch broadcasted successfully)")

    def test_2_pragmata_launch_day(self):
        print("\n[TEST 2] Testing Pragmata Launch (April 17)...")
        self.pragmata.update_status("Available Now - Launched April 17, 2026!")
        expected_msg = "Update for Pragmata: Status changed to 'Available Now - Launched April 17, 2026!'."
        self.assertIn(expected_msg, self.user1.notification_inbox[0])
        self.assertIn(expected_msg, self.user2.notification_inbox[0])
        print(">> Result: PASSED (Pragmata Launch broadcasted successfully)")

    def test_3_display_game_information(self):
        print("\n[TEST 3] Testing Game Information Display...")
        actual_display = str(self.pragmata)
        expected_display = "Game: Pragmata           | Status: April 17, 2026             | Price: ₱2999.00"
        print(f"Data Extracted: {actual_display}")
        self.assertEqual(actual_display, expected_display)
        print(">> Result: PASSED (Game information formatted correctly)")

    def test_4_price_drop_notification(self):
        print("\n[TEST 4] Testing Pragmata Sale Notification...")
        self.pragmata.apply_discount(1499.50)
        expected_msg = "Update for Pragmata: Price dropped to ₱1499.50!"
        self.assertIn(expected_msg, self.user1.notification_inbox[0])
        print(">> Result: PASSED (All subscribers notified of price drop)")

    def test_5_unsubscribe_logic(self):
        print("\n[TEST 5] Testing Unsubscribe Logic...")
        self.pragmata.remove_subscriber(self.user1)
        self.pragmata.update_status("Post-Launch Patch 1.1 Released")
        self.assertEqual(len(self.user2.notification_inbox), 1)
        self.assertEqual(len(self.user1.notification_inbox), 0)
        print(">> Result: PASSED (Removed subscribers do not receive updates)")

    def test_6_gta6_delay_notification(self):
        print("\n[TEST 6] Testing GTA 6 Inevitable Delay...")
        self.gta6.update_status("Delayed to Spring 2026")
        expected_msg = "Update for GTA 6: Status changed to 'Delayed to Spring 2026'."
        self.assertIn(expected_msg, self.user1.notification_inbox[0])
        self.assertEqual(len(self.user2.notification_inbox), 0)
        print(">> Result: PASSED (Only subscribed users suffer the delay)")

if __name__ == '__main__':
    print("-" * 65)
    print("RUNNING AUTOMATED TESTS FOR LAB 4: STEAM WISHLIST")
    print("-" * 65)
    unittest.main(verbosity=2)
