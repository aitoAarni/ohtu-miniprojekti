from interface import Interface
from services.reference_service import ReferenceService
from repositories.reference_repository import ReferenceRepository


def main():
    reference_repository = ReferenceRepository()
    reference_service = ReferenceService(reference_repository)
    interface = Interface(reference_service)

    interface.start()


if __name__ == "__main__":
    main()
