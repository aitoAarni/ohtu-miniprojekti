from interface import Interface
from services.reference_service import ReferenceService
from repositories.reference_repository import default_reference_repository
from user_input import UserInput


def main():
    reference_service = ReferenceService(default_reference_repository)
    user_io = UserInput()
    interface = Interface(reference_service, user_io)

    interface.start()


if __name__ == "__main__":
    main()
