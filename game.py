import random

WELCOME_MESSAGE = "Selam! Tahmin oyununa hoş geldin. 1 ile 100 arasında bir sayı tuttum."
PROMPT_MESSAGE = "Tahminini gir (çıkmak için q): "


def generate_secret(lower: int = 1, upper: int = 100) -> int:
    """Return a random integer within the inclusive range."""
    return random.randint(lower, upper)


def evaluate_guess(guess: int, secret: int) -> str:
    """Return feedback for the given guess relative to the secret number."""
    if guess < secret:
        return "Daha yüksek!"
    if guess > secret:
        return "Daha düşük!"
    return "Doğru!"  # guess == secret


def read_guess() -> int | None:
    """Read a guess from the user, handling exits and validation."""
    raw = input(PROMPT_MESSAGE).strip()
    if raw.lower() == "q":
        return None

    if not raw.isdigit():
        print("Lütfen sadece rakam yaz veya çıkmak için q'ya bas.")
        return read_guess()

    return int(raw)


def play_round() -> bool:
    """Play a single round. Returns False if the player quits."""
    secret = generate_secret()
    attempts = 0
    print(WELCOME_MESSAGE)

    while True:
        guess = read_guess()
        if guess is None:
            print("Görüşmek üzere!")
            return False

        attempts += 1
        feedback = evaluate_guess(guess, secret)
        print(feedback)

        if feedback == "Doğru!":
            print(f"{attempts} denemede bildin!")
            return True


def main() -> None:
    """Run the interactive guessing game loop."""
    while True:
        keep_playing = play_round()
        if not keep_playing:
            break

        again = input("Bir raund daha? (e/h): ").strip().lower()
        if again != "e":
            print("Oynadığın için teşekkürler!")
            break


if __name__ == "__main__":
    main()
