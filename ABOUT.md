### Setting up enviroment

For the setup of the enviroment (Airflow) we've used a Docker instance running in Ubuntu Server.

Once the enviroment was running, we've installed the following libraries:
* requests ->  To make the API request
* sqlalchemy ->  To make the Database requests
* matplotlib and mplfinance -> To draw the plot
* pytest ->  To execute test tasks to the scripts.

The Postgres database was provided by Airflow, and we've logged in using `postgres`:`postgres`@`localhost` as credentials.

### DAG

In this case, the dag doesn't have any schedule, we only use the `Python Operator Library` from Airflow, to call the external python scripts.

We have 2 main directories:

* Tasks -> Where the main functions are stored
* Modules -> Where scripts that interact with libraries are stored

Inside the `Tasks` folder we find 2 main tasks:

* etl.py -> Obtains the data from the API and inserts it to the Db
* makePlot.py -> Makes a request to the DB, and makes a plot.

## Configuration

We've created a file inside the `Tasks` folder called `config.py` where we stored all the values to make the script work.

* mSymbols -> Array specifing the symbols to obtain data, and make the plot.
* API Key -> String containing Alphavantage's API Key

## The API

Following your recommendations, we've used `Alphavantage` services.
Completing the variables in the link will respond with the latest 100 stock values corresponding to the requested symbol, separated by an interval of 15 minutes.

`API Link: https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=15min&symbol={Symbol}&apikey={API_Key}`

This request is made by the module `WebRequests.py`


## Create tables

With the help of SQLAlchemy we made a class called `StockValue` to interact with the database.
(Stored in ./Modules/`Classes.py`)

With that class we've created a table composed with the following columns:

| nombre       | tipo     | descripcion                          |
|--------------|----------|--------------------------------------|
| id           | integer  | Auto Increment Identifier            |
| date         | date     | Symbol identifier from the data      |
| symbol       | text     | Date according to the stock          |
| open         | smallint | Value where the candle opened        |
| high         | smallint | Top value reached by the candle      |
| low          | smallint | Lowest value reached by the candle   |
| close        | smallint | Value where the candle closed        |


## Plotting

To make the plot we have the function `candlestick2_ohlc` from the library `mplfinance` which will help us to make the candle graph required to draw stocks.

With a request to the db we obtain `date, open, high, low, close` for each Symbol in the period of the last 7 days. Then we make a call to the module `PlotLib.py` which draws the graph and saves it to `./Tasks/Exports` as a .png picture.


## Pytest

To check that the script is working as expected, we use the `pytest` library, we had to setup some code with assert functions, to check values.

In the directory `./Modules/Test/` we find those scripts.

* test_etl.py -> Will make an API request, and make sure it responds with all the required values
* test_plot.py -> Will make a request to the DB, and make sure its working, and provides a good amount of data to make the plot.

### GitHub Actions

In the `Settings` of the repo, we have an option to add our own worker. With the steps they give we can setup a runner inside Airflow, so we can program it to run the pytest script and check that everything is working correctly.

We have the option to make its own .yml config file, where we specify the commands to execute and its schedule:

* This will run every time a Push is made to the repo.
* `cd` inside the Tasks directory, and execute pytest.

Then, the log will accesible in the `Actions` tab, inside `pytest.yml` in the Pytest log. With this we make sure that both scripts passed the check.