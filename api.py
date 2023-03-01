import requests
import pandas as pd
# state annual coal consumption (more than 5,000 data)
url = 'https://api.eia.gov/v2/coal/consumption-and-quality/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=consumption&data[1]=price&facets[location][]=80&facets[location][]=81&facets[location][]=82&facets[location][]=83&facets[location][]=84&facets[location][]=85&facets[location][]=86&facets[location][]=87&facets[location][]=88&facets[location][]=89&facets[location][]=90&facets[location][]=AK&facets[location][]=AL&facets[location][]=AR&facets[location][]=AZ&facets[location][]=CA&facets[location][]=CO&facets[location][]=CT&facets[location][]=DC&facets[location][]=DE&facets[location][]=ENC&facets[location][]=ESC&facets[location][]=FL&facets[location][]=GA&facets[location][]=HI&facets[location][]=IA&facets[location][]=ID&facets[location][]=IL&facets[location][]=IN&facets[location][]=KS&facets[location][]=KY&facets[location][]=LA&facets[location][]=MA&facets[location][]=MAT&facets[location][]=MD&facets[location][]=ME&facets[location][]=MI&facets[location][]=MN&facets[location][]=MO&facets[location][]=MS&facets[location][]=MT&facets[location][]=MTN&facets[location][]=NC&facets[location][]=ND&facets[location][]=NE&facets[location][]=NEW&facets[location][]=NH&facets[location][]=NJ&facets[location][]=NM&facets[location][]=NV&facets[location][]=NY&facets[location][]=OH&facets[location][]=OK&facets[location][]=OR&facets[location][]=PA&facets[location][]=PCC&facets[location][]=PCN&facets[location][]=PR&facets[location][]=RI&facets[location][]=SAT&facets[location][]=SC&facets[location][]=SD&facets[location][]=TN&facets[location][]=TX&facets[location][]=US&facets[location][]=UT&facets[location][]=VA&facets[location][]=VT&facets[location][]=WA&facets[location][]=WI&facets[location][]=WNC&facets[location][]=WSC&facets[location][]=WV&facets[location][]=WY&start=2006&end=2022&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_coal_consumption = pd.DataFrame(test['response']['data'])
df_coal_consumption.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/coal_consumption.csv')

url = 'https://api.eia.gov/v2/coal/consumption-and-quality/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=consumption&data[1]=price&facets[location][]=80&facets[location][]=81&facets[location][]=82&facets[location][]=83&facets[location][]=84&facets[location][]=85&facets[location][]=86&facets[location][]=87&facets[location][]=88&facets[location][]=89&facets[location][]=90&facets[location][]=AK&facets[location][]=AL&facets[location][]=AR&facets[location][]=AZ&facets[location][]=CA&facets[location][]=CO&facets[location][]=CT&facets[location][]=DC&facets[location][]=DE&facets[location][]=ENC&facets[location][]=ESC&facets[location][]=FL&facets[location][]=GA&facets[location][]=HI&facets[location][]=IA&facets[location][]=ID&facets[location][]=IL&facets[location][]=IN&facets[location][]=KS&facets[location][]=KY&facets[location][]=LA&facets[location][]=MA&facets[location][]=MAT&facets[location][]=MD&facets[location][]=ME&facets[location][]=MI&facets[location][]=MN&facets[location][]=MO&facets[location][]=MS&facets[location][]=MT&facets[location][]=MTN&facets[location][]=NC&facets[location][]=ND&facets[location][]=NE&facets[location][]=NEW&facets[location][]=NH&facets[location][]=NJ&facets[location][]=NM&facets[location][]=NV&facets[location][]=NY&facets[location][]=OH&facets[location][]=OK&facets[location][]=OR&facets[location][]=PA&facets[location][]=PCC&facets[location][]=PCN&facets[location][]=PR&facets[location][]=RI&facets[location][]=SAT&facets[location][]=SC&facets[location][]=SD&facets[location][]=TN&facets[location][]=TX&facets[location][]=US&facets[location][]=UT&facets[location][]=VA&facets[location][]=VT&facets[location][]=WA&facets[location][]=WI&facets[location][]=WNC&facets[location][]=WSC&facets[location][]=WV&facets[location][]=WY&start=1999&end=2005&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_coal_consumption = pd.DataFrame(test['response']['data'])
df_coal_consumption.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/coal_consumption2.csv')

# US quarterly coal consumption
url = 'https://api.eia.gov/v2/coal/consumption-and-quality/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=quarterly&data[0]=consumption&facets[location][]=US&start=2000-Q1&end=2021-Q1&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_us_consumption = pd.DataFrame(test['response']['data'])
df_us_consumption.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/coal_us_consumption.csv', index=False)

