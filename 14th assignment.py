import logging


logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

def perform_division(x, y):
    try:
        logging.debug("Starting division operation.")

        answer = x / y

        logging.info(f"Division successful: {x} / {y} = {answer}")
        return answer

    except ZeroDivisionError:
        logging.exception("Error occurred: Division by zero is not allowed.")

    except Exception:
        logging.exception("An unexpected error occurred.")

def run_application():
    logging.info("Application started.")

    try:
        value1 = 20
        value2 = 5

        logging.debug(f"Input values: value1={value1}, value2={value2}")

        output = perform_division(value1, value2)
        print("Division Result:", output)

        # Test exception handling
        logging.info("Testing division by zero.")
        perform_division(10, 0)

    except Exception:
        logging.exception("Error in main function.")

    finally:
        logging.info("Application execution completed.")

if __name__ == "__main__":
    run_application()