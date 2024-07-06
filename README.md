# Quant League: Algorithmic Trading Bot

Welcome to the official repository of Quant League's Algorithmic Trading Bot. This project is the culmination of efforts by a dedicated team of developers, data scientist, and financial analysts aiming to compete in the prestigious Quant League competition. Our bot leverages advanced algorithms and machine learning techniques to analyze market data and execute trades with precision and speed.

## Team Members

-   Quang Chinh Trieu - Software Engineer
-   Khanh Linh Chu - Financial Analyst
-   Viet Anh Nguyen - Data Scientist
-   Chanh Thanh Tang - Data Scientist

## Project Overview

The Quant League Algorithmic Trading Bot is designed to automate trading strategies, reducing the need for manual intervention and aiming to maximize returns while minimizing risks. It operates by analyzing real-time market data, identifying potential trading opportunities based on predefined criteria, and executing trades accordingly.

## Key Features

-   **Real-Time Market Analysis**: Utilizes live market data to make informed trading decisions.
-   **Advanced Trading Strategies**: Implements a variety of algorithmic trading strategies tailored to different market conditions.
-   **Machine Learning Integration**: Employs machine learning models to predict market trends and optimize trading strategies.
-   **Risk Management**: Incorporates risk management protocols to safeguard investments against market volatility.

## Code Repo Migration

### Quant Connect PEP8 Migration

As part of our commitment to maintaining high-quality code standards, we have migrated our codebase to adhere to PEP8 guidelines. This ensures better readability and maintainability of our code. Below are some examples of the changes implemented:

#### Before and After PEP8 Migration

-   **Lowercase Properties, Snake Case Variables**

    -   Before: `self.Portfolio[self.Securities[self.spy]].HoldingsValue`
    -   After: `self.portfolio[self.securities[self.spy]].holdings_value`

-   **Snake Case Parameters**

    -   Before: `self.AddEquity("SPY", extendedMarketHours=True)`
    -   After: `self.add_equity("SPY", extended_market_hours=True)`

-   **Capitalized Constants, CamelCase Classes**

    -   Before: `if securityChanges == SecurityChanges.None:`
    -   After: `if security_changes == SecurityChanges.NONE`

-   **Snake Case Methods**

    -   Before: `def OnData(self, data):`
    -   After: `def on_data(self, data):`

-   **Lowercase Methods, Prefix for Private Variables**
    -   Before: `self.ema = self.EMA(symbol, 30, Resolution.Minute)`
    -   After: `self._ema = self.ema(symbol, 20, Resolution.MINUTE)`

## Getting Started

// Todo

## Contribution

// Todo

## License

This project is licensed under the MIT License - see the LICENSE file for details.
