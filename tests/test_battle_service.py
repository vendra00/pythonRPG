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
        hero.health = 100
        enemy.health = 100
        hero.max_health = 100
        enemy.max_health = 100
        hero.mana = 100
        enemy.mana = 100
        hero.max_mana = 100
        enemy.max_mana = 100
        hero.stamina = 100
        enemy.stamina = 100
        hero.max_stamina = 100
        enemy.max_stamina = 100
        hero.experience = 0
        enemy.experience = 0
        hero.level = 1
        enemy.level = 1
        hero.attributes.strength = 10
        enemy.attributes.strength = 10
        hero.attributes.dexterity = 10
        enemy.attributes.dexterity = 10
        hero.attributes.intelligence = 10
        enemy.attributes.intelligence = 10
        hero.attack = 10
        enemy.attack = 10

        # Set up return values for get_decision
        mock_get_decision.return_value = ('attack', None)

        # Set up the side effect for perform_decision to decrease health
        def decrease_health(attacker, defender, _):
            defender.health -= attacker.attack

        mock_perform_decision.side_effect = decrease_health

        # Act
        battle(hero, enemy)

        # Assert
        mock_get_decision.assert_any_call(hero)
        mock_get_decision.assert_any_call(enemy)
        mock_perform_decision.assert_any_call(hero, enemy, ('attack', None))
        mock_perform_decision.assert_any_call(enemy, hero, ('attack', None))
