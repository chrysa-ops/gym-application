# data_store.py
from __future__ import annotations
from typing import Dict, List, Optional
from models import Member, Facility


class DataStore:


    def __init__(self) -> None:
        self.members: Dict[str, Member] = {}
        self.facilities: List[Facility] = []

    # --- Members ---

    def add_member(self, member: Member) -> None:
        self.members[member.digital_id] = member

    def get_member(self, digital_id: str) -> Optional[Member]:
        return self.members.get(digital_id)

    def list_members(self) -> List[Member]:
        return list(self.members.values())

    # --- Facilities ---

    def add_facility(self, facility: Facility) -> None:
        self.facilities.append(facility)

    def list_facilities(self) -> List[Facility]:
        return self.facilities

