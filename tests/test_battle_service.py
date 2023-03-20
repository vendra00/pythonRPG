import unittest
from unittest.mock import Mock, patch

from service.battle_service import battle


class TestBattleService(unittest.TestCase):
    @patch("service.battle_service.get_decision")
    @patch("service.battle_service.perform_decision")
    def test_battle(self, mock_perform_decision, mock_get_decision):
        # Arrange
        hero = Mock()
        enemy = Mock()

        # Set up return values for get_decision
        mock_get_decision.return_value = ('attack', None)

        # Act
        battle(hero, enemy)

        # Assert
        mock_get_decision.assert_any_call(hero)
        mock_get_decision.assert_any_call(enemy)
        mock_perform_decision.assert_any_call(hero, enemy, ('attack', None))
        mock_perform_decision.assert_any_call(enemy, hero, ('attack', None))
