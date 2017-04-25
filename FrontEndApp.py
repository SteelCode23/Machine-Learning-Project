''' Create a simple stocks correlation dashboard.
Choose stocks to compare in the drop down widgets, and make selections
on the plots to update the summary and histograms accordingly.
.. note::
    Running this example requires downloading sample data. See
    the included `README`_ for more information.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve stocks
at your command prompt. Then navigate to the URL
    http://localhost:5006/stocks
.. _README: https://github.com/bokeh/bokeh/blob/master/examples/app/stocks/README.md
'''
import requests
import pandas as pd

DEFAULT_TICKERS = ['ZYNE','ZDPY','XXII','VRCI','VPOR','VPCO','VHUB','VGPR','UBQU','TWMJF','TURV','TRTC','TECR','TAUG','STEV','SRNA','SPRWF','SMG','SIPC','SING','RSSFF','RMHB','RMHB','QEDN','publ','PRRE','PNTV','PLPL','PKPH','PHOT','OXIS','OGRMF','NVLX','NTRR','NGBL','NDEV','MYHI','MYEC','MSRT','MQTRF','MNTR','MJNE','MJNA','MJN','MJMJ','MDCL','MCIG','LXRP','KSHB','KAYS','INSY','INQD','INCC','IMLFF','IIPR','IGPK','IGC','ICBU','HLIX','HEMP','GYOG','GWPH','GRNH','GRCU','GBLX','FWDG','FULL','FITX','FBEC','ERBB','ENCC','EMMBF','EDXC','EAPH','DIDG','DEWM','CVSI','CVSI','CNAB','CHUM','CGRW','CBIS','CBDS','CARA','CANN','BTFL','BLPG','AXIM','ATTBF','APHQF','AMMJ','AGTK','AGSTF','AERO','ACBFF','ACAN','ABBV']
stocks = DEFAULT_TICKERS
for stock in stocks:
    print(stock)
    try:
        data = requests.get("http://chart.finance.yahoo.com/table.csv?s="+stock.lower()+"&a=2&b=15&c=2015&d=4&e=15&f=2017&g=d&ignore=.csv")
        print(data)
        f = open("C:/Users/Steel/Projects/Stock-Predictor-master/daily/table_"+stock.lower()+".csv", 'w' )
        f.write(data.text)
        f.close()
        df = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/table_"+stock.lower()+".csv")
        del df['Open']
        def CleanData(a):
            a = str(a)
            year  = a.split("-")[0]
            month = a.split("-")[1]
            date  = a.split("-")[2]
            return str(year)+str(month)+str(date)
        print(df.columns)
        df['Date']
        df['High']=0
        df['Low'].round(decimals=4)
        df['Close'].round(decimals=4)
        df['Volume'].round(decimals=2)
        df['Adj Close'].round(decimals=4)
        df['Adj Close'], df['Volume'] = df['Volume'],df['Adj Close']
        df['Date'] = df['Date'].map(lambda x:CleanData(x))
        df.sort_values(by='Date',ascending=True, inplace=True)
        df.to_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/table_"+stock.lower()+".csv", index=False)
        df.to_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/Columntable_"+stock.lower()+".csv", index=False)        
        df = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/table_"+stock.lower()+".csv",skiprows=1)
        df.to_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/table_"+stock.lower()+".csv", index=False)
        df = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/table_"+stock.lower()+".csv", skiprows=1)
        print(df.head())
    except Exception as e:
        print("FAILED %s",stock)
        DEFAULT_TICKERS.remove(stock)


''' Create a simple stocks correlation dashboard.'''

try:
    from functools import lru_cache
except ImportError:
    # Python 2 does stdlib does not have lru_cache so let's just
    # create a dummy decorator to avoid crashing
    print ("WARNING: Cache for this example is available on Python 3 only.")
    def lru_cache():
        def dec(f):
            def _(*args, **kws):
                return f(*args, **kws)
            return _
        return dec

from os.path import dirname, join

import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import PreText, Select
from bokeh.plotting import figure

DATA_DIR = "C:\\Users\\Steel\\Projects\\Stock-Predictor-mastertable\\daily\\"


def nix(val, lst):
    return [x for x in lst if x != val]

@lru_cache()
def load_ticker(ticker):
    fname = 'C:/Users/Steel/Projects/Stock-Predictor-master/daily/table_' + ticker.lower() + '.csv'
    data = pd.read_csv(fname, header=None, parse_dates=['date'],
                       names=['date', 'foo', 'o', 'h', 'l', 'c', 'v'])
    data = data.set_index('date')
    return pd.DataFrame({ticker: data.c, ticker+'_returns': data.c.diff()})

@lru_cache()
def get_data(t1, t2):
    df1 = load_ticker(t1)
    df2 = load_ticker(t2)
    data = pd.concat([df1, df2], axis=1)
    data = data.dropna()
    data['t1'] = data[t1]
    data['t2'] = data[t2]
    data['t1_returns'] = data[t1+'_returns']
    data['t2_returns'] = data[t2+'_returns']
    return data

# set up widgets

stats = PreText(text='', width=500)
ticker1 = Select(value='ZYNE', options=nix('ZDPY', DEFAULT_TICKERS))
ticker2 = Select(value='ZDPY', options=nix('ZYNE', DEFAULT_TICKERS))

# set up plots

source = ColumnDataSource(data=dict(date=[], t1=[], t2=[], t1_returns=[], t2_returns=[]))
source_static = ColumnDataSource(data=dict(date=[], t1=[], t2=[], t1_returns=[], t2_returns=[]))
tools = 'pan,wheel_zoom,xbox_select,reset'

corr = figure(plot_width=350, plot_height=350,
              tools='pan,wheel_zoom,box_select,reset')
corr.circle('t1_returns', 't2_returns', size=2, source=source,
            selection_color="orange", alpha=0.6, nonselection_alpha=0.1, selection_alpha=0.4)

ts1 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ts1.line('date', 't1', source=source_static)
ts1.circle('date', 't1', size=1, source=source, color=None, selection_color="orange")

ts2 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ts2.x_range = ts1.x_range
ts2.line('date', 't2', source=source_static)
ts2.circle('date', 't2', size=1, source=source, color=None, selection_color="orange")

# set up callbacks

def ticker1_change(attrname, old, new):
    ticker2.options = nix(new, DEFAULT_TICKERS)
    update()

def ticker2_change(attrname, old, new):
    ticker1.options = nix(new, DEFAULT_TICKERS)
    update()

def update(selected=None):
    t1, t2 = ticker1.value, ticker2.value

    data = get_data(t1, t2)
    source.data = source.from_df(data[['t1', 't2', 't1_returns', 't2_returns']])
    source_static.data = source.data

    update_stats(data, t1, t2)

    corr.title.text = '%s returns vs. %s returns' % (t1, t2)
    ts1.title.text, ts2.title.text = t1, t2

def update_stats(data, t1, t2):
    stats.text = str(data[[t1, t2, t1+'_returns', t2+'_returns']].describe())

ticker1.on_change('value', ticker1_change)
ticker2.on_change('value', ticker2_change)

def selection_change(attrname, old, new):
    t1, t2 = ticker1.value, ticker2.value
    data = get_data(t1, t2)
    selected = source.selected['1d']['indices']
    if selected:
        data = data.iloc[selected, :]
    update_stats(data, t1, t2)

source.on_change('selected', selection_change)

# set up layout
widgets = column(ticker1, ticker2, stats)
main_row = row(corr, widgets)
series = column(ts1, ts2)
layout = column(main_row, series)

# initialize
update()

curdoc().add_root(layout)
curdoc().title = "Stocks"