# state annual coal market sales price
url = 'https://api.eia.gov/v2/coal/market-sales-price/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=price&data[1]=sales&facets[stateRegionId][]=AK&facets[stateRegionId][]=AL&facets[stateRegionId][]=APC&facets[stateRegionId][]=APN&facets[stateRegionId][]=APP&facets[stateRegionId][]=APS&facets[stateRegionId][]=AR&facets[stateRegionId][]=AZ&facets[stateRegionId][]=CO&facets[stateRegionId][]=EMR&facets[stateRegionId][]=ENC&facets[stateRegionId][]=ESC&facets[stateRegionId][]=EST&facets[stateRegionId][]=IL&facets[stateRegionId][]=ILL&facets[stateRegionId][]=IN&facets[stateRegionId][]=INO&facets[stateRegionId][]=INT&facets[stateRegionId][]=KS&facets[stateRegionId][]=KY&facets[stateRegionId][]=KYE&facets[stateRegionId][]=KYW&facets[stateRegionId][]=LA&facets[stateRegionId][]=MAT&facets[stateRegionId][]=MD&facets[stateRegionId][]=MID&facets[stateRegionId][]=MO&facets[stateRegionId][]=MS&facets[stateRegionId][]=MT&facets[stateRegionId][]=MTN&facets[stateRegionId][]=ND&facets[stateRegionId][]=NM&facets[stateRegionId][]=OH&facets[stateRegionId][]=OK&facets[stateRegionId][]=PA&facets[stateRegionId][]=PAA&facets[stateRegionId][]=PAB&facets[stateRegionId][]=PCC&facets[stateRegionId][]=PCN&facets[stateRegionId][]=PRB&facets[stateRegionId][]=SAT&facets[stateRegionId][]=STH&facets[stateRegionId][]=TN&facets[stateRegionId][]=TX&facets[stateRegionId][]=UNT&facets[stateRegionId][]=US&facets[stateRegionId][]=UT&facets[stateRegionId][]=VA&facets[stateRegionId][]=WA&facets[stateRegionId][]=WBO&facets[stateRegionId][]=WMR&facets[stateRegionId][]=WNC&facets[stateRegionId][]=WSB&facets[stateRegionId][]=WSC&facets[stateRegionId][]=WST&facets[stateRegionId][]=WV&facets[stateRegionId][]=WVN&facets[stateRegionId][]=WVS&facets[stateRegionId][]=WY&start=2001&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_coal_market_price = pd.DataFrame(test['response']['data'])
df_coal_market_price.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/coal_market_price.csv')


# state annual electricity net metering (more than 5,000 data)
url = 'https://api.eia.gov/v2/electricity/state-electricity-profiles/net-metering/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=capacity&data[1]=customers&facets[state][]=AK&facets[state][]=AL&facets[state][]=AR&facets[state][]=AZ&facets[state][]=CA&facets[state][]=CO&facets[state][]=CT&facets[state][]=DC&facets[state][]=DE&facets[state][]=FL&facets[state][]=GA&facets[state][]=HI&facets[state][]=IA&facets[state][]=ID&facets[state][]=IL&facets[state][]=IN&facets[state][]=KS&facets[state][]=KY&facets[state][]=LA&facets[state][]=MA&facets[state][]=MD&facets[state][]=ME&facets[state][]=MI&facets[state][]=MN&facets[state][]=MO&facets[state][]=MS&facets[state][]=MT&facets[state][]=NC&facets[state][]=ND&facets[state][]=NE&facets[state][]=NH&facets[state][]=NJ&facets[state][]=NM&facets[state][]=NV&facets[state][]=NY&facets[state][]=OH&facets[state][]=OK&facets[state][]=OR&facets[state][]=PA&facets[state][]=RI&facets[state][]=SC&facets[state][]=SD&facets[state][]=TN&facets[state][]=TX&facets[state][]=US&facets[state][]=UT&facets[state][]=VA&facets[state][]=VT&facets[state][]=WA&facets[state][]=WI&facets[state][]=WV&facets[state][]=WY&start=2013&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_elec_meter = pd.DataFrame(test['response']['data'])
df_elec_meter.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/elec_meter.csv')

