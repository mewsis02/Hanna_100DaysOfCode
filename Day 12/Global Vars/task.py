
# Modifying Global Scope

enemies = 1


def increase_enemies(enemy):
    enemy += 1
    print(f"enemies inside function: {enemy}")
    return enemy


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


