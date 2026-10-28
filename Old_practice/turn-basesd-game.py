import random


# ─────────────────────────── CONSTANTS ─────────────────────────────────

VALID_MOVES = {"kick", "punch", "gun", "knife"}

MOVE_DAMAGE = {
    "kick": 50,
    "punch": 30,
    "gun": 100,
    "knife": 80,
}

BOSS_DAMAGE_MAP = {
    "strike": 150,
    "gun": 100,
    "laser": 200,
    "kick": 50,
    "throw": 120,
}

BOSS_MOVES = list(BOSS_DAMAGE_MAP.keys())


# ─────────────────────────── CORE LOGIC ────────────────────────────────

def computer():
    """Pick a random move for the computer opponent."""
    return random.choice(list(VALID_MOVES))


def damage(move):
    """Return damage for a player move. 0 for invalid moves."""
    return MOVE_DAMAGE.get(move, 0)


def boss_attack():
    """Pick a random boss attack."""
    return random.choice(BOSS_MOVES)


def boss_damage(attack_name):
    """Return damage for a boss attack. 0 for unknown attacks."""
    return BOSS_DAMAGE_MAP.get(attack_name, 0)


# ─────────────────────────── INPUT HELPERS ─────────────────────────────

def get_player_move():
    """
    Prompt until a valid, non-empty combat move is entered.
    Edge cases handled: empty input, whitespace-only, unknown move names.
    """
    while True:
        raw = input("Choose your move — kick / punch / gun / knife: ").strip().lower()
        if not raw:
            print("⚠  You didn't type anything. Please enter a move.")
            continue
        if raw not in VALID_MOVES:
            print(f"⚠  '{raw}' is not a valid move. Choose from: kick, punch, gun, knife.")
            continue
        return raw


def get_dodge_guess():
    """
    Prompt until a valid integer in [1, 10] is entered.
    Edge cases handled: empty input, non-integer text, numbers < 1 or > 10.
    """
    while True:
        raw = input("Guess the number to dodge (1–10): ").strip()
        if not raw:
            print("⚠  You didn't enter anything. Please type a number between 1 and 10.")
            continue
        try:
            guess = int(raw)
        except ValueError:
            print("⚠  That's not a valid number. Please enter a whole number between 1 and 10.")
            continue
        if guess < 1 or guess > 10:
            print("⚠  Out of range! Please enter a number between 1 and 10.")
            continue
        return guess


def ask_yes_no(prompt):
    """
    Ask a yes/no question and return True for yes, False for no.
    Edge cases handled: empty input, whitespace-only, anything other than y/yes/n/no.
    """
    while True:
        raw = input(prompt).strip().lower()
        if not raw:
            print("⚠  Please type 'y' or 'n'.")
            continue
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("⚠  Invalid input. Please type 'y' for yes or 'n' for no.")


# ─────────────────────────── LEVEL 1 ───────────────────────────────────

def play_level_1():
    """
    Level 1 — Street fight against the computer.
    Fixed bugs:
      - Invalid moves no longer silently deal 0 damage while still eating a turn;
        the player is re-prompted until they pick a valid move.
      - Round counter increments only after a full valid round completes.
    Returns True if the player wins, False on loss or draw.
    """
    my_health = 500
    com_health = 500
    turn = 0

    print("\n" + "=" * 54)
    print("  ⚔   LEVEL 1 — Street Fight  ⚔")
    print("=" * 54)
    print(f"  Your HP : {my_health}   |   Computer HP : {com_health}")
    print("=" * 54 + "\n")

    while True:
        print(f"\n── Round {turn + 1} ──")

        # Player picks a validated move (loops on bad input)
        my_try = get_player_move()
        my_dmg = damage(my_try)

        # Computer picks its move
        com_move = computer()
        com_dmg = damage(com_move)

        # Apply damage
        my_health -= com_dmg
        com_health -= my_dmg
        turn += 1

        # Round summary
        print("----------------------------------------------")
        print(f"  You used  : {my_try:<6}  →  dealt {my_dmg} damage")
        print(f"  Computer  : {com_move:<6}  →  dealt {com_dmg} damage")
        print("──────────────────── HEALTH ──────────────────")
        print(f"  Your HP       : {max(0, my_health)}")
        print(f"  Computer HP   : {max(0, com_health)}")
        print("----------------------------------------------")
        print(f"  End of round {turn}")

        # End-condition checks (draw checked first so simultaneous KO = draw)
        if my_health <= 0 and com_health <= 0:
            print("\n💀  Double knockout! It's a draw.")
            return False
        elif com_health <= 0:
            print("\n🏆  You defeated the computer!")
            return True
        elif my_health <= 0:
            print("\n💀  You were defeated. Game over!")
            return False


