#define CAGR function
def CAGR(name, assetData, interval):
    time = len(assetData)
    end = time - 1

    #calculate history length in years
    years = time * interval / 365
    years = round(years,2)

    #calculate total return and CAGR
    invReturn = (assetData[end] - assetData[0] ) / assetData[0]
    CAGR = (invReturn ** (1/years) -1)* 100
    CAGR = round(CAGR,1)

    print(f"{name} has an investment history of {years} years and a CAGR of {CAGR}%")
    print(f"{invReturn}^1/{years} -1 )*100")
