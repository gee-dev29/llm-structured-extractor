from src.extractor import extract_ticket

def main():

    text = """
    Hi,

    I'm John and I bought the wireless keyboard last week.
    The keyboard arrived yesterday but several keys aren't
    working. I'm really annoyed because I need it for work.

    Please either send me a replacement or refund me.

    Thanks,
    John
    """

    result = extract_ticket(text)

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()