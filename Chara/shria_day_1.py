from Chara.character import Person


if __name__ == "__main__":
    shria = Person(stress=1)
    shria.show_status()
    shria.actions.nap(hours=2)
    shria.show_status()