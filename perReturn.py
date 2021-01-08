#import data and set test values
import data as d

testAsset = "SPX500"
testData = d.SPX500
testData.reverse()
testInterval = 7
testLookBack = 4


#define function
def perReturn(name, assetData, interval, lookBack):
    

    #initialize starting values
    time = interval * lookBack
    end = len(assetData) - lookBack + 1
    lastIndex = lookBack - 1
    index = 0
    returnList = []
    invReturn = 0

    #calculate periodic % returns for the lookback span and save it in a new list
    while index < end:
        invReturn = ((assetData[lastIndex + index] / assetData[index] - 1) * 100)
        invReturn = round(invReturn,1)
        returnList.append(invReturn)
        index = index + 1
    
    #find the period with the highest return
    maxReturn = max(returnList)
    maxIndex = returnList.index(maxReturn)

    #display the results
    print(returnList)
    print()
    print(f"The return of {name} during the last observation period of {time} days was {invReturn}%")
    print(f"The maximum return was {maxReturn}% at place {maxIndex}")

#call the function
perReturn(testAsset, testData, testInterval, testLookBack)