# SPDX-License-Identifier: GPL-3.0
# Copyright (c) 2014-2023 William Edwards <shadowapex@gmail.com>, Benjamin Bean <superman2k5@gmail.com>
from __future__ import annotations

from dataclasses import dataclass
from operator import eq, ge, gt, le, lt
from typing import TYPE_CHECKING, Callable, Mapping, Optional, Union

from tuxemon.condition.condcondition import CondCondition

if TYPE_CHECKING:
    from tuxemon.monster import Monster

cmp_dict: Mapping[Optional[str], Callable[[float, float], bool]] = {
    None: ge,
    "<": lt,
    "<=": le,
    ">": gt,
    ">=": ge,
    "==": eq,
    "=": eq,
}


@dataclass
class CurrentHitPointsCondition(CondCondition):
    """
    Compares the Monster's current hitpoints against the given value.

    If an integer is passed, it will compare against the number directly, if a
    decimal between 0.0 and 1.0 is passed it will compare the current hp
    against the total hp.

    Example:
    "conditions": [
        "is current_hp <,1.0",
    ],

    """

    name = "current_hp"
    comparison: str
    value: Union[int, float]

    def test(self, target: Monster) -> bool:
        lhs = target.current_hp
        op = cmp_dict[self.comparison]
        if type(self.value) is float:
            rhs = target.hp * self.value
        else:
            rhs = self.value

        return op(lhs, rhs)
