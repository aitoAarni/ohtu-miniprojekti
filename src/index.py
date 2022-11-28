from interface import Interface
from services.reference_service import ReferenceService
from repositories.reference_repository import default_reference_repository


def main():
    reference_service = ReferenceService(default_reference_repository)
    interface = Interface(reference_service)

    interface.start()


if __name__ == "__main__":
    main()
