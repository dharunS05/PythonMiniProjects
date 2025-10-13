#====================================================
#Currency Converter Using Api
#====================================================

#Import Required packages
#=====================================================
import requests

#conect the api
#=====================================================
def connect_api(url):
    data = requests.get(url).json()
    return data

#create function for currency converter
#=====================================================
def currency_converter(amount,from_currency,to_currency,currency):
    try:
        
        data = currency
        currency_rate = data['conversion_rates']
        if data['result'] == 'success':
            if from_currency == to_currency:
                return amount

            if from_currency not in currency_rate and to_currency not in currency_rate:
                print("Both Currency Not in currency rate list ....!")
                return None

            # convert from amount into usd
            usd_convert_base = amount / currency_rate[from_currency]  

            #convert to amount into usd
            to_conversion_rate = currency_rate[to_currency]

            #final currency amount
            final_currency = usd_convert_base*to_conversion_rate

            return final_currency

    except Exception as e:
        print("Error:",e)

if __name__ =="__main__":

    print("#=====================================================")
    print("# Currency Converter")
    print("#=====================================================")
    url='https://v6.exchangerate-api.com/v6/a166a07054c4dce48548577ecls/latest/USD'
    data = connect_api(url)
    while True:

        amount =int(input("Enter Amount:"))
        from_currency = input("Enter Currency Name:").upper()
        to_currency = input("Enter Converting Currency Name:").upper()
        

        #calling currency_converter function
        #===============================================================
        converter=currency_converter(amount,from_currency,to_currency,data)

        #print the Value
        print(f'{amount} {from_currency} in {converter} {to_currency}')

        print('#============================================================')
        choice = input("Do You want continue[0/1]: ")
        if choice != '1':
            break