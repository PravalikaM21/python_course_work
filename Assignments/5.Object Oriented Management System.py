"""
Assignment 5: Simple OOP Management System - Hotstar (Jio Hotstar)

Goal (easy version):
Create a tiny but complete OTT (streaming) management system using OOP. It follows the
University example idea: a base class, subclasses, supporting classes, and one controller
(HotstarApp) + a simple Command-Line Interface (CLI).

What this file contains (quick checklist):
1) Brief description (this block)
2) Class list with short notes (below)
3) Clean, readable Python code (single file)
4) Sample CLI run (at the bottom, as a comment)
5) Helpful comments near important OOP parts

How OOP is applied here (in simple words):
- Encapsulation: Private-ish fields (with _) + properties to read values safely.
- Abstraction: An abstract Content class defines a common interface for all content.
- Inheritance: Movie and Series inherit from Content; Viewer/Admin inherit from User.
- Polymorphism: display_info() and duration() work differently for Movie vs Series.
- Class vs Instance attributes: plan registry and total revenue are class-level; titles, names, etc.
  are instance-level.
- Class/Static methods: SubscriptionPlan.create_default_plans() (class); Money.cents_to_rupees()
  (static).

-------------------------------------
Class List (short and clear)
-------------------------------------
Base classes
- User: id, name, email/phone (private), role, watchlist, history
- Content (abstract): id, title, genre; common interface: display_info(), duration()

Subclasses
- Viewer(User): normal user
- Admin(User): can add content
- Movie(Content): has runtime_minutes
- Series(Content): has list of Episode

Supporting
- Episode: title, minutes
- SubscriptionPlan: name, monthly_price_cents (class registry of plans)
- Subscription: user_id, plan_name, is_active
- Money: helper for cents↔rupees (static methods)

Controller/Manager
- HotstarApp: keeps all users, content, subscriptions; handles register, add content,
  subscribe, play, reports, totals.

CLI Features (simple):
- Register viewer
- Add movie/series (admin only)
- Subscribe viewer to a plan
- Play content (checks subscription)
- Show reports: total revenue, top content by views, list users & content

"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional

# -----------------------------
# Helper: Money (static methods)
# -----------------------------
class Money:
    @staticmethod
    def cents_to_rupees(cents: int) -> float:
        return round(cents / 100.0, 2)

    @staticmethod
    def rupees_to_cents(rs: float) -> int:
        return int(round(rs * 100))

# -----------------------------
# Abstract Content + Subclasses
# -----------------------------
class Content(ABC):
    _next_id = 1  # class attribute to auto assign ids

    def __init__(self, title: str, genre: str):
        self._id = Content._next_id
        Content._next_id += 1
        self._title = title
        self._genre = genre
        self._views = 0  # encapsulated counter

    # Encapsulation via read-only properties
    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def genre(self) -> str:
        return self._genre

    @property
    def views(self) -> int:
        return self._views

    def _inc_views(self):  # protected-style helper
        self._views += 1

    @abstractmethod
    def display_info(self) -> str:
        """Polymorphic summary for UI/list views."""

    @abstractmethod
    def duration(self) -> int:
        """Polymorphic total minutes."""

class Movie(Content):
    def __init__(self, title: str, genre: str, runtime_minutes: int):
        super().__init__(title, genre)
        self._runtime_minutes = runtime_minutes

    def display_info(self) -> str:
        return f"Movie #{self.id}: {self.title} [{self.genre}] — {self._runtime_minutes} min, views={self.views}"

    def duration(self) -> int:
        return self._runtime_minutes

class Episode:
    def __init__(self, title: str, minutes: int):
        self.title = title
        self.minutes = minutes

class Series(Content):
    def __init__(self, title: str, genre: str, episodes: List[Episode]):
        super().__init__(title, genre)
        self._episodes = episodes  # list of Episode

    def display_info(self) -> str:
        return f"Series #{self.id}: {self.title} [{self.genre}] — {len(self._episodes)} eps, {self.duration()} min total, views={self.views}"

    def duration(self) -> int:
        return sum(ep.minutes for ep in self._episodes)

# -----------------------------
# Users + Subscriptions
# -----------------------------
class User:
    _next_id = 1

    def __init__(self, name: str, email: str, phone: str, role: str):
        self._user_id = User._next_id
        User._next_id += 1
        self._name = name
        self._email = email
        self._phone = phone
        self._role = role  # 'viewer' or 'admin'
        self._subscription: Optional[Subscription] = None
        self._watchlist: set[int] = set()
        self.history: List[int] = []

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def role(self) -> str:
        return self._role

    @property
    def subscription(self) -> Optional["Subscription"]:
        return self._subscription

    def set_subscription(self, sub: Optional["Subscription"]) -> None:
        self._subscription = sub

    def add_to_watchlist(self, content_id: int) -> None:
        self._watchlist.add(content_id)

    def remove_from_watchlist(self, content_id: int) -> None:
        self._watchlist.discard(content_id)

    def has_active_subscription(self) -> bool:
        return bool(self._subscription and self._subscription.is_active)

    def __repr__(self) -> str:
        return f"User#{self.user_id}({self.name}, role={self.role})"

class Viewer(User):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email, phone, role="viewer")

class Admin(User):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email, phone, role="admin")

class SubscriptionPlan:
    # class-level registry (class attribute)
    plans: Dict[str, int] = {}

    @classmethod
    def create_default_plans(cls) -> None:
        """Class method: prepare some common Hotstar-like plans (in INR)."""
        cls.plans = {
            "Basic": Money.rupees_to_cents(149.0),
            "Super": Money.rupees_to_cents(299.0),
            "Premium": Money.rupees_to_cents(499.0),
        }

    @classmethod
    def get_price_cents(cls, name: str) -> Optional[int]:
        return cls.plans.get(name)

@dataclass
class Subscription:
    user_id: int
    plan_name: str
    is_active: bool = True

# -----------------------------
# Controller / Manager: HotstarApp
# -----------------------------
class HotstarApp:
    revenue_cents: int = 0  # class attribute: total revenue across all app instances

    def __init__(self) -> None:
        self.users: Dict[int, User] = {}
        self.content: Dict[int, Content] = {}

    # --- user management ---
    def register_viewer(self, name: str, email: str, phone: str) -> Viewer:
        v = Viewer(name, email, phone)
        self.users[v.user_id] = v
        return v

    def register_admin(self, name: str, email: str, phone: str) -> Admin:
        a = Admin(name, email, phone)
        self.users[a.user_id] = a
        return a

    # --- content management (admin) ---
    def add_movie(self, admin_id: int, title: str, genre: str, runtime_minutes: int) -> Optional[Movie]:
        if not self._is_admin(admin_id):
            print("Only admins can add content.")
            return None
        m = Movie(title, genre, runtime_minutes)
        self.content[m.id] = m
        return m

    def add_series(self, admin_id: int, title: str, genre: str, episodes: List[Episode]) -> Optional[Series]:
        if not self._is_admin(admin_id):
            print("Only admins can add content.")
            return None
        s = Series(title, genre, episodes)
        self.content[s.id] = s
        return s

    def _is_admin(self, user_id: int) -> bool:
        u = self.users.get(user_id)
        return isinstance(u, Admin)

    # --- subscriptions ---
    def subscribe(self, user_id: int, plan_name: str) -> bool:
        user = self.users.get(user_id)
        price = SubscriptionPlan.get_price_cents(plan_name)
        if not user or price is None:
            print("Invalid user/plan.")
            return False
        user.set_subscription(Subscription(user_id, plan_name, True))
        HotstarApp.revenue_cents += price
        print(f"Subscribed {user.name} to {plan_name} (₹{Money.cents_to_rupees(price)})")
        return True

    # --- playback ---
    def play(self, user_id: int, content_id: int) -> bool:
        user = self.users.get(user_id)
        item = self.content.get(content_id)
        if not user or not item:
            print("Invalid user/content.")
            return False
        if not user.has_active_subscription():
            print("Please subscribe to play content.")
            return False
        item._inc_views()  # encapsulated counter increment
        user.history.append(item.id)
        print(f"Playing: {item.title} ({item.duration()} min)")
        return True

    # --- reports ---
    def report_total_revenue(self) -> str:
        return f"Total Revenue: ₹{Money.cents_to_rupees(HotstarApp.revenue_cents)}"

    def report_top_content(self, top_n: int = 5) -> List[str]:
        items = sorted(self.content.values(), key=lambda c: c.views, reverse=True)[:top_n]
        return [f"{c.title} — {c.views} views" for c in items]

    def list_users(self) -> List[str]:
        return [f"{u.user_id}: {u.name} ({u.role})" for u in self.users.values()]

    def list_content(self) -> List[str]:
        return [c.display_info() for c in self.content.values()]

# -----------------------------
# Simple CLI (easy to read)
# -----------------------------

def seed_data(app: HotstarApp) -> int:
    """Create one admin and some sample content + plans. Returns admin_id."""
    SubscriptionPlan.create_default_plans()
    admin = app.register_admin("Hotstar Admin", "admin@hotstar", "99999")
    # Add a couple of content items
    app.add_movie(admin.user_id, "Premalu", "RomCom", 156)
    app.add_movie(admin.user_id, "Vikram", "Action", 174)
    eps = [Episode("Ep1", 42), Episode("Ep2", 45), Episode("Ep3", 40)]
    app.add_series(admin.user_id, "Aarya", "Thriller", eps)
    return admin.user_id


def run_cli() -> None:
    app = HotstarApp()
    admin_id = seed_data(app)

    print("\nWelcome to Simple Hotstar CLI")
    print("(Admin pre-created: id=", admin_id, ")")

    while True:
        print("\nMain Menu:")
        print("1) Register Viewer")
        print("2) Subscribe Viewer")
        print("3) List Content")
        print("4) Play Content")
        print("5) Reports")
        print("6) Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            v = app.register_viewer(name, email, phone)
            print(f"Registered viewer with id={v.user_id}")

        elif choice == "2":
            try:
                uid = int(input("Viewer id: "))
            except ValueError:
                print("Invalid id")
                continue
            print("Plans:")
            for p, price in SubscriptionPlan.plans.items():
                print(f"- {p}: ₹{Money.cents_to_rupees(price)}")
            plan = input("Plan name: ")
            app.subscribe(uid, plan)

        elif choice == "3":
            for line in app.list_content():
                print(line)

        elif choice == "4":
            try:
                uid = int(input("Viewer id: "))
                cid = int(input("Content id to play: "))
            except ValueError:
                print("Invalid id")
                continue
            app.play(uid, cid)

        elif choice == "5":
            print(app.report_total_revenue())
            print("Top content:")
            for row in app.report_top_content():
                print("-", row)
            print("Users:")
            for row in app.list_users():
                print("-", row)

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# To run the CLI directly, uncomment the next line:
run_cli()

"""
OUTPUT:=

Sample CLI Interaction (short)

Welcome to Simple Hotstar CLI
(Admin pre-created: id= 1 )

Main Menu:
1) Register Viewer
2) Subscribe Viewer
3) List Content
4) Play Content
5) Reports
6) Exit
Choose: 1
Name: Pravalika
Email: p@x
Phone: 12345
Registered viewer with id=2

Choose: 2
Viewer id: 2
Plans:
- Basic: ₹149.0
- Super: ₹299.0
- Premium: ₹499.0
Plan name: Super
Subscribed Pravalika to Super (₹299.0)

Choose: 3
Movie #2: Premalu [RomCom] — 156 min, views=0
Movie #3: Vikram [Action] — 174 min, views=0
Series #4: Aarya [Thriller] — 3 eps, 127 min total, views=0

Choose: 4
Viewer id: 2
Content id to play: 2
Playing: Premalu (156 min)

Choose: 5
Total Revenue: ₹299.0
Top content:
- Premalu — 1 views
Users:
- 1: Hotstar Admin (admin)
- 2: Pravalika (viewer)

"""
