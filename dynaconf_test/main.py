from .config import settings


def main():
    print(f"Environment: {settings.ACTIVE_ENV}")
    print(f"Secret: {settings.DEMO_SECRET}")


if __name__ == '__main__':
    main()