# ─────────────────────────── LEVEL 2 ───────────────────────────────────

def play_level_2():
    """
    Level 2 — Dodge-battle against the Boss.
    Fixed bugs:
      - round_num now starts at 0 and increments at the TOP of each loop
        iteration so Round 1 is correctly labelled as Round 1 (was Round 2).
      - Out-of-range and non-integer dodge guesses are now rejected with
        helpful messages instead of crashing or silently accepting bad input.
      - Boss attack name is now revealed even on a successful dodge so the
        player knows what they avoided.
      - Draw condition (both reach 0 HP simultaneously) checked first.
    Edge cases added:
      - Empty dodge input re-prompts the player.
      - Negative / zero dodge guess rejected.
      - Guess > 10 rejected.
    """
    lvl_2_health = 500
    boss_health = 300
    round_num = 0          # FIX: was 1; incremented before round plays → wrong label

    print("\n" + "=" * 54)
    print("  🔥  LEVEL 2 — Boss Battle  🔥")
    print("=" * 54)
    print("  You have no weapon here.")
    print("  Dodge the boss by guessing the right number (1–10)!")
    print("  Correct dodge  → counter-damage hits the boss.")
    print("  Wrong guess    → the boss hits you hard.")
    print(f"\n  Your HP : {lvl_2_health}   |   Boss HP : {boss_health}")
    print("=" * 54 + "\n")

    while True:
        round_num += 1          # FIX: increment here so label = actual round played
        print(f"\n── Dodge Round {round_num} ──")
        print(f"  Your HP : {max(0, lvl_2_health)}   |   Boss HP : {max(0, boss_health)}")

        # Secret dodge number
        dodge_num = random.randint(1, 10)

        # Boss telegraphs attack (player sees the name to add tension)
        b_att = boss_attack()
        b_dam = boss_damage(b_att)
        print(f"  The boss prepares a {b_att.upper()}…")

        # Validated dodge guess
        player_guess = get_dodge_guess()

        print("-------------------------------")
        if player_guess == dodge_num:
            # Successful dodge
            dodge_damage_options = [20, 30, 50, 5000]
            counter_dmg = random.choice(dodge_damage_options)
            boss_health -= counter_dmg
            print(f"  ✅  Perfect dodge! (The number was {dodge_num})")
            print(f"  You avoided the {b_att} and countered for {counter_dmg} damage!")
            print(f"  Boss HP: {max(0, boss_health)}")
        else:
            # Failed dodge
            lvl_2_health -= b_dam
            print(f"  ❌  Wrong! The number was {dodge_num} — you got hit!")
            print(f"  The boss's {b_att} dealt {b_dam} damage to you.")
            print(f"  Your HP  : {max(0, lvl_2_health)}")
            print(f"  Boss HP  : {max(0, boss_health)}")
        print("-------------------------------")

        # End-condition checks (draw checked first)
        if lvl_2_health <= 0 and boss_health <= 0:
            print("\n💥  Both you and the boss collapsed! It's a draw.")
            print("──────────────── GAME OVER ────────────────")
            break
        elif lvl_2_health <= 0:
            print("\n💀  You were defeated by the boss. Game over!")
            print("──────────────── GAME OVER ────────────────")
            break
        elif boss_health <= 0:
            print("\n🏆  The boss has been defeated! YOU WIN!")
            print("──────────────── GAME OVER ────────────────")
            break


# ─────────────────────────── MAIN ──────────────────────────────────────

def play_game():
    """
    Outer game loop.
    Edge case added: replay prompt after every session so the player
    can restart without re-running the script.
    """
    while True:
        # ── Level 1 ──
        won_level_1 = play_level_1()

        # ── Level 2 (only if player won Level 1) ──
        if won_level_1:
            if ask_yes_no("\nWant to jump into Level 2? (y/n): "):
                play_level_2()
            else:
                print("\nThanks for playing! See you next time. 👋")
        else:
            print("\nBetter luck next time!")

        # ── Replay ──
        if not ask_yes_no("\nPlay again from the beginning? (y/n): "):
            print("Thanks for playing! Goodbye. 👋")
            break


if __name__ == "__main__":
    play_game()

