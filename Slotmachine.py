import random


MAX_LINES = 3
MIN_BET= 1
MAX_BET=100
MIN_LINES=1

ROW=3
COL=3



symbols_count={

    "A":3,
    "B":4,
    "C":5,
    "D":3,

}
symbols_value={

    "A":3,
    "B":2,
    "C":8,
    "D":3,

}



def check_winning(lines,symbols,values,bet):

    winnings=0
    winning_lines=[]     
    for line in range(lines):
        symbol=symbols[0][line]  
        for i in symbols:
            
            check_symbol=i[line]
            if check_symbol!=symbol:
                break  
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines    
            
  
                 



def spin(row,col,symbols):

    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    list_symbols = []
    for _ in range(row):
        list_symnol=[]
        for _ in range(col):
            current_symbols=all_symbols[:]
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            list_symnol.append(value)
        list_symbols.append(list_symnol)    
    return list_symbols




def print_spin(symbols):
    # for i in range(len(symbols[0])):
    #     for j,k in enumerate(symbols):
    #         if j == len(symbols)-1:
    #             print(i[k], end="|")
    #         else:
    #             print(k, end="")   

    #     print()
    
    for i in range(len(symbols[0])):
        for k,j in enumerate(symbols):
            if k != len(symbols)-1:
                print(j[i], end=" | ")
            else:
                print(j[i], end=" ")    
        print()
    
 

def get_deposit():
    while True:
        deposit=input("Please enter your deposit ")
        if deposit.isdigit():
            deposit=int(deposit)
            if  deposit >0:
                break
            else:
                print(f"please enter between {MIN_BET} and {MAX_BET} amount ")
        else: 
            print("please enter valid number ")
    return deposit
    
def num_lines():
    while True:
        lines=input("Please enter number of lines you want to bet on. (1-3) ")
        
        if lines.isdigit():
            lines=int(lines)
            if  1<=lines <=MAX_LINES:
                break
            else:
                print(f"please enter between {MIN_LINES} and {MAX_LINES} amount")
        else: 
            print("please enter valid number")
    return lines
def get_bet():
    while True:
        amount=input("Please enter amount you want to bet on each line ")
        if amount.isdigit():
            amount=int(amount)
            if  MIN_BET<=amount <=MAX_BET:
                break
            else:
                print(f"please enter between {MIN_BET} and {MAX_BET} amount")
        else: 
            print("please enter valid number")                
    return amount            



def main():
    balance=get_deposit()
    while True:
        
        
        lines=num_lines()
        bet=get_bet()
        total_bet = balance-bet
        if total_bet > balance:
            print("You are betting more than balance")


        slots=spin(ROW,COL,symbols_count)
        print(print_spin(slots))
        winnings,winning_lists=check_winning(lines,slots,symbols_value,bet)
        print(f"You won {winnings}")
        print(f"You won on line", *winning_lists)
        game=input("Enter to play or 'q' to quit " )
        print(f"Your balance is now {balance}")
        if game == "q":
            break
        
        print("")


main()