# state cost and savings from energy efficiency programs
url = 'https://api.eia.gov/v2/electricity/state-electricity-profiles/energy-efficiency/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=all-other-costs&data[1]=customer-incentive&data[2]=energy-savings&facets[state][]=AK&facets[state][]=AL&facets[state][]=AR&facets[state][]=AZ&facets[state][]=CA&facets[state][]=CO&facets[state][]=CT&facets[state][]=DC&facets[state][]=DE&facets[state][]=FL&facets[state][]=GA&facets[state][]=HI&facets[state][]=IA&facets[state][]=ID&facets[state][]=IL&facets[state][]=IN&facets[state][]=KS&facets[state][]=KY&facets[state][]=LA&facets[state][]=MA&facets[state][]=MD&facets[state][]=ME&facets[state][]=MI&facets[state][]=MN&facets[state][]=MO&facets[state][]=MS&facets[state][]=MT&facets[state][]=NC&facets[state][]=ND&facets[state][]=NE&facets[state][]=NH&facets[state][]=NJ&facets[state][]=NM&facets[state][]=NV&facets[state][]=NY&facets[state][]=OH&facets[state][]=OK&facets[state][]=OR&facets[state][]=PA&facets[state][]=RI&facets[state][]=SC&facets[state][]=SD&facets[state][]=TN&facets[state][]=TX&facets[state][]=US&facets[state][]=UT&facets[state][]=VA&facets[state][]=VT&facets[state][]=WA&facets[state][]=WI&facets[state][]=WV&facets[state][]=WY&start=2013&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_cost_n_saving = pd.DataFrame(test['response']['data'])
df_cost_n_saving.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/cost_n_saving.csv')

# state emissions from energy consumption (more than 5,000 data)
url = 'https://api.eia.gov/v2/electricity/state-electricity-profiles/emissions-by-state-by-fuel/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=co2-rate-lbs-mwh&data[1]=co2-thousand-metric-tons&data[2]=so2-rate-lbs-mwh&data[3]=so2-short-tons&facets[stateid][]=AK&facets[stateid][]=AL&facets[stateid][]=AR&facets[stateid][]=AZ&facets[stateid][]=CA&facets[stateid][]=CO&facets[stateid][]=CT&facets[stateid][]=DC&facets[stateid][]=DE&facets[stateid][]=FL&facets[stateid][]=GA&facets[stateid][]=HI&facets[stateid][]=IA&facets[stateid][]=ID&facets[stateid][]=IL&facets[stateid][]=IN&facets[stateid][]=KS&facets[stateid][]=KY&facets[stateid][]=LA&facets[stateid][]=MA&facets[stateid][]=MD&facets[stateid][]=ME&facets[stateid][]=MI&facets[stateid][]=MN&facets[stateid][]=MO&facets[stateid][]=MS&facets[stateid][]=MT&facets[stateid][]=NC&facets[stateid][]=ND&facets[stateid][]=NE&facets[stateid][]=NH&facets[stateid][]=NJ&facets[stateid][]=NM&facets[stateid][]=NV&facets[stateid][]=NY&facets[stateid][]=OH&facets[stateid][]=OK&facets[stateid][]=OR&facets[stateid][]=PA&facets[stateid][]=RI&facets[stateid][]=SC&facets[stateid][]=SD&facets[stateid][]=TN&facets[stateid][]=TX&facets[stateid][]=US&facets[stateid][]=UT&facets[stateid][]=VA&facets[stateid][]=VT&facets[stateid][]=WA&facets[stateid][]=WI&facets[stateid][]=WV&facets[stateid][]=WY&start=1990&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_emissions_from_elec = pd.DataFrame(test['response']['data'])
df_emissions_from_elec.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/emissions_from_elec.csv')


# crude oil imports (more than 5,000 data)
url = 'https://api.eia.gov/v2/crude-oil-imports/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=quantity&start=2009&end=2022&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_crude_oil_import = pd.DataFrame(test['response']['data'])
df_crude_oil_import.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/crude_oil_import.csv')

# international annual different categories
url = 'https://api.eia.gov/v2/international/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=value&facets[productId][]=116&facets[productId][]=28&facets[productId][]=3002&facets[productId][]=4002&facets[productId][]=4008&facets[productId][]=4411&facets[productId][]=4413&facets[productId][]=4419&facets[productId][]=4701&facets[productId][]=6798&start=1949&end=2022&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_international_annual = pd.DataFrame(test['response']['data'])
df_international_annual.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/international_annual.csv')

# annual natural gas prices (more than 5,000 data)
url = 'https://api.eia.gov/v2/natural-gas/pri/sum/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=value&facets[process][]=FWA&facets[process][]=PCS&facets[process][]=PDV&facets[process][]=PEU&facets[process][]=PEX&facets[process][]=PG1&facets[process][]=PGP&facets[process][]=PIN&facets[process][]=PM0&facets[process][]=PML&facets[process][]=PNG&facets[process][]=PNP&facets[process][]=PRP&facets[process][]=PRS&facets[process][]=VFA&facets[process][]=VFC&facets[process][]=VRX&start=1967&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_natural_gas_prices = pd.DataFrame(test['response']['data'])
df_natural_gas_prices.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/natural_gas_prices.csv')

# annual natural gas import and export by country
url = 'https://api.eia.gov/v2/natural-gas/move/expc/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=value&facets[product][]=EPG0&start=1973&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_natural_gas_importexport = pd.DataFrame(test['response']['data'])
df_natural_gas_importexport.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/natural_gas_importexport.csv')

