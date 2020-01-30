from datetime import datetime


class Quote:
    # Static field with incrementing ID for the current quote.
    # This variable will be incremented after each call of TradeSituation.generate_next_id().
    # It is used to populate __quote_id.
    __common_quote_id: int = 0
    # This class encapsulates all the necessary information for a specific quote.
    __quote_id: int
    # Time of the quote (to set in init).
    __quote_time: datetime
    # Close price.
    __quote_close_px: float
    # Ticker id: use a number instead of the STRING representation.
    __quote_ticker_id: int

    def __init__(self, quote_ticker_id_arg: int, quote_close_px_arg: float, quote_time_arg: datetime):
        """
        Initializes the instance of the Quote.
        :param quote_ticker_id_arg: ticker ID (use int instead of the "string" for memory conservation)
        :param quote_close_px_arg:
        :param quote_time_arg:
        """
        # Generate unique ID of this quote
        self.__quote_id = Quote.generate_next_id()
        # Set up the local variables
        self.__quote_ticker_id = quote_ticker_id_arg
        self.__quote_close_px = quote_close_px_arg
        self.__quote_time = quote_time_arg

    def id(self) -> int:
        """
        Returns the ID of this specific quote
        :return:
        """
        return self.__quote_id

    def price(self) -> float:
        """
        Returns the price corresponding to a specific datetime
        :return:
        """
        return self.__quote_close_px

    def time(self) -> datetime:
        """
        Returns the datetime of this specifiq quote
        :return:
        """
        return self.__quote_time

    def ticker_id(self) -> int:
        """
        Returns the ID of the ticker.
        :return:
        """
        return self.__quote_ticker_id

    @staticmethod
    def generate_next_id():
        Quote.__common_quote_id += 1
        return Quote.__common_quote_id
