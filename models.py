# models.py
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from datetime import time, date
import uuid


class MembershipLevel(Enum):
    BASIC = "basic"
    PREMIUM = "premium"
    PERSONAL_TRAINING = "personal_training"


class MembershipDuration(Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    HALF_YEARLY = "half_yearly"
    YEARLY = "yearly"


@dataclass
class Schedule:
    day_of_week: str  # e.g. "Δευτέρα"
    start_time: time
    end_time: time

    def __str__(self) -> str:
        return f"{self.day_of_week} {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"


@dataclass
class Membership:
    level: MembershipLevel
    duration: MembershipDuration
    start_date: date
    active: bool = True

    def __str__(self) -> str:
        return f"{self.level.value} ({self.duration.value}) από {self.start_date.isoformat()}"


@dataclass
class Member:
    full_name: str
    age: int
    membership: Membership
    schedules: list[Schedule] = field(default_factory=list)
    digital_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    parental_consent: bool = False

    def can_register(self) -> bool:
        """Minors (<18) χρειάζονται γονική συναίνεση."""
        if self.age < 18 and not self.parental_consent:
            return False
        return True

    def can_access_premium(self) -> bool:
        return self.membership.level in {
            MembershipLevel.PREMIUM,
            MembershipLevel.PERSONAL_TRAINING,
        }

    def __str__(self) -> str:
        return f"{self.full_name} (Ηλικία: {self.age}, ID: {self.digital_id})"


@dataclass
class Trainer:
    full_name: str
    specialty: str

    def __str__(self) -> str:
        return f"Trainer: {self.full_name} - {self.specialty}"


@dataclass
class Administrator:
    full_name: str

    def __str__(self) -> str:
        return f"Admin: {self.full_name}"


@dataclass
class Facility:
    name: str
    premium_only: bool = False

    def __str__(self) -> str:
        label = "Premium" if self.premium_only else "Basic"
        return f"{self.name} ({label})"