# daily U.S. nuclear outages
url = 'https://api.eia.gov/v2/nuclear-outages/us-nuclear-outages/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=daily&data[0]=capacity&data[1]=outage&data[2]=percentOutage&start=2007-01-01&end=2022-12-31&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_us_nuclear_outage = pd.DataFrame(test['response']['data'])
df_us_nuclear_outage.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/us_nuclear_outage.csv')

# state energy data system
url = 'https://api.eia.gov/v2/seds/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=value&facets[stateId][]=AK&facets[stateId][]=AL&facets[stateId][]=AR&facets[stateId][]=AZ&facets[stateId][]=CA&facets[stateId][]=CO&facets[stateId][]=CT&facets[stateId][]=DC&facets[stateId][]=DE&facets[stateId][]=FL&facets[stateId][]=GA&facets[stateId][]=HI&facets[stateId][]=IA&facets[stateId][]=ID&facets[stateId][]=IL&facets[stateId][]=IN&facets[stateId][]=KS&facets[stateId][]=KY&facets[stateId][]=LA&facets[stateId][]=MA&facets[stateId][]=MD&facets[stateId][]=ME&facets[stateId][]=MI&facets[stateId][]=MN&facets[stateId][]=MO&facets[stateId][]=MS&facets[stateId][]=MT&facets[stateId][]=NC&facets[stateId][]=ND&facets[stateId][]=NE&facets[stateId][]=NH&facets[stateId][]=NJ&facets[stateId][]=NM&facets[stateId][]=NV&facets[stateId][]=NY&facets[stateId][]=OH&facets[stateId][]=OK&facets[stateId][]=OR&facets[stateId][]=PA&facets[stateId][]=RI&facets[stateId][]=SC&facets[stateId][]=SD&facets[stateId][]=TN&facets[stateId][]=TX&facets[stateId][]=US&facets[stateId][]=UT&facets[stateId][]=VA&facets[stateId][]=VT&facets[stateId][]=WA&facets[stateId][]=WI&facets[stateId][]=WV&facets[stateId][]=WY&facets[stateId][]=X3&facets[stateId][]=X5&start=1960&end=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_state_energy_system = pd.DataFrame(test['response']['data'])
df_state_energy_system.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/state_energy_system.csv')

# state annual CO2 emissions (more than 5,000 data)
url = 'https://api.eia.gov/v2/co2-emissions/co2-emissions-and-carbon-coefficients/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=carbon-coefficient&data[1]=emissions&facets[stateId][]=AK&facets[stateId][]=AL&facets[stateId][]=AR&facets[stateId][]=AZ&facets[stateId][]=CA&facets[stateId][]=CO&facets[stateId][]=CT&facets[stateId][]=DC&facets[stateId][]=DE&facets[stateId][]=FL&facets[stateId][]=GA&facets[stateId][]=HI&facets[stateId][]=IA&facets[stateId][]=ID&facets[stateId][]=IL&facets[stateId][]=IN&facets[stateId][]=KS&facets[stateId][]=KY&facets[stateId][]=LA&facets[stateId][]=MA&facets[stateId][]=MD&facets[stateId][]=ME&facets[stateId][]=MI&facets[stateId][]=MN&facets[stateId][]=MO&facets[stateId][]=MS&facets[stateId][]=MT&facets[stateId][]=NC&facets[stateId][]=ND&facets[stateId][]=NE&facets[stateId][]=NH&facets[stateId][]=NJ&facets[stateId][]=NM&facets[stateId][]=NV&facets[stateId][]=NY&facets[stateId][]=OH&facets[stateId][]=OK&facets[stateId][]=OR&facets[stateId][]=PA&facets[stateId][]=RI&facets[stateId][]=SC&facets[stateId][]=SD&facets[stateId][]=TN&facets[stateId][]=TX&facets[stateId][]=UT&facets[stateId][]=VA&facets[stateId][]=VT&facets[stateId][]=WA&facets[stateId][]=WI&facets[stateId][]=WV&facets[stateId][]=WY&start=1980&end=2018&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_state_CO2_emissions = pd.DataFrame(test['response']['data'])
df_state_CO2_emissions.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/state_CO2_emissions.csv')

# state annual CO2 emissions by fuel
url = 'https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/?api_key=jcpuhfCaFinqTpsqrOm3CpuRj4z4v0NShln4FIG6&frequency=annual&data[0]=value&facets[fuelId][]=CO&facets[fuelId][]=NG&facets[fuelId][]=PE&facets[fuelId][]=TO&start=1970&end=2020&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
response = requests.get(url)
print(response)
test = response.json()
test.keys()
test['response']['data']
df_state_CO2_emissions_by_fuel = pd.DataFrame(test['response']['data'])
df_state_CO2_emissions_by_fuel.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/state_CO2_emissions_by_fuel.csv')


