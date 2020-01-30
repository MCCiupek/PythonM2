from Quote import Quote


class TradeSituation:
    # This variable will be incremented after each call of TradeSituation.generate_next_id().
    # It is used to populate __trade_situation_id.
    __common_trade_situation_id: int = 0
    # Instance attributes
    # Unique ID of the trade_situation
    __trade_situation_id: int
    # If True: it's a LONG (BUY) trade. If False: it's a SHORT (SELL) trade.
    __is_long_trade: bool
    # Quote saved when we opened the position
    __executed_open_quote: Quote
    # Quote saved when we close the position
    __executed_close_quote: Quote
    # Flag used to describe if the position is opened or closed
    __is_closed: bool
    # Maximum draw down in basis points. Always positive!
    __max_dd_in_bps: float
    # Latest profit or loss of the position in basis points
    __pnl_bps: float
    # Take profit in basis points
    __take_profit_in_bps: float
    __transaction_price: float

    def __init__(self, open_order_arg: Quote, is_long_trade_arg: bool, take_profit_in_bps_arg: float, transaction_price_arg: float):
        # Init locals
        self.__is_closed = True
        self.__is_long_trade = is_long_trade_arg
        self.__max_dd_in_bps = 0
        self.__pnl_bps = 0
        self.__executed_open_quote = None
        self.__executed_close_quote = None
        self.__take_profit_in_bps = take_profit_in_bps_arg
        self.__transaction_price = transaction_price_arg

        # Update and set the __trade_situation_id
        self.__trade_situation_id = TradeSituation.generate_next_id()

        # Check arguments sanity.
        if take_profit_in_bps_arg < 0.0:
            raise Exception("Please note that the take profit has to be positive (:2.2f)"
                            .format(take_profit_in_bps_arg))

        # Call self.open_position(...) to open the position immediately
        self.open_position(open_order_arg)

    def open_position(self, quote_arg: Quote):
        """
        Flags the is_closed to False. Saves the entry order.
        :param quote_arg: quote class's instance expected. The first quote.
        :return:
        """
        # Sets the __executed_open_quote to argument's value and flags __is_closed to FALSE
        self.__executed_open_quote = quote_arg
        self.calculate_pnl_and_dd(quote_arg)
        self.__is_closed = False

    def close_position(self, quote_arg: Quote):
        """
        Flags the position as closed. Calculates final PnL
        :param quote_arg: last quote
        :return:
        """
        # Sets the __executed_close_quote to argument's value, calculates PNL and flags __is_closed to TRUE
        self.__executed_close_quote = quote_arg
        self.calculate_pnl_and_dd(quote_arg)
        self.__is_closed = True

    def update_on_order(self, quote_arg: Quote) -> bool:
        """
        Updates all the variables in the position. Calculates the PnL.
        :param quote_arg: the latest quote
        :return: returns True if the position was closed (target profit reached)
        """
        # Check if the position is alive. Return false if the position is dormant
        if self.__is_closed:
            return False

        # Check/update current pnl and draw down
        curr_pnl = self.calculate_pnl_and_dd(quote_arg)

        # Check if target pnl was reached
        if curr_pnl >= self.__take_profit_in_bps + self.__executed_open_quote.price():
            # Target pnl reached: close position; set __is_closed accordingly
            self.close_position(quote_arg)
            # Return True
            return True

        # PnL target not reached: return false
        return False

    def calculate_pnl_and_dd(self, quote_arg: Quote) -> float:
        """
        Calculates (and updates) the PnL and draw down for the position
        :param quote_arg: the current quote
        :return: current pnl
        """
        # In case the position is not opened (not alive) return the value stored in __pnl_bps
        if self.__is_closed:
            return self.__pnl_bps

        # Calculate pnl (different for LONG and SHORT)
        if self.__is_long_trade:
            self.__pnl_bps = -self.__transaction_price +\
                quote_arg.price() - self.__executed_open_quote.price()
        else:
            self.__pnl_bps = -self.__transaction_price - \
                quote_arg.price() + self.__executed_open_quote.price()

        # Calculate draw down
        self.__max_dd_in_bps = max(self.__max_dd_in_bps, -self.__pnl_bps)

        # return __pnl_bps
        return self.__pnl_bps

    def return_current_pnl(self) -> float:
        """
        Returns the current (or final if the position is closed) pnl.
        :return:
        """
        return self.__pnl_bps

    def return_current_draw_down(self) -> float:
        """
        Returns the current (or final if the position is closed) maximum draw down.
        :return:
        """
        return self.__max_dd_in_bps

    def trade_situation_id(self) -> int:
        """
        Returns this trade situation ID
        :return:
        """
        return self.__trade_situation_id

    def is_closed(self):
        """
        Returns true if the position was closed previously
        :return:
        """
        return self.__is_closed

    @staticmethod
    def generate_next_id():
        TradeSituation.__common_trade_situation_id += 1
        return TradeSituation.__common_trade_situation_id


