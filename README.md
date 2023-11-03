# Bitget_-token_analysis

$TOKEN Bitget listing trade data forensic research
By Moudinho3 – Twtr: @moudinho3
These are the python files and outputs used to generate the analysis


Background
The Floki team launched the TokenFi token. Bitget, an exchange, went against the project's wishes and listed a the token before it officially launched. They traded large volumes of the token without having any to cover user withdrawals. Bitget ALLEGEDLY refused to cooperate and tried to make an OTC deal at a discount to purchase the missing toknes. The project called out Bitget's actions, leading Bitget to hastily delist the token.Bitget announced a buyback plan, going against it’s own terms of service, acting in illegal fashion.I share with you the data of Bitget’s actions, the financial impact and value of the “hole” and publicly call out their actions.Furthermore i call out ALLEGEDLY illegal and manipulative industry actions by Bitget, as well as fraud, deception and market manipulation.Ironically, there stand unsubstantiated accusations against the Floki team for market manipulation yet $FLOKI is still listed and trading on Bitget.

Links & Sources:
Bitget Lists TokenFi:
https://www.bitget.com/support/articles/12560603799524
Bitget Delists TokenFo:https://www.bitget.com/support/articles/12560603799638
Data for Research:
Bitget API
GitHub:
https://github.com/InAMooD/Bitget_-token_analysis


To protect the integrity of the research you can access the code used to source the data and to calculate the figures here: https://github.com/InAMooD/-TOKEN_Bitget_Fraud


Trade Data
Trading started 27/10/2023 17:00 GMT+2
Ended on 31/10/2023 09:10 GMT+2No tokens have been depositedNo tokens have been withdrawnThis allows me to calculate the CVD to find the net missing amount of tokens and derive data from it.

Overview of data
Calculate CVD to identify the missing token amount from Bitget. We do so by comparing net buying and selling with the source trade by trade data.Source data sample:symbol,tradeId,side,fillPrice,fillQuantity,fillTime
TOKENUSDT_SPBL,1101813802653372607,Buy,0.00004975,492244.41,1698418801000
TOKENUSDT_SPBL,1101813802653372605,Buy,0.0000497,202147.16,1698418801000

CVD Formula: (TL;DR it’s correct.)        price = float(row['fillPrice'])
        quantity = float(row['fillQuantity'])
        trade_value = price * quantity
        if side == 'Buy':
            cumulated_volume_delta += quantity
        else:
            cumulated_volume_delta -= quantity





Analysis
The calculated bitget_loss = (0.00605001 - vwap) * cumulated_volume_deltaMarket value at buyback time = mkt_val_buyback_time_announcement = 671829575 * 0.021635
Estimated that Bitget issued over half the volume in non-existing tokens, with a 14m USD hole at time of Buyback announcement. approximately 
Estimated 30m USD hole at Buyback execution ( On-chainMark price 0,04), (without accounting liquidity)
Estimated Realised loss of 1.1m USD due to shady Buyback*
Estimated to be illegal consumer protection laws Excluding negligible fee revenue*
In another world this is how an exchange blows up and rekts it’s customers! Remember FTX?

Analysis
Bitget did not stop trading immediately after first rumors.
Bitget and it’s representatives let customers buy & sell the tokens at high market prices, without public comments stating withdrawals will come.

Analysis
Bitget let customers buy the coin over long time to mitigate its losses.
Combination of lying about opening withdrawals (see next slides) and allowing trading to mitigate losses and to bait arbitrage volume.
Uptrending CVD means the exchange keeps issuing naked Tokens.

Analysis
Bitget let customers buy the coin over long time to mitigate its losses.
Combination of lying about opening withdrawals (see next slides) and allowing trading to mitigate losses and to bait arbitrage volume.

Industry risk & skem tactics
Could have been a FTX situation, as price deviated strongly from spot price on-chain.
At Buyback time, 10x valuation would have blown up the insurance fund.
Instead customers and honest traders takes the L.
As of current knowledge, no reparations have been offered to customers who purchased above buyback price.

Revenue vs risk
Total Volume
1 269 807 189
Undiscounted Fee Rate
0.1%
Fee Revenue
12 698 071
Buyback value
$ 7682,34 
Bitget generated very little revenue with these actions, so my assumption is that there was:Eithera directional bet internallyOrAn honest mistake solved with a not practices


In my opinion,Such actions jeopardize customers, traders, and even the exchange solvency itself.

Bitget’s core values
No further comment needed, as the actions of Bitget were exactly the opposite.

Bitget’s communication
Bitget communication was very clearly towards reopening withdrawals.
It is estimated that these tactics may have been employed 
Partially redacted to protect anonymity of Bitget rep.

Conclusion (Opinionated)
Market Safety conclusion:Bitget has engaged in fraudulent activities, breaking Terms of Service and Consumer protection law.It is our duty as customers to call out these actions. We have the luck that most exchanges have excellent API’s and we can source all the data we want to analyse and check these allegedly fraudulent practices.It is upon ourselves to fight and expose these practices to make exchanges safer and improve best practices.It is also upon ourselves to report to regulatory authorities such practices.We as traders and crypto natives are used to taking a loss and moving on, but maybe once in a while if the counterpart tries to screw you over, consider working a few days to expose it.Data conclusion:The generated fees were an estimated ~7.614 USD and i do not see how an exchange takes such risks for 7614 dollars, unless there is pre-meditation and intent to deceive.
What can i do?:Maybe you can sue, i don’t know not a lawyer,i do think you could lever a country's consumer protection laws.You can also report this to financial regulatory authorities.

Contact:
You can contact me on Twitter @Moudinho3
