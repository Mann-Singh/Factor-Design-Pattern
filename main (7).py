# Authors: Prabhas Dama and Manjot Singh
#Date: 4/16/25
#Description: This program is uses the abstract factory design pattern to create a game where the player fights 4 different types of monsters made by two different factories and include 2 variations of each monster.

import hero
import beg_factory
import exp_factory
import check_input
import random


def main():
  print("Monster Trials")
  print("What is your name?")
  hero_name = input()
  fact1 = beg_factory.BeginnerFactory()
  fact2 = exp_factory.ExpertFactory()
  the_hero = hero.Hero(hero_name)
  """Initializes the list of enemies: 2 beginner and 1 expert"""
  enemies = [
      fact1.create_random_enemy(),
      fact1.create_random_enemy(),
      fact2.create_random_enemy()
  ]

  print(f"You will face a series of three monsters, {hero_name}." +
        "\ndefeat them all to win \n")
  
  """Runs until player dies or all enemies are defeated"""
  while the_hero.hp > 0 and enemies:
    print(f"\n{the_hero}")
    for i, enemy in enumerate(enemies, 1):
      print(f"{i}. Attack {enemy}")

    enemy_choice = check_input.get_int_range("Choose an enemy to attack: ", 1,
                                      len(enemies)) - 1
    
    print("\nAttack with:")
    print("1. Sword Attack")
    print("2. Arrow Attack")
    attack_choice = check_input.get_int_range("Enter choice: ", 1, 2)

    enemy = enemies[enemy_choice] 
    if attack_choice == 1:
      attack_msg = the_hero.melee_attack(enemy)
      print(attack_msg)
    else: 
      attack_msg = the_hero.ranged_attack(enemy)
      print(attack_msg)

    if enemy.hp == 0:
      print(f"You have slain the {enemy.name}!")
      enemies.remove(enemy)
      if not enemies:
        break
    """Chooses a random enemy to attack the player"""
    attacker = random.choice(enemies)
    print(attacker.melee_attack(the_hero))

  if the_hero.hp > 0:
    print("Congratulations! You have defeated all 3 monsters!.")
  else:
    print("You have been defeated by the monsters!")
  print("Game Over")


main()
